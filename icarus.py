import discord
from discord.ext import commands as discord_commands

import asyncio
import importlib
import logging
import os

import commands
from config import config
from update import check_for_updates

log = None
bot = discord_commands.Bot(command_prefix='!',
                           description=config['description'], pm_help=True)
bot.command_functions = []


def startup_info():
    log.info('Starting Icarus...')
    

def after_login_info():
    log.info('Connected servers: {}'.format(len(bot.servers)))
    for server in bot.servers:
        log.info("{} ({})".format(server.name, server.id))

    
@bot.event
async def on_ready():
    log.info('Logged in as {} ({})'.format(bot.user.name, bot.user.id))
    after_login_info()


@bot.event
async def on_command(ctx, error):
    check_for_updates()
    

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
            

log = configure_logging()
startup_info()
import_commands()
bot.run(config['token'])
