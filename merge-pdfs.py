# Python script to merge multiple PDF files into single merged PDF file via command line.

import PyPDF2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', nargs='*', help='Input PDF file(s) to merge separated by space)')
parser.add_argument('-f', '--folder', nargs=1, help='Folder containing input PDF files to merge')
parser.add_argument('-o', '--output', nargs=1, help='Filename of merged file', required=True)

args = parser.parse_args()

option_input = args.input
option_folder = args.folder
option_output = args.output


def main():

    if option_input:
        input_files = option_input
    elif option_folder:
        input_files = [f'{os.path.join(option_folder[0], dfile)}' for dfile in os.listdir(option_folder[0])]
    else:
        input_files = None
        print('Please also specify either PDF filename(s) or folder containing PDF files to merge. Refer option --help.')

    if input_files:

        # create merged PDF object
        pdf_merge = PyPDF2.PdfFileMerger()

        # store individual PDF files to merged PDF object
        for input_file in input_files:
            pdf_input_file = open(input_file, 'rb')
            pdf_merge.append(pdf_input_file)

        # write to merged PDF object
        with open(option_output[0], 'wb') as fileobject:
            pdf_merge.write(fileobject)


if __name__ == '__main__':
    main()