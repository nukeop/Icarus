import random
import time

from discord import Colour, Embed

positive=[
    "Courageous",
    "Focused",
    "Powerful",
    "Stalwart",
    "Vigorous",
    ]
negative=[
    "Abusive",
    "Fearful",
    "Hopeless",
    "Irrational",
    "Masochistic",
    "Paranoid",
    "Selfish",
]




def get_pos_neg():

    return random.choice(negative) if random.randint(0,1) == 1 else random.choice(positive)


def create_command(bot):
    @bot.command(pass_context= True, brief= "Test your resolve")
    async def resolve (ctx):
        effect = get_pos_neg()


        
        await bot.say("{}\'s resolve is being tested...".format(ctx.message.author.display_name))
        time.sleep(3)
        
        embed = None

        if effect in negative:
            embed = Embed(
                title = "",
                description = ":anger:" + effect
            )
            embed.type= "rich"
            embed.color = Colour.red()
            await bot.say(None, embed=embed)

        else:
            embed = Embed(
                title = "",
                description =":sparkles:" + effect
            )
            embed.type= "rich"
            embed.color = Colour.gold()

            await bot.say(None, embed=embed)
            
