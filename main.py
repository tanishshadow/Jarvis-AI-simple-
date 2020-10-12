#  TODO # Need help at line no. 42 and 43
import pyttsx3
import speech_recognition as sr
import datetime
# TODO:Setting voices for speaking of the AI
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    "Greets the user according to the time"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        morn = "Good morning Sir!"
        speak(morn)
        print(morn)
    else:
        after = "Good afternoon Sir!"
        speak(after)
        print(after)


def takeCommand():
    """Recognises the audio and gives the output"""
    re = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        re.pause_threshold = 1
        audio = re.listen(source)
    try:

        query = re.recognize_google(audio, language='en-in')


        # TODO Not printing these two things in the console---("recognising..." and "user's query "".... see below-- )
        # It gets stuck on listening
        print("Recognising....")
        print(f"User's:{query}")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    greet()
    intro = "I am jarvis and i am here to assist you!"
    speak(intro)
    print(intro)
    takeCommand()
