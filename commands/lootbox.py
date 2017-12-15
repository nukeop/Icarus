import random
import time

lootbox_contents = open("data/lootbox.txt").readlines()

def create_command(bot):

    @bot.command(pass_context=True)
    async def lootbox(ctx):
        await bot.say("{} is opening a loot box... :gift:".format(ctx.message.author.mention))
        time.sleep(3)
        await bot.say(random.choice(lootbox_contents))
