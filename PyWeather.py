import requests
import pprint

pp = pprint.PrettyPrinter(indent=2)
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=springfield,ohio&appid=6e86794d3d979323e578481f0d846126"
)

weather = response.json()
pp.pprint(weather)
