from flask import Flask, render_template, request, send_file
import gtts
import os
import time
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']
    lang = request.form.get('lang', 'en')  # Default to 'en' (English) if no language is selected
    
    if text:
        # Generate a unique filename using current timestamp and random string
        unique_filename = f"output_{int(time.time())}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}.mp3"
        
        # Generate speech from text
        tts = gtts.gTTS(text, lang=lang)  # Use selected language
        tts.save(unique_filename)

        # Send the audio file for download
        return send_file(unique_filename, as_attachment=True)

    return "Error: No text provided!", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Enables network access
