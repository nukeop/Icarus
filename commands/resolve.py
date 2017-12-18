import random
import time

from discord import Colour, Embed

positive={
    "Courageous" : "A moment of valor shines brightest against a backdrop of despair.",
    "Focused" : "A moment of clarity in the eye of the storm...	",
    "Powerful" : "Anger is power- unleash it!",
    "Stalwart" : "Many fall in the face of chaos, but not this one!... not today.",
    "Vigorous" : "Adversities can foster hope, and resilience.",
    }


negative={
    "Abusive" : "Frustration, and fury! ...More destructive than a hundred cannons",
    "Fearful" : "Fear and frailty finally claim their due...",
    "Hopeless" : "There can be no hope in this hell... no hope at all.",
    "Irrational" : "Reeling! Gasping! Taken over the edge, into madness.",
    "Masochistic" : "Those who covet injury, find it in no short supply.",
    "Paranoid" : "The walls close in, the shadows whisper of conspiracy. ",
    "Selfish" : "Self-preservation is paramount, at any cost.",
}


def get_pos_neg():

    return random.choice(list(negative.items())) if random.randint(0,1) == 1 else random.choice(list(positive.items()))


def create_command(bot):
    @bot.command(pass_context= True, brief= "Test your resolve")
    async def resolve (ctx):
        effect = get_pos_neg()
        await bot.say("{}\'s resolve is being tested...".format(ctx.message.author.display_name))
        time.sleep(3)
        
        embed = None

        if effect in list(negative.items()):
            embed = Embed(
                title = "",
                description = ":anger:" + effect[0]
            )
            embed.type= "rich"
            embed.color = Colour.red()
            embed.set_footer(
               text= effect[1]
            )
            
            await bot.say(None, embed=embed)

        else:
            embed = Embed(
                title = "",
                description =":sparkles:" + effect[0]
            )
            embed.type= "rich"
            embed.color = Colour.gold()
            embed.set_footer(
                text= effect[1]
            )

            await bot.say(None, embed=embed)
            
