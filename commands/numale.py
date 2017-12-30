import random

numales = open("data/numales.txt").readlines()

def create_command(bot):

    @bot.command(pass_context=True, brief="Posts that face (you know which "
                 "one)")
    async def numale(ctx):
        await bot.say(random.choice(numales))
