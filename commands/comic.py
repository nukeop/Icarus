import json
import requests

from discord import Colour, Embed


API_URL_XKCD = "http://xkcd.com/info.0.json"


def get_comic():
    requested = requests.get(API_URL_XKCD).text
    parsed = json.loads(requested)

    picture = parsed["img"]

    return picture

def create_command(bot):
    @bot.command(pass_context= True, brief = "xkcd comic")
    async def comic(ctx):

        picture = get_comic()

        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.dark_orange()
        embed.set_image(
            url = picture
        )
        await bot.say(None, embed=embed)
