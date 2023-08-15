from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'floorplan' not in request.files:
        return 'No file part'
    file = request.files['floorplan']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        # Call your floorplan processing function here
        # For example: process_floorplan(filename)
        return 'File uploaded and processed'

if __name__ == '__main__':
    app.run(debug=True)
