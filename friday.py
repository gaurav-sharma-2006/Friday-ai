import cmd
from platform import python_branch
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import speedtest
from whatsapp import sendMessage


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Myself friday! Welcome to the system how can i help you")       

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dragongourav717@gmail.com', 'choy vuoj qxod jshl')
    server.sendmail('dragongourav717@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #searching anything using wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=100)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #open youtube,google,stackoverflow,github using webbrowser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open github' in query:
            webbrowser.open("github.com")


        #shutdown the operating system
        elif 'shutdown the system'in query: 
            os.system("shutdown /s /t 1")

        #play music from operating system
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Gaurav Sharma\\Music\\favourite'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        #telling the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        #sending e-mail
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'dragongourav@gmail.com'    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Gaurav bhai. I am not able to send this email")    
        
        #sending whatsapp message
        elif 'whatsapp' in query:
            sendMessage()
        
        #shutdown friday AI
        elif "friday shutdown" in query:
            speak("bye bye sir!")
            exit()
        
        #open any app
        elif "open" in query:   
                query = query.replace("open","")
                query = query.replace("jarvis","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
        
        #telling the internet speed
        elif "internet speed" in query:
                try:
                    wifi=speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                except Exception as e:
                    print(e)
                    speak("There is some error")

        #click any photo using system camera
        elif "click my photo" in query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")
        
        