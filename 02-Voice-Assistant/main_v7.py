import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from transformers import pipeline

# -------------------------
# Text To Speech
# -------------------------
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# -------------------------
# AI Intent Classifier
# -------------------------
print("Loading AI model...")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "launch a computer program",
    "open a website in browser",
    "search something on google",
    "ask for current time"
]

# -------------------------
# Speech Recognition
# -------------------------
recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:

        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        print("Listening...")

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    print("Processing...")

    command = recognizer.recognize_google(audio)

    print(f"\nYou said: {command}")

    # -------------------------
    # Intent Classification
    # -------------------------
    result = classifier(
        command,
        labels
    )

    print("\nConfidence Scores:")

    for label, score in zip(
        result["labels"],
        result["scores"]
    ):
        print(f"{label}: {score:.3f}")

    intent = result["labels"][0]

    print(f"\nPredicted Intent: {intent}")

    # -------------------------
    # Execute Action
    # -------------------------

    if intent == "ask for current time":

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        speak(f"The time is {current_time}")

    elif intent == "search something on google":

        query = command.lower()

        query = (
            query.replace("search", "")
                 .replace("google", "")
                 .strip()
        )

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        speak("Searching Google")

    elif intent == "open a website in browser":

        if "github" in command.lower():

            webbrowser.open(
                "https://github.com"
            )

            speak("Opening GitHub")

        elif "youtube" in command.lower():

            webbrowser.open(
                "https://youtube.com"
            )

            speak("Opening YouTube")

        else:

            speak("Website not configured")

    elif intent == "launch a computer program":

        if "calculator" in command.lower():

            os.system("calc")

            speak("Opening Calculator")

        elif "notepad" in command.lower():

            os.system("notepad")

            speak("Opening Notepad")

        else:

            speak("Application not configured")

except sr.WaitTimeoutError:
    print("No speech detected.")

except sr.UnknownValueError:
    print("Could not understand audio.")

except sr.RequestError as e:
    print("Speech Recognition API Error:")
    print(e)

except Exception as e:
    print("\nUnexpected Error")
    print("Type:", type(e).__name__)
    print("Message:", repr(e))