from config import config

def check_if_owner(ctx):
    return config['owner'] == ctx.message.author.id
