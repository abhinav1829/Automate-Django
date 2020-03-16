import datetime
import os
import re
import urllib
import webbrowser
import speech_recognition as sr
import wikipedia
from win32com.client import Dispatch
import pythoncom

tts = Dispatch("SAPI.SpVoice")


def speak(audio):
    pythoncom.CoInitialize()
    tts.Speak(audio)


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good  Morning, Abhinav")
    elif 12 <= hour < 18:
        speak("Good afternoon, Abhinav")
    else:
        speak("Good evening, Abhinav")
    speak("I am automate . How may I help you ?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said : " + query + "\n")
    except Exception as e:
        print(e)
        speak("Say again please...")
        return "None"
    return query


def listen():
    wish_me()
    query = take_command().lower()
    if 'youtube' in query:
        speak('Opening Youtube')
        query = query.replace("youtube", "").strip().replace(" ", "+")
        htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
        results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + results[0])
    elif 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia')
        print(results)
        speak(results)
    elif 'google' in query:
        speak("Searching Google")
        query = query.replace("google", "").strip()
        webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'play movie' in query:
        speak('Playing movie Active Measures .')
        movie_dir = 'G:\Movies\Active Measures'
        movies = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir, movies[0]))
    elif 'bye' in query:
        speak('Goodbye')
        exit()


def main():
    listen()


if __name__ == '__main__':
    main()
