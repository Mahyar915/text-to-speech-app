from flask import Flask, render_template, request, send_file
import gtts
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']
    if text:
        # Generate speech from text
        tts = gtts.gTTS(text)
        audio_path = "output.mp3"
        tts.save(audio_path)

        # Send the audio file for download
        return send_file(audio_path, as_attachment=True)

    return "Error: No text provided!", 400

if __name__ == '__main__':
    app.run(debug=True)
