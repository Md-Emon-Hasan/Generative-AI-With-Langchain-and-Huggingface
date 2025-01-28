import os
import streamlit as st
from groq import Groq

# Groq API key (replace with your actual API key)
api_key = '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'

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

def transcribe_audio(file):
    """
    Transcribe the uploaded audio file using the Groq Whisper-large-v3 model.
    :param file: The uploaded audio file
    :return: Transcribed text from the audio file
    """
    # Save the uploaded file temporarily
    temp_filename = "uploaded_audio.mp3"  # Temporarily store the file name
    with open(temp_filename, "wb") as f:
        f.write(file.getbuffer())

    # Create transcription using Groq's API
    with open(temp_filename, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=(temp_filename, audio_file.read()),
            model="whisper-large-v3",  # Use the desired Whisper model version
            response_format="verbose_json",  # Or another format depending on your needs
        )

    # Return the transcribed text
    return transcription.text

def main():
    # Streamlit interface
    st.title("Audio Transcription with Whisper-large-v3")
    st.write("Upload an audio file (MP3, WAV, etc.) and I will transcribe it using Groq's Whisper-large-v3 model.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        # Show audio file to the user
        st.audio(uploaded_file, format="audio/mp3")

        # Display loading indicator while processing the transcription
        with st.spinner("Transcribing... Please wait."):
            try:
                transcription_text = transcribe_audio(uploaded_file)

                # Show the transcription result
                st.subheader("Transcription Result:")
                st.text_area("Transcribed Text", transcription_text, height=300)

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()