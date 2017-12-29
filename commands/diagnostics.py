import socket

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
        await bot.send_message(ctx.message.author, socket.gethostname())

    return diagnostics
