import random
import time

def create_command(bot):

    @bot.command(pass_context=True, name="russianroulette", help="Play russian roulette")
    async def russianRoulette(ctx):
        """
        1 out of 6 chambers is loaded. This command lets you test your luck.
        """
        await bot.say("{} spins the barrel and pulls the trigger... :gun:".format(ctx.message.author.mention))
        time.sleep(3)
                      
        if random.randrange(0, 5) < 1:
            await bot.say("BANG! :boom::gun: {} is dead.".format(ctx.message.author.mention))
        else:
            await bot.say("\*click\*")
