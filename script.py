import speech_recognition as sr
import pyttsx3 as py

rec = sr.Recognizer()


def SpeakText(command):
    engine = py.init()
    engine.say(command)
    engine.runAndWait()


SpeakText('Hi there')

while 1:
    try:
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source, duration=0.2)
            audio = rec.listen(source)
            text = rec.recognize_google(audio)
            text = text.lower()
            SpeakText(text)

    except sr.RequestError as error:
        print("Error: could not request results; {0}".format(error))

    except sr.UnknownValueError:
        print("Error: unknown value occurred")


