import os
import socket
import subprocess

from discord import Colour, Embed
from discord.ext import commands as discord_commands

from checks import check_if_owner

def create_command(bot):

    @bot.command(pass_context=True, brief="Bot diagnostics for owners")
    @discord_commands.check(check_if_owner)
    async def diagnostics(ctx):
        """
        Shows various diagnostics useful for bot owners, such as the hostname
        of the machine the bot is running on. Only responds to the person
        specified as the owner in the config.
        """
        embed = Embed()
        embed.type = "rich"

        embed.add_field(
            name="Hostname",
            value=socket.gethostname()
        )

        embed.add_field(
            name="Server count",
            value=len(bot.servers)
        )

        uptime=subprocess.check_output(['uptime']).decode('utf-8')
        uptime = ' '.join(uptime.split(' ')[:3]).strip()
        embed.add_field(
            name="Uptime",
            value=uptime
        )
        
        await bot.send_message(ctx.message.author, None, embed=embed)

    return diagnostics
