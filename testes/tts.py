import pyttsx3
engine = pyttsx3.init()



voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

engine.say('Vasco da Gama')
engine.runAndWait()