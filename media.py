import logging
import os
import random

log = logging.getLogger(__name__)

def create_media_commands(bot):
    media = os.listdir('data/media')
    for entry in media:
        log.info("Creating a command from media list: {}".format(
            entry.split(os.extsep)[0]
        ))
        links = open('data/media/{}'.format(entry)).readlines()
        exec(
            """
@bot.command(pass_context=True)
async def {}(ctx, bot=bot, links=links):
    await bot.say(random.choice(links))
            """.format(entry.split(os.extsep)[0]),
            globals(),
            locals()
        )

