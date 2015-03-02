import json, requests, csv


# city = raw_input("Type a city: ")
city = 'London'

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric' %city) 
data = json.loads(r.content)


name = data['name']
weather = data['weather'][0]['description']
temp = data['main']['temp']

print """%s: 
Temperature: %s 
Weather: %s""" % (name, temp, weather)


