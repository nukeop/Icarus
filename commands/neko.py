import json
import requests

from discord import Colour, Embed


NEKO_API = "http://nekos.life/api/neko"

def get_neko():
    r = requests.get(NEKO_API).text
    parsed = json.loads(r)
    return parsed["neko"]


def create_command(bot):

    @bot.command(pass_context=True, brief="Random neko image for you")
    async def neko(ctx):
        neko = get_neko()
        
        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.magenta()

        embed.set_image(
            url=neko
        )
        await bot.say(None, embed=embed)
