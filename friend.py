import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
import os
import webbrowser
import pyautogui
from pywikihow import RandomHowTo, WikiHow, search_wikihow

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            os.system("mpg123 welcome.mp3")
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello friend' in command:
                command = command.replace('hello friend', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play video' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        mytext = datetime.datetime.now().strftime('%I:%M %p')
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("time.mp3")
        os.system("mpg123 time.mp3")
        print(mytext)
        os.system("rm time.mp3")
    elif 'how to' in command:
        max_results = 1
        mytext = search_wikihow((command), max_results)
        assert len(mytext) == 1
        mytext[0].print()
        language = 'en'
        myobj = gTTS(text=mytext[0], lang=language, slow=False)
        myobj.save("info.mp3")
        os.system("mpg123 info.mp3")
        os.system("rm info.mp3")
    elif 'who is' in command:
        person = command.replace('who is', '')
        mytext = wikipedia.summary(person, 1)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("info.mp3")
        os.system("mpg123 info.mp3")
        print(mytext)
        os.system("rm info.mp3")
    elif 'what is' in command:
        person = command.replace('what is', '')
        mytext = wikipedia.summary(person, 1)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("info.mp3")
        os.system("mpg123 info.mp3")
        print(mytext)
        os.system("rm info.mp3")
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        mytext = (pyjokes.get_joke())
        lagnuage = 'en'
        myobj = gTTS(text=mytext, slow=False)
        myobj.save("joke.mp3")
        os.system("mpg123 joke.mp3")
        print(mytext)
        os.system("rm joke.mp3")
    elif 'open arsenal' in command:
        os.system("mpg123 arsenalquestion1.mp3")
        print ("listening...")
        command = take_command()
        print(command)
        if 'i want you to scan ip address' in command: 
            os.system("mpg123 arsenalquestion2.mp3")
            ans = input("ip address: ")
            ip = ans.split()[0]
            os.system('cd tools && cd Information-Gathering && cd ipgeolocation && python3 ipgeolocation.py -t ' + (ip))
        if 'dork' in command:
            os.system("mpg123 arsenalquestion3.mp3")
            print ("listening...")
            command = take_command()
            webbrowser.open('https://www.' + (command)) 
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
