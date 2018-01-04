from config import config
from discord import Colour, Embed


INVITE_URL = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0"

def invite_embed(bot):
    embed = Embed()
    embed.type = "rich"
    embed.title = "Add me to your server"
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.description = "[Click here for the invite link]({})".format(INVITE_URL.format(bot.user.id))
    
    embed.add_field(
        name='Github repo',
        value=config['repository']
    )
    
    return embed

def create_command(bot):

    @bot.command(pass_context=True, brief="PMs you an invite link so you can add this bot to your channel")
    async def invite(ctx):
        """
        PMs you an invite link so you can add this bot to your channel.
        """
        embed = invite_embed(bot)
        await bot.say(None, embed=embed)

    return invite
    
