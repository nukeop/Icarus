import json
import requests

from config import config

API = 'http://www.omdbapi.com/?t={}&apikey={}'

def get_movie_info(movie):
    r = requests.get(API.format(movie, config['omdb_api_key'])).text
    parsed = json.loads(r)
    if 'Error' in parsed:
        return (parsed['Error'], None)

    seasons = ''
    if 'totalSeasons' in parsed:
        seasons = 'Seasons: {}\n'.format(parsed['totalSeasons'])
    print(parsed)
        
    msg = ("Title: {}\nYear: {}\nRuntime: {}\nGenre: {}\nCountry: {}\n{}Plot: "
           "{}").format(parsed['Title'], parsed['Year'], parsed['Runtime'],
                        parsed['Genre'], parsed['Country'], seasons,
                        parsed['Plot'])
    return (msg, parsed['Poster'])

def create_command(bot):

    @bot.command(pass_context=True, brief="Shows information about movies")
    async def movie(ctx, *, terms):
        """
        !movie <title> will show you information pulled from IMDB, including
        title, release date, runtime, genre, country, a plot summary, and a
        poster thumbnail.
        """
        movie_info = get_movie_info(terms)
        
        await bot.say(movie_info[0])
        await bot.say(movie_info[1])
