import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime

from wikipedia import summary

#Intilaize voice engine
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(audio)
        print("You said: ",command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry,I didn't Understand.")
        return ""
    except sr.RequestError:
        print("could not request results.")
        return ""

def run_assistant():
    speak("Hello Raj! How can I help you today?")
    while True:
        command=listen_command()

        if "time" in command:
            time=datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "wikipedia" in command:
            speak("What should i Search on Wikipedia")
            topic=listen_command()
            if topic:
                summary=wikipedia.summary(topic,sentences=2)
                speak(f"According to Wikipedia: {summary}")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        elif command:
            speak("Sorry,I dont know that command yet.")

run_assistant()