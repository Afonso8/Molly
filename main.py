import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

new_voice_rate = 145
engine.setProperty("rate", new_voice_rate)

engine.say("Hello Sir, I am Molly, what do you need?")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "hey molly" in command:
                command = command.replace("hey molly", "")
                print(command)
    except:
        pass # TODO speak the error
    return command

def run_molly():
    try:
        command = take_command()
        print(command)
        if "play" in command:
            song = command.replace("play", "")
            talk("playing " + song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is " + time)
            print(time)
        elif "who is" in command:
            object = command.replace("who is", "")
            info = wikipedia.summary(object, 2)
            talk(info)
        elif "joke" in command:
            talk(pyjokes.get_joke())


        else:
            talk("Please say the command again.")
    except:
        pass

while True:
    run_molly()