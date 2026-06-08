# VERSION 3+4

# Voice → Text
import speech_recognition as sr
import webbrowser
# Text → Voice
import pyttsx3
# Opening Windows Apps
import os
# Current Time
from datetime import datetime

# Speech Recognition Object
recognizer = sr.Recognizer()

# Text To Speech Engine
engine = pyttsx3.init()

# Optional: Female Voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Speaking Speed
engine.setProperty("rate", 150)


def speak(message):
    print("Assistant:", message)

    engine.say(message)
    engine.runAndWait()


# Listen From Microphone
with sr.Microphone() as source:

    print("Listening...")

    audio = recognizer.listen(source)

    print("Processing...")

try:
    # Speech To Text
    text = recognizer.recognize_google(audio)

    text = text.lower()

    print("You said:", text)

    # Calculator
    if "calculator" in text:
        speak("Opening Calculator")
        os.system("calc")

    # Notepad
    elif "notepad" in text:
        speak("Opening Notepad")
        os.system("notepad")

    # Time
    elif "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    # VERSION 4
        """ elif text.startswith("open "):

        site = text.replace("open ", "")

        websites = {
            "youtube": "https://youtube.com",
            "github": "https://github.com",
            "google": "https://google.com",
            "chatgpt": "https://chatgpt.com",
            "linkedin": "https://linkedin.com",
            "instagram": "https://instagram.com"
        }

        if site in websites:
            speak(f"Opening {site}")

            webbrowser.open(websites[site])

        else:
            speak("Website not found") """

    # VERSION 5
        """ elif text.startswith("open "):

        site = text.replace("open ", "").strip()

        speak(f"Opening {site}")

        url = f"https://www.{site}.com"

        webbrowser.open(url) """

    # VERSION 6
    
    elif text.startswith("search "):

        query = text.replace("search ", "").strip()

        speak(f"Searching for {query}")

        query = query.replace(" ", "+")

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

    else:
        speak("Command not recognized")

except:
    speak("Sorry, I could not understand")

