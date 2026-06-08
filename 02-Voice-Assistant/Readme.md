# Voice Assistant (Mini Siri)

A beginner-friendly AI/ML project that converts speech into text, understands user commands, performs actions, and responds using voice.

This project was built step-by-step to learn the fundamentals of Speech Recognition, Text-to-Speech, NLP, Automation, and AI Intent Classification.

---

## Project Overview

The Voice Assistant listens to a user's voice command, converts it into text, understands the intent, performs an action, and optionally responds back using speech.

Example:

User:
"Open Calculator"

Assistant:
"Opening Calculator"

Calculator launches automatically.

---

## Features Built

### Version 1 - Speech Recognition

Convert voice into text using Speech-to-Text.

Example:

Listening...
Processing...
You said: hello voice assistant

### Version 2 - Rule-Based Commands

Added simple command execution:

- Open Calculator
- Open Notepad
- Tell Current Time

### Version 3 - Text To Speech (TTS)

Assistant can now speak responses.

Example:

The time is 03:12 PM

### Version 4 - Open Websites

Assistant can launch websites such as:

- GitHub
- YouTube

### Version 5 - Google Search

Example:

Search Python tutorial

Automatically opens:

https://www.google.com/search?q=python+tutorial

### Version 6 - Complete Rule-Based Assistant

Combined:

- Speech Recognition
- Text To Speech
- Application Launching
- Website Opening
- Google Searching
- Time Queries

### Version 7 - AI Intent Classification

Added Natural Language Processing using:

facebook/bart-large-mnli

The assistant predicts the user's intent using Zero-Shot Classification.

Example:

Command:
"what time is it"

Predicted Intent:
tell current time

This version was created mainly for learning NLP concepts.

---

## Tech Stack

### Python

Main programming language

### SpeechRecognition

Converts speech into text

### PyAudio

Accesses microphone input

### pyttsx3

Converts text into speech

### Transformers

Provides NLP models

### BART Large MNLI

Used for Zero-Shot Intent Classification

### Webbrowser

Opens websites automatically

### OS Module

Launches system applications

---

## Project Structure
```
02-VOICE-ASSISTANT/
│
├── main.py
├── main_v7.py
├── AI-Powered-Assistant.py
├── intent_test.py
├── tts_test.py
├── README.md
└── .gitignore
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install transformers
pip install torch
```

---

## Run Project

### Basic Assistant

```bash
python main.py
```

### AI Intent Assistant

```bash
python main_v7.py
```

---

## Challenges Faced

### Microphone Detection Issues

- Learned how microphone devices are accessed through PyAudio.
- Understood how SpeechRecognition captures audio input.

### Speech Recognition Errors

- Background noise sometimes caused incorrect command recognition.
- Learned the importance of noise adjustment and testing.

### Text-To-Speech Problems

- Faced issues where only part of the response was spoken.
- Learned how pyttsx3 manages speech queues.

### Hugging Face Storage Issues

- Large NLP models required significant disk space.
- Learned how model caching works.
- Configured Hugging Face storage on a different drive.

### Intent Classification Errors

Example:

Command:
"Open GitHub"

Predicted:
"Open Application"

Instead of:
"Open Website"

This demonstrated that AI models can make mistakes even with high confidence scores.

---

## Skills & Concepts Learned

### Artificial Intelligence

- Speech Recognition
- Speech-To-Text (STT)
- Text-To-Speech (TTS)
- Natural Language Processing (NLP)
- Intent Classification
- Zero-Shot Learning
- Confidence Score Analysis
- Model Evaluation
- AI Decision Making

### Machine Learning

- Using Pretrained Models
- Hugging Face Transformers
- BART Large MNLI Model
- Model Inference
- Classification Pipelines
- Prompt-Based Intent Detection
- Understanding Model Predictions
- Comparing AI vs Rule-Based Systems

### Software Development

- Python Automation
- Browser Automation
- System Application Automation
- Voice-Based User Interfaces
- Exception Handling
- Modular Code Design
- Working with External Libraries
- Environment & Dependency Management

---

## Libraries & Tools Explored

### SpeechRecognition

Learned:

- Capturing microphone input
- Converting speech into text
- Handling recognition errors
- Noise sensitivity issues

### PyAudio

Learned:

- Microphone access
- Audio stream handling
- Device communication

### pyttsx3

Learned:

- Offline text-to-speech
- Voice engine configuration
- Speaking dynamic responses

### Transformers

Learned:

- Loading pretrained NLP models
- Running inference locally
- Zero-shot classification workflows

### Hugging Face Hub

Learned:

- Downloading pretrained models
- Model caching
- Storage management
- Working with large AI models

---

## Real-World Engineering Lessons

- AI models are not always better than simple logic.
- Data and prompts heavily affect predictions.
- Model confidence does not guarantee correctness.
- Large models require significant storage resources.
- Testing edge cases is essential.
- Rule-based systems can outperform AI for small tasks.
- Good user experience is as important as model accuracy.

---

## Problem Solving Experience

During this project I learned how to:

- Debug microphone issues
- Fix text-to-speech problems
- Manage virtual environments
- Handle package installation errors
- Configure Hugging Face model storage
- Resolve disk space limitations
- Analyze incorrect AI predictions
- Compare multiple implementation approaches

---

## Final Outcome

Built a fully functional voice assistant capable of:

- Listening to voice commands
- Understanding user requests
- Speaking responses
- Opening applications
- Launching websites
- Searching Google
- Telling the current time
- Experimenting with AI-based intent classification

### Complete Pipeline

```text
Voice Input
      ↓
Speech Recognition
      ↓
Text Conversion
      ↓
Intent Detection
      ↓
Action Execution
      ↓
Voice Response
```

---

## Future Improvements

- Continuous Listening Mode
- Wake Word Detection ("Hey Assistant")
- Open Any Installed Application
- Weather Information
- Wikipedia Search
- Smart File Management
- ChatGPT Integration
- GUI Interface using Tkinter or Streamlit
- Local LLM Integration
- Task Scheduling & Automation

---

## Key Takeaway

> More AI does not always mean better results.

For a small set of commands, a simple rule-based system can often outperform a large AI model.

This project helped compare traditional programming approaches with modern AI-powered NLP systems and understand where each approach works best.

---

## Author

**Tanishi Rai**
