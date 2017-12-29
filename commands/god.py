import random

from discord import Colour, Embed

words = open("data/GodWordsHappy.txt").readlines()

def get_words(words, num):
    return " ".join([random.choice(words).strip() for _ in range(num)])

def create_command(bot):

    @bot.command(pass_context=True, brief="Allows you to communicate with God")
    async def god(ctx, num=10):
        """
        Ask God for his input on any subject.
        """
        embed = Embed(
            description=get_words(words, num)
        )
        embed.type = "rich"
        embed.color = Colour.blue()
        
        await bot.say("God says...", embed=embed)

    return god
