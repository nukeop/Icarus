from discord import Colour, Embed
from discord.ext import commands as discord_commands

from checks import check_if_owner
from database import db

stats_table = db.table('stats')

def create_command(bot):
    @bot.command(pass_context=True, brief="Shows command statistics (owners only)")
    @discord_commands.check(check_if_owner)
    async def stats(ctx):
        embed = Embed()
        embed.type="rich"
        embed.title = 'Command invocation stats'
        
        embed.description = '```'

        rows = reversed(sorted(stats_table.all(), key=lambda x: x['invoked']))
        for row in rows:
            embed.description += '{}: {}\n'.format(row['name'], row['invoked'])

        embed.description += '```'
        
        await bot.say(None, embed=embed)
