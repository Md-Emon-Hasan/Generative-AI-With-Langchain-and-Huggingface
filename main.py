import os
from groq import Groq

# Replace with your actual API key
api_key = 'your-api-key'

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Assuming the audio file is in the same directory as the script
audio_filename = "Recording.mp3"  # Replace with your actual file name
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, audio_filename)

with open(file_path, "rb") as file:
    # Create transcription using Groq's API
    transcription = client.audio.transcriptions.create(
        file=(audio_filename, file.read()),
        model="whisper-large-v3",  # Use the desired Whisper model version
        response_format="verbose_json",  # Or another format depending on your needs
    )

    # Print the transcribed text
    print(transcription.text)
