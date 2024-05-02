import requests as req
import pyttsx3
import json

print(":::: Welcome to pyWeatherBot 0.1 (type 's' to stop) ::::")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        city = input("Enter City : ")
        if(city == "s"):
            speak_text("Thanks for using our application!")
            break
        url = f"https://api.weatherapi.com/v1/current.json?key=a29bbdc24bda436b9e3101655232412&q={city}"
        res = req.get(url)
        wdic = json.loads(res.text)
        w = wdic["current"]["temp_c"]
        speak_text(f"The current weather in {city} is {w} degrees!")
    except Exception as e:
        speak_text(f"Something Wrong!")
