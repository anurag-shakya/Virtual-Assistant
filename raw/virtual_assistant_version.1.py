# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:43:57 2018

@author: s.anurag
"""
# Clearing Namespace %reset -f

#importing Libraries
import speech_recognition as sr
import webbrowser 

r3 = sr.Recognizer()
r2 = sr.Recognizer()
r = sr.Recognizer()

with sr.Microphone() as source:
    
    # Adapt to noise 
    r.adjust_for_ambient_noise(source)
    print("\n OPTIONS: \n---------- \n [ Open URL | Search Web | Search Music]")
    print("\nSay Something!")
    audio = r.listen(source)
    print("done")
    
    
if "web" in r2.recognize_google(audio):
    
    # Obtain audio when word 'web' is heard
    r2 = sr.Recognizer()
    url = "https://en.wikipedia.org/wiki/"
    with sr.Microphone() as source:
        print("please say a keyword to be searched..")
        audio = r.listen(source)
        print("got it")
        
        try :
            get = r2.recognize_google(audio)
            print("Google thinks you said : \n" + get)
            webbrowser.open_new(url+get)
        
        except sr.UnknownValueError:
            print("\n Sorry! coudn't Understand ")
        except sr.RequestError as e:
            print("\n Failed to retrieve results".format(e))

elif "music" in r3.recognize_google(audio):
    
    # Obtain audio when word 'music' is heard
    r3 = sr.Recognizer()
    url2 = "https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("please say a keyword to be searched..")
        audio = r.listen(source)
        print("got it")
        
        try :
            text = r3.recognize_google(audio)
            print("Google thinks you said : \n" + text)
            webbrowser.open_new(url2+text)
        
        except sr.UnknownValueError:
            print("\n Sorry! coudn't Understand ")
        except sr.RequestError as e:
            print("\n Failed to retrieve results".format(e))    
            
else :
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    try :        
        text = r.recognize_google(audio)
        print("Google thinks you said : \n" + text)
        webbrowser.get(chrome_path).open(text)        
    except Exception as e:
        print(e)
    
    