import json
import requests
import urllib.parse

from config import config

from discord import Colour, Embed


apikey = config["openweathermap_apikey"]
API_PT_1="http://api.openweathermap.org/data/2.5/find?q="
API_PT_2="&units=metric&appid="
 


def get_weather(location):
    location = urllib.parse.quote(location)
    r = requests.get(API_PT_1 + location + API_PT_2 + apikey).text
    parsed = json.loads(r)

    weather_conditions = [w['main'] for w in parsed['list'][0]['weather']]
        
    weather = parsed['list'][0]["name"]
    temperature = parsed['list'][0]["main"]["temp"]
    wspeed = parsed['list'][0]["wind"]["speed"]
    clouds = parsed['list'][0]["clouds"]["all"]

    return (weather, temperature, wspeed, clouds, weather_conditions)


def create_command(bot):
    @bot.command(pass_context=True, brief="Shows weather")
    async def weather (ctx, *, location):
        """
        !weather <location> - look up weather information in a city or a region
        """
        weather = get_weather(location)
    
        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.gold()

        embed.add_field(
            name=":rainbow: Weather in ",
            value=weather[0]
        )

        embed.add_field(
            name=":sun_with_face: Temperature: ",
            value=str(weather[1]) + " C"
        )

        embed.add_field(
            name=":warning: Conditions: ",
            value=', '.join(weather[4])
        )

        embed.add_field(
            name=":cloud_tornado: Wind speed: ",
            value=str(weather[2]) + " m/s"
        )

        embed.add_field(
            name=":white_sun_small_cloud: Cloudiness: ",
            value=str(weather[3]) + " %"
        )

        await bot.say(None, embed=embed)

