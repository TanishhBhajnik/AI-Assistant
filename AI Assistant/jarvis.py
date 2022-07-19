import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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
          



def takeCommand():

   #It takes microphone input from user and return string output
   speak("Jarvis at your service sir.")
   
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1 
      audio = r.listen(source)
   

   try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='eng-in')
      print(f"User said: {query}\n")

   except Exception as e:
      #print(e)

      print("Say that again please...")   
      return "None"
   
   return query



if __name__ == "__main__":
     #speak("Hello! Good evening")
     wishMe()

     query = takeCommand().lower()

      #Logic for executing tasks based on query

if 'wikipedia' in query:
   speak('Searching wikipedia...')
   query = query.replace("wikipedia", "")
   results = wikipedia.summary(query, sentences=1)
   speak("According to wikipedia")
   print(results)
   speak(results)
elif 'open youtube' in query:
          webbrowser.open("youtube.com")

