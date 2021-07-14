#!C:\Users\HP\AppData\Local\Programs\Python\Python36\python.exe

import pyttsx3



engine = pyttsx3.init()

rate = engine.getProperty("rate")

engine.setProperty("rate", 50)


engine.say("hello")

engine.runAndWait()