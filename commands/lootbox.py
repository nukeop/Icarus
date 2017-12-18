import random
import time

from discord import Colour, Embed

lootbox_contents = open("data/lootbox.txt").readlines()

quotes=[
    "A boon, at last! ",
    "This expedition, at least, promises success.",
    "Leave nothing unchecked, there is much to be found in forgotten places.",
    "Trinkets and charms, gathered from all the forgotten corners of the earth... ",
    "Rarities and curios, sold at a profit, of course.",
    "Idol, amulet, or lucky charm - the simplest object can be a talisman against evil.",
    "Room by room, hall by hall, we reclaim what is ours",
    "Tokens of hope, recovered from the encroaching dark.",
    "Where there is no peril in the task, there can be no glory in its accomplishment.",
]


def create_command(bot):

    @bot.command(pass_context=True, brief="Opens a random lootbox for you")
    async def lootbox(ctx):
        await bot.say("{} is opening a loot box... :gift:".format(ctx.message.author.mention))
        time.sleep(3)

        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.gold()
        embed.add_field(
            name="The contents are yours...",
            value=random.choice(lootbox_contents)
        )
        embed.set_footer(
            text= random.choice(quotes)
        )
        await bot.say(None, embed=embed)
