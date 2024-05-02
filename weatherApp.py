import requests as req
import json

city = input("Enter City : ")

url = f"https://api.weatherapi.com/v1/current.json?key=a29bbdc24bda436b9e3101655232412&q={city}"

res = req.get(url)

wdic = json.loads(res.text)
print(wdic)