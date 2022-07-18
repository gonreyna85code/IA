from asyncio.windows_events import NULL
from cgitb import text
from typing_extensions import Self
import numpy as np
import datetime
import pyttsx3
from decouple import config
import speech_recognition as sr
from gtts import gTTS
import os 
import transformers
nlp = transformers.pipeline("conversational",
model="microsoft/DialoGPT-small")


USERNAME = config('USER')
BOTNAME = config('BOTNAME')
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
            try:
                print("recognizing...")                
                self.text = recognizer.recognize_google(audio, language='es-EU') 
                print("me --> ", self.text )
            except:
                NULL
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    def speak(self, text):    
        engine.say(text)
        engine.runAndWait()    
    def text_to_speech(self, text):
        print("bot --> ", text)
        speaker = gTTS(text=text, lang="es", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3") #macbook->afplay | windows->start
        ##os.remove("res.mp3")      
    def action_time(self):
        return datetime.datetime.now().time().strftime('%H:%M')    



# Run the AI
if __name__ == "__main__":
    ai = ChatBot(name="robot")                     
    while True:
      ai.speech_to_text()
      chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)     
      res = str(chat)
      res = res[res.find("bot >> ")+6:].strip()        
      ai.speak(res)
      
        

