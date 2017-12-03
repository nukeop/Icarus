def create_command(bot):

    @bot.command(pass_context=True, brief="Insults another user")
    async def insult(ctx):
        """
        Insults another user.
        """
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]
            await bot.say('{} '.format(user.mention))
        else:
            await bot.say('Mention the user you want to insult.')
        
    return insult
