import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'img')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/carousel')
def gallery():
    images = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    return render_template('carousel.html', images=images)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return redirect(url_for('gallery'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')