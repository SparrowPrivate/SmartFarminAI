import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'jfif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "WrittenBySadiq"


def allowed_file(filename):
    flash('allowed   file')
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'
        if not allowed_file(file.filename):
            return 'File type not allowed'

        if file:
            filename = secure_filename(file.filename)
            file_loc = os.path.join("static/uploads", filename)
            file.save(file_loc)
            print(file_loc)
            result = "This is result"
            return render_template('new.html', file_loc=file_loc, result=result)
            # return '<html><body><img src="'+file_loc+'" height ="240" width ="260"><br><h2>'+result+'</h2></body></html>'

    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)
