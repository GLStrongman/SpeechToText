import speech_recognition as sr
import pyttsx3 as py

rec = sr.Recognizer()


def SpeakText(command):
    engine = py.init()
    engine.say(command)
    engine.runAndWait()


SpeakText('Hi there')
