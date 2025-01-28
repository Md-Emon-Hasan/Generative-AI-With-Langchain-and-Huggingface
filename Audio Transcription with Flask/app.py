'''
   Author  : Emon Hasan
   Email   : iconicemon01@gmail.com
   GitHub  : https://github.com/Md-Emon-Hasan
   LinkedIn: https://www.linkedin.com/in/emon-hasan/
   Date    : 01/28/2025
   Time    : 17:43
   Project : Audio Transcription Web App with Flask and Groq API 
   Purpose : Audio Transcription Web App with Flask and Groq API with Python and whisper-large-v3(open-ai) model .
'''

# Import required libraries
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from groq import Groq

# Replace with your actual API key
api_key = 'your_api_key'

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

app = Flask(__name__)

# Route for homepage (file upload)
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling file upload and transcription
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['audio_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded file temporarily
    temp_filename = "uploaded_audio.mp3"  # Temporarily store the file name
    file.save(temp_filename)

    try:
        # Transcribe the audio using Groq's API
        with open(temp_filename, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=(temp_filename, audio_file.read()),
                model="whisper-large-v3",
                response_format="verbose_json"
            )

        # Return the transcribed text
        return jsonify({'transcription': transcription.text})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)