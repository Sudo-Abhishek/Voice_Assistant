
import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes
import isapi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!!")

    else:
        speak("good evening!!")

    speak("welcome to your voice assistant, how may I help you?")

def takeCommand():
    # takes microphone input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say that again...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            print(song)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'H:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open stackoverflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stackoverflow")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Abhishek")
            print("I was built by Abhishek")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)

        elif 'play on youtube' in query:
            song = query.replace('play on youtube', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            print(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())


    # Logic for executing task based on query
