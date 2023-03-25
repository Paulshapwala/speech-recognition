import speech_recognition as sr
import gtts 
from playsound import playsound
import os
from datetime import datetime
import json

r = sr.Recognizer()

token = 'secret_xpFJoW4wwdLcodPjQXDoyWqyLSSpXScLbCTKOCc71Qk'
database_id = '06ac178d28d94fe39a6cabbbf26c2c2c'

ACTIVATION_COMMAND = 'hello'
def get_audio():
    with sr.Microphone() as source:
        print('say something')
        audio = r.listen(source)
        return audio

def audio_to_text(audio):
    text = ''
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('speech recognition could not understand the audio')
    except sr.RequestError:
        print('could not request results from API')
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        temp_file = './temp.mp3'
        tts.save(temp_file)
        playsound(temp_file)
        os.remove(temp_file)
    except EssertionError:
        print('could not play sound')
        
if __name__ == '__main__':
    while True:
        a = get_audio()
        command = audio_to_text(a)
        if ACTIVATION_COMMAND in command.lower():
            print('activate')
            play_sound('what can I do for you?')
            
            note = get_audio()
            note = audio_to_text(note)
        from notion_client import Client

        # Authenticate with your integration token
        notion = Client(auth=token)

        # Retrieve a database
        data = notion.databases.query(
            **{
                "database_id": database_id,
            }
        )
        data = json.dumps(data)
        

        if note:
            play_sound(note)
            now = datetime.now().astimezone().isoformat()
            
            
            
        