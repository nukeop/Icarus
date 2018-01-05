import json
import random

import pokebase as pb
from discord import Colour, Embed

def embed_pokemon(poke):
    species = poke.species
    descriptions = []
    for entry in species.flavor_text_entries:
        if entry.language.name == 'en':
            descriptions.append(entry.flavor_text)
    types = sorted(list(poke.types), key=lambda x: x.slot)
    types = '/'.join(x.type.name.capitalize() for x in types)
    
    embed = Embed()
    embed.type = "rich"
    embed.color = Colour.blue()
    embed.title = "You caught: #{} {}".format(species.id, poke.name.capitalize())
    embed.description = random.choice(descriptions)
    
    embed.set_image(
        url=poke.sprites.front_default
    )

    embed.add_field(
        name='Type',
        value=types
    )

    return embed


def create_command(bot):
    @bot.command(pass_context=True, brief="Catch a random pokemon")
    async def pokemon(ctx):
        l = pb.APIResourceList('pokemon')
        poke = random.choice(list(l))
        poke = pb.NamedAPIResource('pokemon', poke['name'])
        embed = embed_pokemon(poke)
        await bot.say(None, embed=embed)
