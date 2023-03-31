import pipwin as pipwin
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
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

    speak("I am Voice Assistant Companion Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=8, phrase_time_limit=8)

    try:
        print("Hold on for a moment...")
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
    server.login('20CS076@charusat.edu.in', 'akshatshah2808@@')
    server.sendmail('20CS076@charusat.edu.in', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Do you want to open youtube ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("youtube.com")
            else:
                speak("Please say that again")


        elif 'open google' in query:
            speak("Do you want to open google ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("google.com")
            else:
                speak("Please say that again")


        elif 'open stackoverflow' in query:
            speak("Do you want to open stackoverflow ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("stackoverflow.com")
            else:
                speak("Please say that again")


        elif 'open github' in query:
            speak("Do you want to open github ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("github.com")
            else:
                speak("Please say that again")


        elif 'open hotstar' in query:
            speak("Do you want to open hotstar ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("hotstar.com")
            else:
                speak("Please say that again")


        elif 'open sonyliv' in query:
            speak("Do you want to open SonyLiv ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                webbrowser.open("sonyliv.com")
            else:
                speak("Please say that again")


        elif 'open vs code' in query:
            speak("Do you want to open vs code ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                codePath = "C:\\Users\\Akshat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
                os.startfile(codePath)
            else:
                speak("Please say that again")


        elif 'play music' in query:
            music_dir = 'C:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'shut down pc' in query:
            speak("Do you want to shut down pc ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                os.system("shutdown /s /t 1")
            else:
                speak("Please say that again")


        elif 'restart pc' in query:
            speak("Do you want to restart pc ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                os.system("shutdown /r /t 1")
            else:
                speak("Please say that again")


        elif 'email to Akshat' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "20CS076@charusat.edu.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Akshat bhai. I am not able to send this email")

        elif 'exit' in query:
            speak("Do you wish to exit VAC ? (yes / no)")
            content1 = takeCommand()

            if 'yes' in content1:
                exit()
            else:
                speak("Please say that again")
