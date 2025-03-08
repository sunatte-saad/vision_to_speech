from gtts import gTTS
import os
from io import BytesIO

def text_to_speech_play(text, lang='en', filename='output.mp3'):
    try:
        tts = gTTS(text=text, lang=lang, tld='com.au', slow=False)     
        tts.save(filename)
        print(f"Audio saved as {filename}")       
        os.system(f'start {filename}')
    except Exception as e:
        print(f"Error: {e}")
def text_to_speech(text, lang='en', filename='output.mp3'):
    try:
        tts = gTTS(text=text, lang=lang, tld='com.au', slow=False)      
        tts.save(filename)
        print(f"Audio saved as {filename}")      
        return filename
    except Exception as e:
        print(f"Error: {e}")
        return None

def play_directly(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.write_to_fp(BytesIO())
    except Exception as e:
        print(f"Error: {e}")
