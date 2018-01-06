import json
import random
import requests

from discord import Colour, Embed

API = 'https://api.gwentapi.com/v0/'
CARDS_COUNT = 357


def random_card():
    cards = requests.get(API + 'cards?limit={}'.format(CARDS_COUNT)).text
    cards = json.loads(cards)
    cards = cards['results']
    return random.choice(cards)

def set_embed_color(embed, card_details):
    faction = card_details['faction']['name']
    if faction == 'Monster':
        embed.color = Colour.red()
    elif faction == 'Neutral':
        embed.color = Colour.dark_orange()
    elif faction == 'Nilfgaard':
        embed.color = Colour.darker_grey()
    elif faction == 'Northern Realms':
        embed.color = Colour.blue()
    elif faction == "Scoia'tael":
        embed.color = Colour.green()
    elif faction == 'Skellige':
        embed.color = Colour.purple()
        
    return embed

def embed_card(card):
    embed = Embed()
    embed.type = "rich"

    card_details = requests.get(card['href']).text
    card_details = json.loads(card_details)
    variation = json.loads(requests.get(
        random.choice(card_details['variations'])['href']
    ).text)

    embed.title = card_details['name']
    try:
        embed.description = card_details['flavor']
    except KeyError:
        pass

    embed.set_image(
        url=variation['art']['thumbnailImage']
    )

    embed.add_field(
        name='Effect',
        value=card_details['info']
    )

    embed.add_field(
        name='Rarity',
        value=variation['rarity']['name']
    )

    embed.add_field(
        name='Faction',
        value=card_details['faction']['name']
    )

    return set_embed_color(embed, card_details)

def create_command(bot):
    @bot.command(pass_context=True, brief="Pick a gwent card at random")
    async def gwent(ctx):
        card = random_card()
        await bot.say(None, embed=embed_card(card))
