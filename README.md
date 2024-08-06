# Html/CSS generator from PDF

Web application that allows users to upload PDF files, convert them to HTML/CSS, and then provide a downloadable ZIP file containing the HTML and CSS files.

## Installation

1. Clone the repository using 
  ```bash
  git clone https://github.com/bugemarvin/html_css_generator_from_pdf.git
  ```
  and navigate to the project directory
  ```bash
  cd html_css_generator_from_pdf
  ```
  create a virtual environment using
  ```bash
  python3 -m venv venv
  ```
  and activate it using
  ```bash
  source venv/bin/activate
  ```
2. Install the required packages using 
  ```bash
  pip install -r requirements.txt
  ```
3. Run the application using 
  ```bash
  python app.py
  ```
  `or`
  ```bash
    flask run
  ```
  (if you have Flask installed)
4. Navigate to 
  ```bash
    http://localhost:5000`
  ```
  in your browser to use the application

## Usage

1. Upload a PDF file using the file input
2. Click the "Upload" button
3. Wait for the conversion to complete
4. Check the downloads folder for the ZIP file containing the HTML and CSS files generated from the PDF

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

1. [MIT License](https://opensource.org/licenses/MIT)
2. fork the repository
3. create a new branch (`git checkout -b improve-feature`)
4. make the appropriate changes in the files and add comments where necessary (`git add <filename>` or `git add .`)
5. commit changes (`git commit -m 'Improve feature'`)
6. push changes to the branch (`git push origin improve-feature`)
7. create a Pull Request

##  Contact

if you have any questions, feel free to contact me at bugemarvin@outlook.com

Save this as  `README.md` in the root directory of your project. This file will be used to display the project description on the repository page.
