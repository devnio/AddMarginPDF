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
    - **--margin_w 200**: add 200 pixels to the right of the pdf 
    - *no dir_path is specified*: the directory is automatically the one where the script is run from (.). Make sure that the pdfs are inside the directory where the script is run.
    - *no margin_h is specified*: no margin for height added.
    - Find the resulting pdfs inside: **dir_path/resized_pdfs**.

**Use case**
   - Programmed to have right margin in order to take notes on pdfs.

**Todo**

- Make more general, add centering options of content.
