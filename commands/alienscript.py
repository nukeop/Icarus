import random

CHARS = '. ,'

def get_alien_script():
    length = random.randint(10, 50)
    return ''.join([random.choice(CHARS) for _ in range(length)])


def create_command(bot):
    @bot.command(pass_context=True, brief="Generates alien words.")
    async def alienscript(ctx):
        await bot.say(get_alien_script())

    return alienscript
