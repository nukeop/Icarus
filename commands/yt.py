import json
import requests

from config import config

YT_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search?part=id,snippet&type=video&maxResults=50&q={}&key={}"
YT_WATCH_URL = "https://www.youtube.com/watch?v={}"


def yt_search(terms):
    results = json.loads(
        requests.get(
            YT_SEARCH_URL.format(terms, config['yt_api_key'])
        ).text
    )

    return results

    
def create_command(bot):
    @bot.command(pass_context=True, brief="Youtube search")
    async def yt(ctx, *, terms):
        search = yt_search(terms)
        best_match = search['items'][0]
        
        
        await bot.say(YT_WATCH_URL.format(best_match['id']['videoId']))

    return yt
