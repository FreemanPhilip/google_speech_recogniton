import speech_recognition as speech 
from time import ctime
import webbrowser
import playsound
from gtts import  gTTS
import os
import time
import random

# this line of code enblae us to initialise our speech app
recg =speech.Recognizer()
def voice_recognition(ask=False):
    with speech.Microphone() as source:
        if ask:
           fap_speak (ask)
        audio = recg.listen(source)
        voice_output = ""
        try:
            voice_output=recg.recognize_google(audio)
            fap_speak(voice_output)
        except speech.UnknownValueError :
             fap_speak ("sorry what said is not clear")
        except speech.RequestError:
            fap_speak ("sorry our network is down")
        return voice_output
    
    # this line of code enable the google to speek back to us
def fap_speak(audio_string):
    tts= gTTS(text=audio_string, lang="en")
    randomfile=random.randint(1, 1000000)
    freespeek = "audio" + str(randomfile) +".mp3"
    tts.save(freespeek)
    playsound.playsound(freespeek) 
    print(audio_string)
    os.remove(freespeek)
    
    
# this line of code enables google to respond to ur search per  ur search
def respond():
    if "what is my name" in voice_output:
         fap_speak("you name is freeman")
    elif "where am  i from " in voice_output:
         fap_speak("you are from gahana in greater accra")
    else:
         fap_speak("talk again")

    if "what is the time" in voice_output:
          fap_speak("the time is " + ctime())
    
    if "search" in voice_output:
        search=voice_recognition("what are u searching for?")
        url= "https://www.google.com/search?q=" +search
        webbrowser.get().open(url)
        fap_speak ("here is what i  have found" + search)
    if "find location" in voice_output:
        location =voice_recognition("what is the location?")
        url= "https://www.google.np/maps/place/" + location + "/&amp"
        webbrowser.get().open(url)
        fap_speak ("here is the location of " + location)
    if "exit" in voice_output:
        exit()
        
    
       


time.sleep(1)
fap_speak ("how may i help you?")
while 1:
    voice_output=voice_recognition()
    respond(voice_output)



        
        
