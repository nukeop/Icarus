import json
import requests

from discord import Colour, Embed
from config import config

DANBOORU_API = "http://danbooru.donmai.us/posts.json?limit=1&random=true&tags={}"
POST_URL = "http://danbooru.donmai.us/posts/{}"
login = config["danbooru_login"]
api_key = config["danbooru_apikey"]


def generate_help_string():
    help = "\
    Shows random lewd image from Danbooru tagged with the terms (up to a maximum of two) passed as parameters. \n \
    A space denotes two different tags to be searched for, use underscore for when a tag has more than one word. \n \
    For example: '!lewd red_hair one_piece_swimsuit' will search for an image tagged with 'red_hair' and 'one_piece_swimsuit'. \n \
    Please remember to carefully use parameters to avoid bugs.\
    "
    return help


async def get_lewd(term, bot):
    r = requests.get(DANBOORU_API.format(term), auth=(login, api_key)).text
    parsed = json.loads(r)
    try:
        if term:
            post = parsed[0]["file_url"]
            if (post == None):
                post = parsed[0]["source"]
            return {"post": post, "id": parsed[0]["id"]}
        elif (term == None):
             await bot.say("No arguments at the end of the query.")
    except:
        await bot.say("No images found, or incorrect query structure.")


    
def create_command(bot):

    @bot.command(pass_context=True, brief="Random lewd image for you. Courtesy of danbooru.donmai.us", help=generate_help_string())
    async def lewd(ctx, *, term=None):
        lewd = await get_lewd(term, bot)

        embed = Embed()
        embed.type = "rich"
        embed.colour = Colour.magenta()
        embed.set_image(
            url=lewd["post"]
        )
        embed.set_footer(
            text=POST_URL.format(lewd["id"])
        )
        await bot.say(None, embed=embed)
