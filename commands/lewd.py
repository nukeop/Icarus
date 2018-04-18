import json
import requests

from discord import Colour, Embed
from config import config

DANBOORU_API = "http://danbooru.donmai.us/posts.json?limit=1&random=true&tags={}"
login = config["danbooru_login"]
api_key = config["danbooru_apikey"]


def generate_help_string():
    help = "\
    Shows random lewd image from Danbooru tagged with the term passed as a parameter. \n \
    Please remember to carefully use parameters to avoid bugs.\
    "
    return help


async def get_lewd(term, bot):
    try:
        res = requests.get(DANBOORU_API.format(term), auth=(login, api_key)).content
        parsed = json.loads(res)
        if parsed == []:
            return "empty"
        post = parsed[0]
        return post["file_url"]
        
    except:
        await bot.say("Something happened ;^)")


def create_command(bot):

    @bot.command(pass_context=True, brief="Random lewd image for you. Courtesy of danbooru.donmai.us", help=generate_help_string())
    async def lewd(ctx, *, term):
        lewd = await get_lewd(term, bot)

        if lewd == "empty":
            await bot.say("Couldn't find any image tagged with " + term + ".")

        embed = Embed()
        embed.type = "rich"
        embed.colour = Colour.magenta()

        embed.set_image(
            url=lewd
        )
        await bot.say(None, embed=embed)
