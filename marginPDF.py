from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

import argparse
import os

parser = argparse.ArgumentParser(description='PDF margin size and paths.')
parser.add_argument('--dir_path', type=str, default = ".", help='Path of directory with pdf to resize.')
parser.add_argument('--margin_w', type=int, default = 0,  help='Width margin of new pdf.')
parser.add_argument('--margin_h', type=int, default = 0, help='Height margin of new pdf.')
args = parser.parse_args()

# Resize path
outputh_path = "./resized_pdfs"
os.makedirs(outputh_path, exist_ok=True)


def resize_pdf(filename):
    path_file = args.dir_path + "/" + filename
    print("Open pdf file: ", path_file)
    reader = PdfFileReader(open(path_file,'rb'))
    number_of_pages = reader.getNumPages()
    # Take first page (used for the size)
    first_page = reader.getPage(0)
    
    writer = PdfFileWriter()
    for i in range (0, number_of_pages):
        # Create white page with margins and merge with other files
        blank_page = PageObject.createBlankPage(None, first_page.mediaBox.getWidth() + args.margin_w, first_page.mediaBox.getHeight() + args.margin_h)
        blank_page.mergeScaledTranslatedPage(reader.getPage(i), 1, 0, 0) # page, scale, offset_x, offset_y
        writer.addPage(blank_page)
    
    output_file = outputh_path + "/resized_" + filename
    print("Save resized pdf in: ", output_file)
    with open(output_file, 'wb') as f:
        writer.write(f)


if __name__ == "__main__":    
    print("Resizing pdfs in directory: " + args.dir_path)
    for filename in os.listdir(args.dir_path):
        if filename.endswith(".pdf") : 
            print("Resizing: ", filename)
            resize_pdf(filename)

