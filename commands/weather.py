import json
import requests

from config import config



def get_weather(location):
    apikey = config["openweathermap_apikey"]
    r= requests.get("http://api.openweathermap.org/data/2.5/find?q="+location+"&units=metric&appid="+apikey).text
    parsed = json.loads(r)

    weather_conditions=[]
    for w in parsed['list'][0]['weather']:
        weather_conditions.append(w['main'])


    msg= "Weather in {}: \nTemperature: {} C \nConditions: {}\nWind speed: {} m/s\nCloudiness: {}%"\
         .format(parsed['list'][0]["name"], parsed['list'][0]["main"]["temp"], ", ".join(weather_conditions), parsed['list'][0]["wind"]["speed"], parsed['list'][0]["clouds"]["all"])
    return msg
    

    
def generate_help_string():
    help="Shows you current weather in location of your choice"



def create_command(bot):
    @bot.command(pass_context=True, brief="Shows weather", help=generate_help_string())
    async def weather (ctx, *, location):
        await bot.say(get_weather(location))
