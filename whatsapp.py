import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source,phrase_time_limit=3)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
strTime=int(datetime.now().strftime("%H"))
update=int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    print('''1.Divyanshu 2.Divyansh 3.Ashutosh Bansal 4.Hardik Verma''')
    a=takeCommand()
    if a=='Divyanshu':
          try:
               speak("Whats the message...")
               message=takeCommand().lower()
               pywhatkit.sendwhatmsg("+917906780665",message,time_hour=strTime,time_min=update)
               whatsapp = open("whatsapp.txt", "w+") 
               file=whatsapp.write(message)
               file.close()
          except Exception as e:
               print(e)
               speak("Message is not able send")
        
    elif a=='Divyansh':
          try:
               speak("Whats the message...")
               message=takeCommand().lower()
               pywhatkit.sendwhatmsg("+919368066344",message,time_hour=strTime,time_min=update)
               whatsapp = open("whatsapp.txt", "w+") 
               file=whatsapp.write(message)
               file.close()
          except Exception as e:
               print(e)
               speak("Message is not able send")
    elif a=='Ashutosh Bansal':
        try:
            speak("Whats the message...")
            message=takeCommand().lower()
            pywhatkit.sendwhatmsg("+918279610810",message,time_hour=strTime,time_min=update)
            whatsapp = open("whatsapp.txt", "w+") 
            file=pywhatkit.text_to_handwriting(message)
            file.close()
        except Exception as e:
            print(e)
            speak("Message is not able send")
    elif a=='Hardik Verma':
        try:
            speak("Whats the message...")
            message=takeCommand().lower()
            pywhatkit.sendwhatmsg("+918958477149",message,time_hour=strTime,time_min=update)
            whatsapp = open("whatsapp.txt", "w+") 
            file=whatsapp.write(message)
            file.close()
        except Exception as e:
            print(e)
            speak("Message is not able send")
    else:
        speak(f"{a} not int list") 
