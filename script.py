import speech_recognition as sr
import pyttsx3 as py
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ffmpeg

#  Initialize SpeechRecognition
rec = sr.Recognizer()

#  Opens Tkinter dialogue box to choose file
Tk().withdraw()
filename = askopenfilename()
path = os.path.dirname(filename)
print(filename, "  path:  ", path)
textfname = filename + '.txt'

#  Convert chosen file to .wav
stream = ffmpeg.input(filename)
stream = ffmpeg.output(stream, 'tmp/output.wav')
ffmpeg.run(stream)


#  Method to read string of text out loud
def SpeakText(command):
    engine = py.init()
    engine.say(command)
    engine.runAndWait()


#  Records audio from the given file
file = sr.AudioFile('tmp/output.wav')
with file as source:
    audio = rec.record(source)


#  Converts the audio to text using Google
text = rec.recognize_google(audio)
print(text, end='\n')
SpeakText(text)

#  Writes the text to a file in the same place as the original audio
file = open(textfname, "w+")
file.write(text)
file.close()

os.remove('tmp/output.wav')
