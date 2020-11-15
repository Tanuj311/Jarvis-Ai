import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        speak('Please Wait!!')
        print(f'User Said: {query}')

    except Exception:
        print('say that again......')
        return "None"

    return query

def wish():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak('Good Morning!')
    elif hours>=12 and hours<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am jarvis, how can I help you!')

wish()
while True:
    query = recognize().lower()

    if 'on youtube' in query:
        querystr= ''
        query = query.replace('on youtube','')
        query_list = query.split(' ')
        for i in query_list:
            querystr += i+'+'
        webbrowser.open(f'https://www.youtube.com/results?search_query={querystr}')

    elif 'who are you' in query:
        speak('I am Jarvis, I can help solve your problems!')

    elif 'open movies folder' in query:
        os.startfile('F:\\MOVIES')
    
    elif 'open python projects folder' in query:
        os.startfile('F:\\Python Projects')

    elif 'directory' in query:
        query = query.replace('directory','')
        queryl = query.split(' ')
        for i in queryl:
            if len(i) == 1:
                os.startfile(f'{i}:\\')

    elif 'on google' in query:
        googlestr = ''
        query = query.replace('on google','')
        querylist = query.split(' ')
        for i in querylist:
            if googlestr=='':
                googlestr += i
            else:
                googlestr += i+'+'
        webbrowser.open(f'https://www.google.com/search?q={googlestr}')

    elif 'open youtube' in query:
        webbrowser.open('https://www.youtube.com/')

    elif 'open google' in query:
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    elif 'wikipedia' in query:
        query = query.replace('wikipedia','')
        result = wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)

    elif 'open vs code' in query:
        os.startfile('C:\\Users\\tanuj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

    elif 'what is the time' in query:
        time = datetime.datetime.now().strftime('%H:%M:%S')

        timestr = f'the time is {time}'
        speak(timestr)
        print(timestr)

    elif "what is today's date" in query:        
        date = datetime.datetime.now().date()
        date_str = f"today's date is {date}"
        day = datetime.datetime.now().strftime('%A')
        print(date_str, f'and day is {day}')
        speak(f"today's date is {date} and day is {day}")    

    elif '.com' in query:
        query_l = query.split(' ')
        for i in query_l:
            if '.com' in i:
                webbrowser.open(f'http://{i}/')

    elif 'hello' in query:
        speak('HI THERE!')

    else:
        if query != "none":
            speak("i am sorry i cant answer your question")

    print('')


    


    