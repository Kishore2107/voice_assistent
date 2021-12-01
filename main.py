from twilio.rest import Client
from datetime import date
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import datetime
account_sid = 'AC22197c9a0c0cc1f098f374f16c401578'
auth_token = '40f04cc8ab2b2e446799dbd33c78a423'
client = Client(account_sid, auth_token)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        dir(sr)
        print('listening111...')
        with sr.Microphone() as source:
            print('listening...', source)
            voice = listener.listen(source)
            command = listener.recognize(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print('exception listening...',e)
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'date and time' in command:
        day = datetime.datetime.now().strftime('%c')
        talk('today date is' + day)
    elif 'date' in command:
        day = datetime.datetime.now().strftime('%d%B  %Y %A')
        talk('today date is' + day)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        person = command.replace('about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Go and check your calender')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'thank you' in command:
        talk('its my pleasure')
    elif 'send sms' in command:
        talk('what u want to send')
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command1 = listener.recognize_google(voice)
            command1 = command1.lower()
        talk('Sending sms')
        message = client.messages \
            .create(
            body=command1,
            from_='+16083058009',
            to='+918610144971'
        )
        talk('message send')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

