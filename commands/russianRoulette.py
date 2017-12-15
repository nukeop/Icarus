import random
import time

def create_command(bot):

    @bot.command(pass_context=True, name="russianroulette")
    async def russianRoulette(ctx):
        await bot.say("{} spins the barrel and pulls the trigger... :gun:".format(ctx.message.author.mention))
        time.sleep(3)
                      
        if random.randrange(0, 5) < 1:
            await bot.say("BANG! :boom::gun: {} is dead.".format(ctx.message.author.mention))
        else:
            await bot.say("\*click\*")
