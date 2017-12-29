INVITE_URL = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0"

def create_command(bot):

    @bot.command(pass_context=True, brief="PMs you an invite link so you can add this bot to your channel")
    async def invite(ctx):
        """
        PMs you an invite link so you can add this bot to your channel.
        """
        await bot.say("Use the link below to add me to your server.")
        await bot.say(INVITE_URL.format(bot.user.id))
        await bot.say("You can only add me to servers you own or administrate.")

    return invite
    
