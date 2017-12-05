from config import config

def create_command(bot):

    @bot.command(pass_context=True, brief="")
    async def info(ctx):
        """
        Shows information about information about information
        """
        await bot.say("Icarus - a Discord bot")
        await bot.say("Development takes place here: {}".format(config['repository']))
