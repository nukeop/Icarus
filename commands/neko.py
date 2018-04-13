import json
import requests

from discord import Colour, Embed


NEKO_API = "http://nekos.life/api/neko"
API_SECOND = "http://nekos.life/api/v2/img/"


def generate_help_string():
    help = "\
    Shows random neko image if used withous any additional parameters. \n \
    You can add a parameter at the end of query to specify what kind of image you would like to see. Parameters you can use are: \n \
    cum \n les \n meow \n tickle \n lewd \n feed \n bj \n \
    nsfw_neko_gif \n poke \n anal \n slap \n pussy \n lizard \n\
    classic \n kuni \n pat \n kiss \n cuddle \n fox_girl \n\
    boobs \n hug \n \n\
    Please remember to carefully use parameters to avoid bugs.\
    "
    return help

async def get_neko(term, bot):
    try:
        if term:
            r = requests.get(API_SECOND + term).text
            parsed = json.loads(r)
            return parsed["url"]
        else:
            r = requests.get(NEKO_API).text
            parsed = json.loads(r)
            return parsed["neko"]
    except:
        await bot.say("Wrong argument. Type !help neko to see the list of available parameters")

def create_command(bot):

    @bot.command(pass_context=True, brief="Random neko image for you. Possibly nsfw", help=generate_help_string())
    async def neko(ctx , *, term):
        neko = await get_neko(term, bot)
        
        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.magenta()

        embed.set_image(
            url=neko
        )
        await bot.say(None, embed=embed)
