Add margin to PDFs
========

Add margins to multiple PDFs all at once.

**Pre requisite**
  - Python 
  - PyPdf2 (pip install pypdf2)

**How to use**
  - Command to run script: 
                 
        python marginPDF --dir_path <path_of_directory_with_pdfs> --margin_w <width_margin_in_pixels> --margin_h <height_margin_in_pixels>

  - Example: 
          
        python marginPDF --margin_w 200
    - This adds 200 pixels to the right of the pdf, since no dir_path is specified the directory is automatically the on where the script is run from (.) and margin_h is 0.

**Use case**
   - Programmed to have right margin in order to take notes on pdfs.

**Todo**

- Make more general, add centering options of content.