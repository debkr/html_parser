# HTML Parser 1.0.0
# 14 May 2016
# A simple text reader/cleaner to handle HTML
# tagging in text files parsed from the web


# import packages
import re

# open & read text file, handling html tagging
# enter filename or quit (with default)
fname = raw_input('Enter filename or Q to quit: ')
if fname.lower() == 'q' :
    quit()
elif len(fname) == 0 :
    fname = 'defaulttextfilename.txt'

# open file or return error message
try:
    fhand = open(fname)
except:
    print 'Filename not found:', fname
    quit()

# save tagged text; clean, detag & save cleaned text
taggedtext = '' ; cleanedtext = ''
for line in fhand :
    line = line.rstrip()
    line = line.lstrip()
    if len(line) == 0 : continue
    print '\n\n', 'LINE:', line

    if re.search('^<h1', line) :
        titleline = line
        taggedtext = taggedtext + line + '\n'
        title = re.findall('^<h1.*?>(.+)</h1>$', line)
        cleanedtext = cleanedtext + 'Title: ' + title[0] + '\n'

    if re.search('^<h2', line) :
        taggedtext = taggedtext + line + '\n'
        cleanedtext = cleanedtext + 'Header: ' + (re.findall('^<h2.*?>(.+)</h2>', line))[0] + '\n'

    if re.search('^<h[3-6]', line) :
        taggedtext = taggedtext + line + '\n'
        cleanedtext = cleanedtext + 'Sub-header: ' + (re.findall('^<h[3-6].*?>(.+)</h[3-6]>', line))[0] + '\n'

    if re.search('^<em>', line) :
        taggedtext = taggedtext + line + '\n'
        cleanedtext = cleanedtext + 'Para-header: ' + (re.findall('^<em.*?>(.+)</em>', line))[0] + '\n'
        
    if re.search('^<p>', line) :
        snip = re.findall('^<p.*?>(.+)', line)
        if len(snip) < 1 : continue
        else :
            taggedtext = taggedtext + line + '\n'
            if re.search('</p>$', line) :
                # Line ends with an html tag
                cleanedtext = cleanedtext + (re.findall('^<p.*?>(.+)</p>', line))[0] + '\n'
            else :
                # Line does NOT end with an html tag
                cleanedtext = cleanedtext + (re.findall('^<p.*?>(.+)', line))[0] + '\n'

    if re.search('^<li>', line) :
        snip = re.findall('^<li>(.+)', line)
        if len(snip) < 1 : continue
        else :
            taggedtext = taggedtext + line + '\n'
            if re.search('</li>', line) :
                # Line ends with an html tag
                cleanedtext = cleanedtext + 'Bullet-point: ' + (re.findall('^<li.*?>(.+)</li>', line))[0] + '\n'
            else :
                # Line does NOT end with an html tag
                cleanedtext = cleanedtext + 'Bullet-point: ' + (re.findall('^<li.*?>(.+)', line))[0] + '\n'

    # exception-handling
    if re.search('^[A-Z,a-z]', line) :
        print '\n\n', 'Found a TEXT PARA:', line
        if re.search('^m=s', line) :
            check = raw_input('Add to file? (Y/N):')
            if check.lower() == 'y' :
                taggedtext = taggedtext + line + '\n'
                cleanedtext = cleanedtext + line + '\n'
        elif re.search('^ga\(', line) :
            check = raw_input('Add to file? (Y/N):')
            if check.lower() == 'y' :
                taggedtext = taggedtext + line + '\n'
                cleanedtext = cleanedtext + line + '\n'
        elif re.search('^\[0\]', line) :
            check = raw_input('Add to file? (Y/N):')
            if check.lower() == 'y' :
                taggedtext = taggedtext + line + '\n'
                cleanedtext = cleanedtext + line + '\n'
        else :
            taggedtext = taggedtext + line + '\n'
            cleanedtext = cleanedtext + line + '\n'

print '\n\n', 'All tagged text:', '\n', taggedtext

# save tagged text to temp file
inp = raw_input('Enter temp filename:')
tempout = inp + '.txt'
print 'Filename:', tempout
fout = open(tempout, 'w')
fout.write(taggedtext)
fout.close()


print '\n\n', 'Cleaned text:', '\n', cleanedtext

# save cleaned text to final file
inp = raw_input('Enter final filename:')
finalout = inp + '.txt'
print 'Filename:', finalout
fout = open(finalout, 'w')
fout.write(cleanedtext)
fout.close()
 
