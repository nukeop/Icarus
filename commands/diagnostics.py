import socket

from discord.ext import commands as discord_commands

from checks import check_if_owner

def create_command(bot):

    @bot.command(pass_context=True, brief="Bot diagnostics for owners")
    @discord_commands.check(check_if_owner)
    async def diagnostics(ctx):
        await bot.send_message(ctx.message.author, socket.gethostname())

    return diagnostics
