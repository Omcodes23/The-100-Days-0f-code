import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("I am archane , an ai , I was created by master Om vataliya , Please tell  me how may i help you , but sir , before giving any command , be sure that , your connected to internet , and , install all the requir pakages")
    print("commands like: search avatar according to wikipedia\nOpen youtube\nopen stackoverflow\nopen google\nplay music\nopen vs code\netc...")
    speak("you can try by saying any of these commands")
def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #This pause_threshold is used for taking time after speech
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing the task based of query
        if 'wikipedia' in query:
            speak('searching wikipeadia')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir ='G:\\SONG1\\NEW\\New folder'
            songs = os.listdir(music_dir)
            print(songs[0],"is playing now")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'quit' in query:
            speak("exiting the archne ai")
            sys.exit()
            