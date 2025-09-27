from flask import Flask, request, render_template, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_link', methods=['POST'])
def create_link():
    # Random unique link (timestamp based)
    token = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    return f"Your share link: <a href='/share/{token}'>https://your-app.onrender.com/share/{token}</a>"

@app.route('/share/<token>')
def share(token):
    return render_template('share_consent.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return 'No file', 400
    f = request.files['photo']
    timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    filename = f'{timestamp}_{f.filename}'
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)
    return 'OK', 200

@app.route('/logs')
def logs():
    files = os.listdir(UPLOAD_FOLDER)
    files.sort(reverse=True)
    return render_template('logs.html', files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
