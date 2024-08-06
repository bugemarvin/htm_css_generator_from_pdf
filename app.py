from flask import Flask, request, redirect, url_for, render_template, send_file
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename
import zipfile
from convertor import convert_pdf_to_html_css

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
Bootstrap(app)

# Ensure the uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Convert PDF to HTML/CSS
            output_folder = os.path.join('output', filename.rsplit('.', 1)[0])
            os.makedirs(output_folder, exist_ok=True)
            convert_pdf_to_html_css(filepath, output_folder)
            
            # Create ZIP file
            zip_path = os.path.join('output', f'{filename.rsplit(".", 1)[0]}.zip')
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for root, dirs, files in os.walk(output_folder):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_folder))

            return send_file(zip_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
