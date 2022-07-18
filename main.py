from online_ops import find_my_ip, play_on_youtube, search_on_google, search_on_wikipedia, send_whatsapp_message
from os_ops import open_calculator, open_visualstudio, open_cmd
from datetime import datetime
from gtts import gTTS
from decouple import config
import speech_recognition as sr
from random import choice
from utils import opening_text
import os

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='es-US')
        print(f'User said: {query}\n')
        if not 'desactivar' in query or 'terminar' in query:
            if BOTNAME in query or "la mía" in query:
                speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("buenas noches!")
            else:
                speak('buen dia!')
            exit()
    except Exception:
        print("Error")
        query = 'None'
    return query


def greet_user():
    hour = datetime.now().hour
    print(hour)
    if (hour >= 6) and (hour < 12):
        speak(f"Buen dia {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"buenas tardes {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"buenas noches {USERNAME}")
    elif (hour >= 19) and (hour < 21):
        speak(f"buenas noches {USERNAME}")
    speak(f"soy {BOTNAME}. en que puedo ayudar?")


def speak(text):
    tts = gTTS(text=text, lang="es", slow=False)
    # auto play not saved in a file
    tts.save("res.mp3")
    os.system("start res.mp3")


a, b = 'áéíóúüñÁÉÍÓÚÜÑ', 'aeiouunAEIOUUN'
trans = str.maketrans(a, b)


if __name__ == '__main__':
    greet_user()
    while True:
        # query lower case and remove punctuation
        query = take_user_input().lower()
        # activate only on key name
        if BOTNAME in query or "la mía" in query:
            if 'desactivar' in query or 'terminar' in query:
                speak(choice(opening_text))
                exit()
            if 'visual studio' in query.translate(trans):
                open_visualstudio()
            elif 'terminal' in query.translate(trans):
                open_cmd()
            elif 'calculadora' in query.translate(trans):
                open_calculator()
            elif 'direccion ip' in query.translate(trans):
                ip_address = find_my_ip()
                speak(
                    f'Tu direccion ip es {ip_address}.\n imprimiendo en consola, por favor espere...')
                print(f'Tu direccion ip es {ip_address}')
            elif 'wikipedia' in query.translate(trans):
                speak('que quieres buscar en Wikipedia?')
                search_query = take_user_input().lower()
                results = search_on_wikipedia(search_query)
                speak(f"Segun Wikipedia, {results}")
                speak("imprimiendo en consola, por favor espere...")
                print(results)
            elif 'youtube' in query.translate(trans):
                speak('que quieres reproducir?')
                video = take_user_input().lower()
                play_on_youtube(video)
            elif 'google' in query.translate(trans):
                speak('que quieres buscar?')
                query = take_user_input().lower()
                search_on_google(query)
            elif "whatsapp" in query.translate(trans):
                speak('por favor ingrese el número en la consola: ')
                number = input("Ingrese el número: ")
                speak("cual es el mensaje?")
                message = take_user_input().lower()
                send_whatsapp_message(number, message)
                speak("Mensaje enviado con éxito")
            