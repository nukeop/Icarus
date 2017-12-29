import json
import requests
import urllib.parse

from config import config
from discord import Colour, Embed


apikey = config["lastfm_api_key"]
LASTFM_ALBUM_SEARCH = "http://ws.audioscrobbler.com/2.0/?method=album.search&album={}&api_key={}&format=json"


def get_album_info(album):
    album = urllib.parse.quote(album)
    return json.loads(requests.get(LASTFM_ALBUM_SEARCH.format(album, apikey)).text)


def get_album_embed(data):
    album = data['results']['albummatches']['album'][0]
    
    embed = Embed()
    embed.type = "rich"
    embed.color = Colour.green()

    embed.title = '{} - {}'.format(album['artist'], album['name'])

    embed.set_image(
        url=album['image'][-1]['#text']
    )

    return embed

    
def create_command(bot):
    @bot.command(pass_context=True, brief="Shows info about music albums")
    async def album(ctx, *, album):
        """
        searches last.fm for albums matching the supplied name, and
        returns info relevant to the closest match (album art, artist and album
        name)
        """
        data = get_album_info(album)
        embed = get_album_embed(data)
        await bot.say(None, embed=embed)
