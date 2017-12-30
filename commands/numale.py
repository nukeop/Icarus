import random

numales = [
    "https://i.imgur.com/Bo2bSDN.jpg",
    "https://i.imgur.com/TYhCjdf.jpg",
    "https://i.imgur.com/QVwovqY.jpg",
    "https://i.imgur.com/G373kWA.jpg",
    "https://i.imgur.com/7Dhu1nR.jpg",
]


def create_command(bot):

    @bot.command(pass_context=True, brief="Posts that face (you know which "
                 "one)")
    async def numale(ctx):
        await bot.say(random.choice(numales))
