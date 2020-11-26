import pyttsx3   #Text-to-Speech Conversion library, pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime  #Not need to install but we need to import it for dattime argument
import wikipedia #pip install wikipedia
import webbrowser #For browser opening
import os #For dekstop path access
import smtplib #Package in pyhton for sending mail

engine = pyttsx3.init('sapi5') #sapi5 is Speech Application Programming Interface or SAPI, an API developed by Microsoft to use inbuilt voices in windows
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning......")
        r.pause_threshold = 1 #Manage the gap between input speech, press ctr+entr for more details
        audio = r.listen(source)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) #If you want to print the error message then use it
        print("Say that again please...")
        return "None"    #Returning None as a string
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ayaniemcal@gmail.com', '-------') #for security concern make a text file from which you can access your password. Don't out your password directly here.
    server.sendmail('ayaniemcal@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    #speak("Aditya is a good boy")
    wishMe() #This will first wish you according to time

    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'krishna music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=zCj5EqMFMNo&feature=youtu.be")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        elif 'github desktop' in query:
            githubdekstop = "C:\\Users\\LENOVO\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(githubdekstop)

        #Algorithm for sending mail
        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityarajbu@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my dear Aditya, I am not able to send this email right now.")

        #Algorithm for playing music from files
        '''elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs' #Basically we have to include here our music deirectry file
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))'''
        elif 'quit' in query:
            exit()

