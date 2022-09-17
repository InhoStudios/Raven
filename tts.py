# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()

array = "Testing"
  
# testing
engine.say(array)
engine.runAndWait()
