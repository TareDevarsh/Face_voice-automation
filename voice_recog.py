import speech_recognition as sr
import os

def voice_recognition_google(name):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        os.system('clear')
        print('---------------------------------\n')
        print('What can i do for you '+ str(name).upper() + '\n')
        print('---------------------------------\n')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language = 'en-IN').lower().split()
            
        except Exception as e:
            text = e
            print("Could Not Detect your voice")

    return text