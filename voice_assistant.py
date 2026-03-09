import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak")
    r.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        text = r.recognize_google(audio)
        print("You said:", text)

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for speech")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")

    except sr.RequestError:
        print("Could not request results from Google Speech service")

# Text to Speech
engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()
