# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:43:57 2018

@author: s.anurag
"""
# Clearing Namespace


#importing Libraries
import speech_recognition as sr
import webbrowser 
import os

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
    
stmnt = r2.recognize_google(audio)    
    
if "web" in stmnt:
    
    # Obtain audio when word 'web' is heard
    
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

elif "music" in stmnt:
    
    # Obtain audio when word 'music' is heard
   
    url2 = "https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("please say a keyword to be searched..")
        audio = r.listen(source)
        print("got it")
        
        try :
            text = r2.recognize_google(audio)
            print("Google thinks you said : \n" + text)
            webbrowser.open_new(url2+text)
        
        except sr.UnknownValueError:
            print("\n Sorry! coudn't Understand ")
        except sr.RequestError as e:
            print("\n Failed to retrieve results".format(e))    

elif "open" in stmnt:
    
    # Obtain audio when word 'open' is heard 
    
    with sr.Microphone() as source:
        print("please name app to be opened...")
        audio = r.listen(source)
        print("got it")
        
        try :
            text = r2.recognize_google(audio)
            print("Google thinks you said : \n" + text)
            
            
            if "chrome" in text or "google" in text:
                try:
                    print("opening google chrome...")
                    os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
                except Exception as e:
                    print(str(e))
            
            elif "caclulator" in text:
                try:
                    print("opening Calculator...")
                    os.system('start calc.exe')
                except Exception as e:
                    print(str(e))
                
            else:
                print("couldn't find the app \n or add app to the search directory ")
                                    
        
        except sr.UnknownValueError:
            print("\n Sorry! coudn't Understand ")
        except sr.RequestError as e:
            print("\n Failed to retrieve results".format(e))    
            
elif "close" in stmnt:
    
    # Obtain audio when word 'close' is heard 
    
    with sr.Microphone() as source:
        print("please name app to be closed...")
        audio = r.listen(source)
        print("got it")
        
        try :
            text = r2.recognize_google(audio)
            print("Google thinks you said : \n" + text)
            
            
            if "chrome" in text or "google" in text:
                try:
                    print("close google chrome...")
                    os.system('TASKKILL /F /IM chrome.exe')
                except Exception as e:
                    print(str(e))
            elif "caclulator" in text:
                try:
                    print("closing Calculator...")
                    os.system('TASKKILL /F /IM calculator.exe')
                except Exception as e:
                    print(str(e))
                
            else:
                print("couldn't find the app \n or add app to the search directory ")
       
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
    
    