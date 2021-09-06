import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    
    else:
        speak("Good Evening")

    speak("Am moogambo,How can i help you")

def takeCommand():
    '''it takes microphone input and gives output'''
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.record(source,duration=3)
    
    try:
        str = r.recognize_google(audio)
        query = str
        print("User:",query)
    
    except Exception as e:
        #print(e)
        print('say again..\n')
        return "None"

    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email_id','password') #the username and password of mail through which mail has to be sent
    server.sendmail('email_id',to,content) #same username or mail_id
    server.close()

if __name__=="__main__":
    wishMe()
    
    while True:  
        query = takeCommand().lower()
        
          #logic for searching
        
        if 'wikipedia' in query:
           speak('searching wikipedia..')     
           query = query.replace('wikipedia',' ')
           result = wikipedia.summary(query,sentences=2)
           print(result)
           speak(result)
        
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'music' in query:
            dr = '.\music'
            song = os.listdir(dr)
            r = random.randint(0,len(song)-1)
            os.startfile(os.path.join(dr,song[r]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(strTime)
        
        elif 'open photoshop' in query:
            photopath = 'C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe' #path of the file
            os.startfile(photopath)
        
        elif 'send mail to' in query:
            try:
                speak('what should i send')
                content = takeCommand()
                to = 'mail_id' #where the mail should be sent
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('cant send e-mails now')
        
        elif 'thank you' in query:
            playsound('.\\soundclip\\laugh.mp3')
            playsound('khush.mp3')
        
        elif 'your name' in query:
            playsound('.\\soundclip\\laugh.mp3')  #plays sounds 
            playsound('.\\soundclip\\name.mp3')
        
        
