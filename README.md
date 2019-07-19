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
          
        python marginPDF --dir_path "./example" --margin_w 500
    - **--margin_w 500**: add 500 pixels to the right of the pdf 
    - **dir_path**: script runs in the "./example" directory. 
      - *if no dir_path is omitted* then the directory is automatically the one where the script is run from (.). Make sure that the pdfs are inside the directory where the script is run.
    - *no margin_h is specified*: no margin for height added.
    - Find the resulting pdfs inside: **dir_path/resized_pdfs**.
  
Initial PDF:
![Initial Pdf](example/result_example/imgs_example.jpg)

Resized PDF:
![Initial Pdf](example/result_example/imgs_example_resized.jpg)

**Use case**
   - Programmed to have right margin in order to take notes on pdfs.

**Todo**

- Make more general, add centering options of content.
