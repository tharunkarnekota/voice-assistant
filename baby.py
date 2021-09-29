import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki


listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate                      #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

va_name = 'baby'

def speak(text):
    speaker.say('yes boss, '+ text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

speak_ex('hi boss. i am your'+va_name+'...tell me boss')


def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
                print(command)
              #  speak(command)

    except:
        print('check your mic')

    return command

while True:
    final_command = take_command()
    if 'close' in final_command:
        print('see you again boss. i will be there when ever you want')
        speak('see you again boss. i will be there when ever you want')
        break
    elif 'time' in final_command:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        print(current_time)
        speak(current_time)
    elif 'play' in final_command:
        final_command = final_command.replace('play ','')
        print('playing '+final_command)
        speak('playing '+final_command+ 'enjoy boss')
        pk.playonyt(final_command)
        break
    elif 'search' in final_command or 'google' in final_command:
        final_command = final_command.replace('search ', '')
        final_command = final_command.replace('google ', '')
        speak('searching for'+final_command)
        pk.search(final_command)
        break
    elif 'who is' in final_command or 'what is' in final_command:
        final_command = final_command.replace('who is ', '')
        final_command = final_command.replace('what is ', '')
        info = wiki.summary(final_command,2)
        print(info)
        speak(info)
    elif 'who are you' in final_command:
        speak_ex('i am your' + va_name + '...tell me boss')
    else:
        speak_ex('please say it again boss.')






