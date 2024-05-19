from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/uploads')
def index():
    return render_template('uploads.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image_names = os.listdir('./static/uploads')
    return render_template('dashboard.html', image_names=image_names)

if __name__ == '__main__':
    app.run(debug=True)