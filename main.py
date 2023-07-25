import speech_recognition as sr
from AppOpener import open
from AppOpener import close
import win32com.client
import webbrowser as wb
# import openai as oa
import datetime

#def chat(query):

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.8  we can remove this kyunki 0.8 bydefault hai
        audio = r.listen(source)
        try:
            print("Recognizing Sir....")
            query1 = r.recognize_google(audio, language="en-in")
            print(f"User said: {query1}")
            return query1
        except Exception as e:
            return print("Sorry", e)


while 1:
    # print("Enter the word you want to speak")
    speaker.Speak("Hello Sir I am Zero")
    while True:
        print("Listening Monsieur.....")
        query = takecommand()
        # speaker.Speak(query)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"],
                 ["google", "https://www.google.com"], ["special", "https://www.xnxx.press/search/xnxx/1"],
                 ["toy story", "https://thetoystories.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir...")
                wb.open(site[1])
                

        if "the time" in query:
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir the time is {strftime}")

        apps = [["Whatsapp"], ["Discord"], ["Spotify"], ["Google Chrome"], ["Visual Studio Code"], ["Camera"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {app[0]} Sir...")
                open(app[0])
            if f"Close {app[0]}".lower() in query.lower():
                speaker.Speak(f"Closing {app[0]} Sir...")
                close(app[0])

        if "Jarvis Quit".lower() in query.lower():
            exit()

        if "reset chat".lower() in query.lower():
            chatStr = ""
