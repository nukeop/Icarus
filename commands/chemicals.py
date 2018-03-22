import random
import string

def get_chemical():
    return random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)

def create_command(bot):

    @bot.command(pass_context=True, brief="Generates random chemicals")
    async def chemicals(ctx):
        await bot.say('\n'.join([get_chemical() for _ in range(5)]))

    return chemicals
