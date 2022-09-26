import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime
import wikipedia
import requests
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try :

        with sr.Microphone() as source:
            command = []
            print("listening.....")
            playsound("C:\\Users\\Arafath\\OneDrive\\Desktop\\Python\\before_sound.wav")
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            playsound("C:\\Users\\Arafath\\OneDrive\\Desktop\\Python\\middle_sound.wav")
            command = command.lower()
    except:
        pass

    return command

def run_command():
    while True:
        command = take_command() 
        if 'paint' in command:
            talk('yes sir')
            print('Processing...')
            command = command.replace(command, '')
        elif 'how are you' in command:
            talk('i am fine sir, what about you ?')
            command = command.replace(command, '')
        elif 'weather' in command:
            sunny = """
                \   /
                 .-.    
             ― (   ) ―
                 `-’
                /   \  
            """
            partly_cloudy = """
                \  /         
              _ /"".-.          
                \_(   ).      
                /(___(__)
            """
            null = """
                  _`/"".-.     
                   ,\_(   ).  
                  /(___(__)  
                   ‘ ‘ ‘ ‘  
                   ‘ ‘ ‘ ‘
            """
            url = "https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=fd8b026bb69f10bdcfbd76150dbb9dad"
            url1 = requests.get(url)
            url1_data = url1.json()
            temp = ((url1_data['main']['temp'] - 273))
            temp_format = format(temp, ".2f")
            description = ((url1_data['weather'][0]['description']))
            city = ((url1_data['name']))
            humidity = ((url1_data['main']['humidity']))
            wind_speed = str((url1_data['wind']['speed']))
            talk("today's weather report in " + city + ' is')
            print("-------------------------------")
            print("Weather report in " + city )
            print("-------------------------------")
            convertor = str(humidity)
            if humidity >= 65:
                print(null)
            elif humidity >= 50:
                print(partly_cloudy)
            elif humidity <= 50:
                print(sunny)
            date = datetime.datetime.now().date()
            var = str(date)
            cho = var[5:7]
            if cho == "01":
                pick = "Jan"
            if cho == "02":
                pick = "Feb"
            if cho == "03":
                pick = "Mar"
            if cho == "04":
                pick = "Apr"
            if cho == "05":
                pick = "May"
            if cho == "06":
                pick = "Jun"
            if cho == "07":
                pick = "Jul"
            if cho == "08":
                pick = "Aug"
            if cho == "09":
                pick = "Sep"
            if cho == "10":
                pick = "Oct"
            if cho == "11":
                pick = "Nov"
            if cho == "12":
                pick = "Dec"
            print("                    ┌─────────────┐")
            print("┌───────────────────┤ " + var[8:10], pick, var[0:4] + " ├───────────────────────┐")
            print("│                   └─────────────┘                       │")
            print("│  Today's temperature is        : " + temp_format +  "                  │")
            print("├─────────────────────────────────────────────────────────┤")
            print("│  Wind speed                    : " + wind_speed +   "                   │")
            print("├─────────────────────────────────────────────────────────┤")
            print("│  Possibilities for raining is  : " + convertor + " %                   │")
            print("├─────────────────────────────────────────────────────────┤")
            print("│  You will be having " + description + " on the sky                      │")
            print("└─────────────────────────────────────────────────────────┘\n")
            talk("Today's temperature is " + temp_format)
            talk("Now the wind speed in you area is " + wind_speed)
            talk("Possibilities for raining is " + convertor + "percentage")
            talk("You will be having " + description + " on the sky")
            command = command.replace(command, '')

        elif 'where am i' in command:
            url = "https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=fd8b026bb69f10bdcfbd76150dbb9dad"
            url1 = requests.get(url)
            url1_data = url1.json()
            place = ((url1_data['name']))
            print("You are in " + place)
            talk("You are in " + place)  
            lat = str((url1_data['coord']['lat']))
            print("Your latitude is " + lat)
            talk("Your latitude is " + lat)
            lon = str((url1_data['coord']['lon']))
            print("Your longitude is " + lon)
            talk("Your longitude is " + lon)
            command = command.replace(command, '')
        elif 'what is your name' in command:
            print('My name is siri')
            talk('My name is siri')
            command = command.replace(command, '')
        elif 'close chrome' in command:
            talk('Yes sir')
            os.system("taskkill /f /im chrome.exe")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I %M %p')
            print(time)
            talk("it's" + time)
            command = command.replace(command, '')
        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 5)
            print(command)
            print(info)
            talk(info)
            command = command.replace(command, '')
        elif 'shutdown' in command:
            pywhatkit.shutdown(10)
            talk('Shutting down in 10 seconds')
        elif "date" in command:
            date = datetime.datetime.now().date()
            var = str(date)
            cho = var[5:7]
            if cho == "01":
                pick = "Jan"
            if cho == "02":
                pick = "Feb"
            if cho == "03":
                pick = "Mar"
            if cho == "04":
                pick = "Apr"
            if cho == "05":
                pick = "May"
            if cho == "06":
                pick = "Jun"
            if cho == "07":
                pick = "Jul"
            if cho == "08":
                pick = "Aug"
            if cho == "09":
                pick = "Sep"
            if cho == "10":
                pick = "Oct"
            if cho == "11":
                pick = "Nov"
            if cho == "12":
                pick = "Dec"
            print("Today's date is " + pick, var[8:10], var[0:4])
            talk("Today's date is " + var[8:10] + pick + var[0:4])
            command = command.replace(command, '')
        elif 'bye bye' in command:
            print('Bye sir. have a good day')
            talk('Bye sir. have a good day')
            break
            sys.exit()
        elif 'how are you' in command:
            print("I am fine sir. what about you ?")
            talk("I am fine sir. what about you ?")
        elif 'close notepad' in command:
            talk('closing notepad')
            os.system("taskkill /f /im notepad.exe")
        elif 'play' in command:
            command = command.replace('play', '')
            print(command)
            talk('Playing' + command)
            print('Processing...')
            pywhatkit.playonyt(command)
            command = command.replace(command, '')
run_command()