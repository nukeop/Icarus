import argparse
import discord
from discord.ext import commands as discord_commands
from tinydb import Query

import asyncio
import importlib
import logging
import os

import commands
from config import config
from database import db
from media import create_media_commands
from update import periodic_autoupdate, send_after_update_message

log = None
bot = discord_commands.Bot(command_prefix='!',
                           description=config['description'], pm_help=True)
bot.command_functions = []
userdata = db.table('userdata')


def startup_info():
    log.info('Starting Icarus...')
    periodic_autoupdate()
    

async def after_login_info():
    log.info('Connected servers: {}'.format(len(bot.servers)))

    db.purge_table('connected_servers')
    table = db.table('connected_servers')
    for server in bot.servers:
        try:
            table.insert({'server': {
                'id': server.id,
                'name': server.name,
                'owner': server.owner.id,
                'member_count': server.member_count
            }})
        except:
            pass
            
    if config['updated']:
        for server in bot.servers:
            main_channel = [c for c in list(server.channels) if c.type ==
                        discord.ChannelType.text and c.position == 0][0]
            await send_after_update_message(bot, main_channel)

 
@bot.event
async def on_ready():
    log.info('Logged in as {} ({})'.format(bot.user.name, bot.user.id))
    await after_login_info()


@bot.event
async def on_message(message):
    user_db_entry = Query()
    entry = userdata.get(user_db_entry.id == message.author.id)
    if not entry:
        doc_id = userdata.insert({'id': message.author.id})
        entry = userdata.get(doc_id=doc_id)

    userdata.update({'name': message.author.name}, doc_ids=[entry.doc_id])
    await bot.process_commands(message)


@bot.check
def checkDevMode(ctx):
    return (not config['dev'] or ctx.message.channel.name == 'icarus')


def configure_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.getLogger('websockets').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('github').setLevel(logging.WARNING)

    formatter = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s -"
                                  " %(message)s")

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    root.addHandler(console)

    return root

    
def import_commands():
    log.info("Scanning commands...")
    files = os.listdir(os.path.join(os.path.dirname(__file__),
                                    commands.__name__))
    files = [os.path.splitext(x)[0] for x in sorted(files) if
             os.path.splitext(x)[1] == ".py"]
    for module in files:
        log.info("Loading command: {}".format(module))
        cmd = importlib.import_module('commands.{}'.format(module))
        if hasattr(cmd, 'create_command'):
            cmd_fun = cmd.create_command(bot)
            bot.command_functions.append(cmd_fun)
        else:
            log.error("Invalid command: {}, skipping".format(module))
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', action='store_true', help='If enabled, the'
                        ' bot will only talk in channels named #icarus')
    parser.add_argument('--updated', action='store_true', help='This option'
                        ' will make the bot announce that it has been updated'
                        ' when it connects to the channels. Typically only'
                        'used by the auto-update script')
    args = parser.parse_args()

    config['dev'] = args.dev
    config['updated'] = args.updated
    
    log = configure_logging()
    startup_info()
    import_commands()
    create_media_commands(bot)
    bot.run(config['token'])
