import fitz
import os
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import pdfplumber


def convert_pdf_to_html_css(pdf_path, output_folder):
    # Extract text and layout data
    text = extract_text(pdf_path, laparams=LAParams())

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Extract tables
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(table)

    # Save images
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i}.png')
        image.save(image_path, 'PNG')

    # Generate HTML
    html_content = "<html><head><title>PDF to HTML</title><link rel='stylesheet' type='text/css' href='styles.css'></head><body>"
    html_content += f"<p>{text}</p>"

    # Add tables to HTML
    for table in tables:
        html_content += '<table>'
        for row in table:
            html_content += '<tr>'
            for cell in row:
                html_content += f'<td>{cell}</td>'
            html_content += '</tr>'
        html_content += '</table>'

    # Add images
    for i in range(len(images)):
        html_content += f'<img src="images/page_{i}.png" alt="PDF image">'

    html_content += "</body></html>"

    # Save HTML
    with open(os.path.join(output_folder, 'index.html'), 'w') as file:
        file.write(html_content)

    # Generate CSS
    css_content = """
    html, body, div, span, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    abbr, address, cite, code,
    del, dfn, em, img, ins, kbd, q, samp,
    small, strong, sub, sup, var,
    b, i,
    dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend,
    table, caption, tbody, tfoot, thead, tr, th, td,
    article, aside, canvas, details, figcaption, figure, 
    footer, header, hgroup, menu, nav, section, summary,
    time, mark, audio, video {
        margin:0;
        padding:0;
        border:0;
        outline:0;
        font-size:100%;
        vertical-align:baseline;
        background:transparent;
    }

    body {
        line-height:1.6;
        font-family: Arial, sans-serif;
        margin: 20px;
    }

    article,aside,details,figcaption,figure,
    footer,header,hgroup,menu,nav,section { 
        display:block;
    }

    nav ul {
        list-style:none;
    }

    blockquote, q {
        quotes:none;
    }

    blockquote:before, blockquote:after,
    q:before, q:after {
        content:'';
        content:none;
    }

    a {
        margin:0;
        padding:0;
        font-size:100%;
        vertical-align:baseline;
        background:transparent;
    }

    ins {
        background-color:#ff9;
        color:#000;
        text-decoration:none;
    }

    mark {
        background-color:#ff9;
        color:#000; 
        font-style:italic;
        font-weight:bold;
    }

    del {
        text-decoration: line-through;
    }

    abbr[title], dfn[title] {
        border-bottom:1px dotted;
        cursor:help;
    }

    table {
        border-collapse:collapse;
        border-spacing:0;
        width: 100%;
        margin: 20px 0;
    }

    table, th, td {
        border: 1px solid #ddd;
    }

    th, td {
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 20px 0;
    }

    hr {
        display:block;
        height:1px;
        border:0; 
        border-top:1px solid #cccccc;
        margin:1em 0;
        padding:0;
    }

    input, select {
        vertical-align:middle;
    }
    """

    with open(os.path.join(output_folder, 'styles.css'), 'w') as file:
        file.write(css_content)
