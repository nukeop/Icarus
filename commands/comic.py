import json
import requests

from discord import Colour, Embed

API_URL_XKCD_LATEST = "http://xkcd.com/info.0.json"
API_URL_XKCD = "http://xkcd.com/{}/info.0.json"

def get_xkcd_latest():
    return json.loads(requests.get(API_URL_XKCD_LATEST).text)

def get_xkcd(i):
    return json.loads(requests.get(API_URL_XKCD.format(i)).text)

def xkcd_embed(data):
    embed = Embed()
    embed.type = "rich"
    embed.title = 'XKCD - {}: {}'.format(data['num'], data['safe_title'])
    embed.description = data['alt']
    embed.set_image(
        url=data['img']
    )

    return embed

def create_command(bot):
    @bot.command(pass_context= True, brief = "xkcd comic")
    async def comic(ctx):
        embed = xkcd_embed(get_xkcd_latest())
        embed.color = Colour.dark_orange()
        await bot.say(None, embed=embed)
