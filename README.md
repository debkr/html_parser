# HTML Parser 1.0.0
A simple Python text reader/cleaner to handle HTML tagging in text files parsed from the web

14 May 2016

## Description

A simple text reader/cleaner to handle HTML tagging in text files parsed from the web. Please use responsibly and ethically, on files/content where you hold the necessary copyright permissions!

The program opens and reads a user-specified text file (or uses hard-coded default filename on 'enter'). Searching line by line based on html tagging, it appends only the relevant html-tagged lines to a new text string ('taggedtext'), then cleans those same lines (strips out the html following tagging) and appends the cleaned text to a new text string ('cleanedtext'), with additional labelling where relevant. Tags are handled as follows:

* \<h1\> tags: cleaned and saved, labelled as 'Title';
* \<h2\> tags: cleaned and saved, labelled as 'Header';
* \<h3\> to \<h6\> tags: cleaned and saved, labelled as 'Sub-header';
* \<em\> tags (italics): cleaned and saved, labelled as 'Para-header' (Paragraph header);
* \<p\> tags: indicate text paragraphs, cleaned and saved only (no additional labels added);
* all other tags: ignored.

The program has been hard-coded to deal with some additional commonly-identified exceptions in the cleaning process (with user input required to check and confirm action required: add to text string or ignore).

Two files are saved (user-entry required for filenames):
* One for the edited text with html tagging still retained;
* The other for the final edited, cleaned and labelled text.


Some problems to be ironed out:
* This program has problems with ASCII codes. The current work-around is to go in and perform a second, manual clean-up on the final output text file. This is too much manual intervention - need to find a way to fix this in-program.


Further improvements to be made:
* Use the 'Title' label (lowercase and stripped of whitespace) as a default output filename (with user override option);
* Add option to identify keywords, calculate their counts and append to the output file if required (see tag\_eng & blog\_tagger);
* Add option for user to identify key phrases (of 2, 3 or 4 words' length), calculate their counts and append to the output file if required (program still to be built);
* Handle other html tags as required (e.g. html tags inside cleaned/detagged text lines, such as italics, strong, etc.).


Future developments planned:
* Build program into a relevance engine by using all identified keywords/key phrases. Those keywords/phrases identified as coming from lines with header tags ( \<h1\>, \<h2\>, etc.) are to be weighted most highly, followed by words/phrases appearing most often in the paragraph text;
* Delve further into the web data headers and meta data to extract further useful info if required (+ save to output file)
* Search for all links on the page/in the text (in the body text and/or in the headers/footers) adn save to a directory (and/or append to the output file)
* Provide user with an option to follow any or the URL links identified (both internally to the domain host, and externally).
