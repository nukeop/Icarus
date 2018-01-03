def create_command(bot):

    @bot.command(pass_context=True, brief="Shows the mentioned user's avatar")
    async def av(ctx):
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]

            if user.avatar_url:
                await bot.say('Avatar of mentioned user {}:\n{}'.format(user.mention, user.avatar_url))
            else:
                await bot.say('User {} has no avatar.'.format(user.mention))
        else:
            await bot.say('Mention is required.')

    return av
