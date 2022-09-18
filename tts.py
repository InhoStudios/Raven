# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()

#input of string from ocr
phrase = "Testing"
  
# testing
engine.say(phrase)
engine.runAndWait()

def speak(string):
    engine.say(string)
    engine.run