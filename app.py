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

from flask import send_from_directory

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
@app.route('/logs')
def logs():
    files = os.listdir(UPLOAD_FOLDER)
    files.sort(reverse=True)
    return render_template('logs.html', files=files)

from flask import send_from_directory



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
