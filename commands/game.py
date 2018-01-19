from igdb_api_python.igdb import igdb
from discord import Colour, Embed

from config import config

igdb = igdb(config['igdb_api_key'])

def get_game(title):
    result = igdb.games({
        'search': title,
        'fields': 'name'
    }).body[0]

    result = igdb.games({
        'ids': result['id'],
        'expand': ['developers']
    })
    return result.body[0]

def embed_game(game):        
    embed = Embed()
    embed.type = 'rich'
    embed.color = Colour.green()

    embed.title = game['name']
    embed.description = game['summary']
    embed.url = game['url']

    embed.set_footer(
        text='Game info powered by igdb.com'
    )

    try:
        cover = game['cover']['url']
        if cover[0] == '/':
            cover = 'https:' + cover
        embed.set_thumbnail(
            url=cover
        )
    except KeyError:
        pass
        
    try:
        screenshot = game['screenshots'][0]['url']
        if screenshot[0] == '/':
            screenshot = 'https:' + screenshot

        embed.set_image(
            url=screenshot
        )
    except KeyError:
        pass

    try:
        embed.add_field(
            name='Rating',
            value=round(float(game['rating']), 1)
        )
    except KeyError:
        pass

    try:
        developers = ', '.join(x['name'] for x in game['developers'])

        embed.add_field(
            name='Developers',
            value=developers
        )
    except KeyError:
        pass

    return embed
            
def create_command(bot):
    @bot.command(pass_context=True, brief="Shows information about videogames")
    async def game(ctx, *, terms):
        game = get_game(terms)
        embed = embed_game(game)
        await bot.say(None, embed=embed)
        
