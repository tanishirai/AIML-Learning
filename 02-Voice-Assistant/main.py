# VERSION 1 

""" # Loads SpeechRecognition library.
import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:

    print("Listening...")

    # Record audio
    audio = recognizer.listen(source)

    print("Processing...")

try:
    # Convert speech to text
    text = recognizer.recognize_google(audio)

    print("You said:", text)

except:
    print("Sorry, could not understand.") """


# VERSION 2

import speech_recognition as sr
import os           # Used to interact with Windows.
from datetime import datetime       # Used to get current time.

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("Listening...")

    audio = recognizer.listen(source)

    print("Processing...")

try:
    text = recognizer.recognize_google(audio)

    text = text.lower()

    print("You said:", text)

    # Command 1
    if "open calculator" in text:
        print("Opening Calculator...")
        os.system("calc")

    # Command 2
    elif "open notepad" in text:
        print("Opening Notepad...")
        os.system("notepad")

    # Command 3
    elif "what time" in text:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Current Time:", current_time)

    else:
        print("Command not recognized.")

except:
    print("Sorry, could not understand.")