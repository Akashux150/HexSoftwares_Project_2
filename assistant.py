import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Akash")
    elif hour < 18:
        speak("Good Afternoon Akash")
    else:
        speak("Good Evening Akash")

    speak("I am your voice assistant. How can I help you?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except:
        speak("Sorry, I didn't catch that.")
        return ""

    return command

def run_assistant():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "exit" in command or "stop" in command:
        speak("Goodbye Akash")
        exit()

    else:
        speak("Sorry, I did not understand.")

# Start Assistant
wish_user()

while True:
    run_assistant()
