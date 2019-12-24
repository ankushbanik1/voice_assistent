import speech_recognition as sr
import webbrowser
import time
import os
import random
import pyttsx3
from time import ctime

r=sr.Recognizer()

speaker=pyttsx3.init('sapi5')
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)
rate=speaker.getProperty('rate')
speaker.setProperty('rate',173)

def speak(audio_str):
    print('computer:'+audio_str)
    speaker.say(audio_str)
    speaker.runAndWait()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice_data=' '
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry ! i did not get what you said please say it again")    
        except sr.RequestError:
            speak("sorry server down")

        return voice_data    

import wolframalpha 
client = wolframalpha.Client('PTXAVW-7G94KUAYPA') 
def wolfQuestion(data):
    if 'quize' in data:
        question = record_audio('What do you want to Ask ?')
        

        res = client.query(question) 
        answer = next(res.results).text 
        speak("answer is "+answer)
  
# Includes only text from the response 
          
       
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Alexis')
    if 'what is the  time' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        
        speak('What do you want to search for?')
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()
if __name__ == "__main__":
    time.sleep(1)
    speak("How may i help You?")
    speak("Do you want to take a quize ?")

    while 1:
        voice_data=record_audio()
        # respond(voice_data)
        wolfQuestion(voice_data)