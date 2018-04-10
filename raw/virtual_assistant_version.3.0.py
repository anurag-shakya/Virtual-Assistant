# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:43:57 2018
virtual_assistant_version.3.py
@author: s.anurag
"""
#importing Libraries
import speech_recognition as sr
import webbrowser 
import os
import csv
from datetime import datetime

# to save every commands in directory "D:/VA/history/"
def save_cmd(audio):
    file_name = "D:/VA/history/" + "microphone record (" + str(1+ (len(next(os.walk("D:/VA/history/"))[2]))) + ").wav"
    with open(file_name,"wb") as f:
        f.write(audio.get_wav_data()) 
        

# to manage a log file in directory "D:/VA/history/log.csv"
def save_log(text):
    t = datetime.now()
    date, time = t.strftime("%d %B %Y %A"), t.strftime("%H:%M:%S")
    with open('D:/VA/history/log.csv', "a", newline='') as log_data:
        write_object = csv.writer(log_data)
        write_object.writerow([date, time, text])
    


showmenu = True
while(showmenu):

    r2 = sr.Recognizer()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        # Adapt to noise 
        r.adjust_for_ambient_noise(source)
        
        # Menu 
        print("\n OPTIONS: \n---------- \n [ URL | Search Web | Search Music | Open/Close Apps]")
        print("\nSay Something!")
        audio = r.listen(source)
        print("wait...")
        save_cmd(audio)
        
        
    try:
        stmnt = r2.recognize_google(audio).upper()
        save_log(stmnt)
        
    except:
        print("inaudible!!! \n Try again")
        continue
        
    if "WEB" in stmnt:
        
        # Obtain audio when word 'web' is heard        
        url = "https://en.wikipedia.org/wiki/"

        with sr.Microphone() as source:
            print("please say a keyword to be searched..")
            audio = r.listen(source)
            print("searching...")
            save_cmd(audio)
            
            
            try :
                get = r2.recognize_google(audio)
                print("You said : " + get)
                save_log(get)
                webbrowser.open_new(url+get)
            
            except sr.UnknownValueError:
                print("\n Sorry! coudn't Understand ")
            except sr.RequestError as e:
                print("\n Failed to retrieve results".format(e))
    
    elif "MUSIC" in stmnt:
        
        # Obtain audio when word 'music' is heard       
        url2 = "https://www.youtube.com/results?search_query="

        with sr.Microphone() as source:
            print("which song you want to play..")
            audio = r.listen(source)
            print("playing...")
            save_cmd(audio)
            
            try :
                text = r2.recognize_google(audio)
                print("You said : " + text)
                save_log(text)
                webbrowser.open_new(url2+text)
            
            except sr.UnknownValueError:
                print("\n Sorry! coudn't Understand ")
            except sr.RequestError as e:
                print("\n Failed to retrieve results".format(e))    
    
    elif "OPEN" in stmnt:
        
        # Obtain audio when word 'open' is heard 
        
        with sr.Microphone() as source:
            print("please name app to be opened..")
            audio = r.listen(source)
            print("got it")
            save_cmd(audio)
            
            try :
                text = r2.recognize_google(audio).upper()                
                print("You said : " + text)
                save_log(text)
                
                
                if "CHROME" in text or "GOOGLE" in text:
                    try:
                        print("opening google chrome...")
                        os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
                    except Exception as e:
                        print(str(e))
                
                elif "CALCULATOR" in text:
                    try:
                        print("opening Calculator...")
                        os.system('start calc.exe')
                    except Exception as e:
                        print(str(e))
                    
                else:
                    print("couldn't find the app \n or Try opening : 'chrome' 'calculator' 'google' ")
                                        
            
            except sr.UnknownValueError:
                print("\n Sorry! coudn't Understand ")
            except sr.RequestError as e:
                print("\n Failed to retrieve results".format(e))    
                
    elif "CLOSE" in stmnt:
        
        # Obtain audio when word 'close' is heard         
        with sr.Microphone() as source:
            print("please name app to be closed..")
            audio = r.listen(source)
            print("got it")
            save_cmd(audio)
            
            try :
                text = r2.recognize_google(audio).upper()
                print("You said : " + text)
                save_log(text)
                
                
                if "CHROME" in text or "GOOGLE" in text:
                    try:
                        print("close google chrome...")
                        os.system('TASKKILL /F /IM chrome.exe')
                    except Exception as e:
                        print(str(e))
                elif "CALCULATOR" in text:
                    try:
                        print("closing Calculator...")
                        os.system('TASKKILL /F /IM calculator.exe')
                    except Exception as e:
                        print(str(e))
                    
                else:
                    print("couldn't find the app \n or Try closing: 'chrome' 'calculator' 'google' ")
           
            except sr.UnknownValueError:
                print("\n Sorry! coudn't Understand ")
            except sr.RequestError as e:
                print("\n Failed to retrieve results".format(e))    
        
        
    # else if search keyword on google search engine
    elif " " in stmnt:      
               
        url3 = "https://www.google.co.in/search?q="            
        try :            
            print("You said : " + stmnt)
            webbrowser.open_new(url3 + stmnt)
            
        except sr.UnknownValueError:
            print("\n Sorry! coudn't Understand ")
        except sr.RequestError as e:
            print("\n Failed to retrieve results".format(e))        
    
    
    # else search URL on web                    
    else :
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        try :                    
            print("You said : " + stmnt)
            webbrowser.get(chrome_path).open(stmnt)        
        except Exception as e:
            print(e)
            
    # asking for more itteration
    ans = input("Want more assistance? (y/n) : ")
    if ans.upper() =='N':        
        showmenu = False      
        
print("\naudio saved succesfully. \nlog created. \nThank you! \nExiting...")
exit = input()
