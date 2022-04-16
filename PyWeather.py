import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)
'''
 Requires you to make an account to generate an API
 Make an account at https://openweathermap.org
'''
int_city = input('City: ')
int_state = input('State: ')
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={int_city}, {int_state}&appid=6e86794d3d979323e578481f0d846126"
)

weather = response.json()
pp.pprint(weather)
