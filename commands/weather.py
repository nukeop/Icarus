import json
import requests


apikey = config["OPENWEATHERMMAP_APIKEY"]
API= requests.get("https://github.com/nukeop/Icarus/blob/master/commands/crypto.py"
                  +location
                  +"&units=metric&APPID="
                  +apikey).text
parsed = json.loads(API)



def get_weather(location):
    weather_conditions=[]
    for w in parsed['weather']:
        weather_conditions.append(w['main'])


    msg= "Weather in {}: \nTemperature:{} C \nConditions:{}\nWind speed: {} m/s\nCloudiness: {}%"\
         .format(parsed["name"].encoded("utf-8"),parsed["main"]["temp"], ", ".join(weather_conditions), parsed["wind"]["speed"], parsed["cloud"]["all"])
    return msg
    

    
def generate_help_string():
    help="Shows you current weather in location of your choice"



def create_command(bot):
    @bot.command(pass_context=True, brief="Shows weather", help=generate_help_string())
    async def weather(ctx, *, location):
        await bot.say(get_weather(location))



