from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import os
from threading import Thread
import time

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/uploads'
PROCESSED_FOLDER = '/tmp/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

progress = {
    'percent': 0,
    'filename': ''
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global progress
    file = request.files['file']
    
    if file and file.filename != '':
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        progress['percent'] = 0  # Reset progress
        progress['filename'] = ''
        
        # Start the processing in a separate thread
        thread = Thread(target=process_csv, args=(filepath,))
        thread.start()

        return jsonify({'message': 'Processing started'})

def process_csv(filepath):
    global progress
    df = pd.read_csv(filepath)
    
    total_rows = len(df)
    processed_filename = "processed_" + os.path.basename(filepath)
    processed_filepath = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)

    for i, row in df.iterrows():
        # Simulate some processing time per row
        time.sleep(0.1)
        
        # Realiza aquí el procesamiento del DataFrame
        # Ejemplo: duplicar la primera columna
        df.at[i, 'duplicated'] = row[df.columns[0]] * 2
        
        # Update progress
        progress['percent'] = int((i + 1) / total_rows * 100)
    
    df.to_csv(processed_filepath, index=False)
    progress['filename'] = processed_filename
    progress['percent'] = 100  # Mark as complete

@app.route('/progress')
def get_progress():
    return jsonify(progress)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['PROCESSED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
