import discord
from discord.ext import commands

import asyncio

from commands.insult import create_command

bot = commands.Bot(command_prefix='!')
create_command(bot)

@bot.event
async def on_ready():
    print('Logged in as {} ({})'.format(bot.user.name, bot.user.id))
    
bot.run('')
