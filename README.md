# merge-PDFs
Python script to merge multiple PDF files into a single merged PDF file via command line.

## Merge multiple PDF files
`python merge-pdfs.py -i INPUT_FILE_1.pdf INPUT_FILE_2.pdf -o OUTPUT_FILE.pdf`.

**Options**

`-i` : PDF objects to merge e.g. *INPUT_FILE_1.PDF* and *INPUT_FILE_2.pdf*

`-o` : Name of merged PDF object e.g. *OUTPUT_FILE.pdf*

## Merge folder containing multiple PDF files
`python merge-pdfs.py -f DIRECTORY_PATH -o OUTPUT_FILE.pdf`.

**Options**

`-f` : Directory that contains PDF objects to merge e.g. *DIRECTORY_PATH*

`-o` : Name of merged PDF object e.g. *OUTPUT_FILE.pdf*