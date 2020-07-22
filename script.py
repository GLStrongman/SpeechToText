import speech_recognition as sr
import pyttsx3 as py
from tkinter import Tk
from tkinter.filedialog import askopenfilename

rec = sr.Recognizer()

Tk().withdraw()
filename = askopenfilename()


def SpeakText(command):
    engine = py.init()
    engine.say(command)
    engine.runAndWait()


file = sr.AudioFile(filename)
with file as source:
    audio = rec.record(source)


text = rec.recognize_google(audio)
print(text, end='\n')
SpeakText(text)
