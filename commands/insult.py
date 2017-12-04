import random
from database import db

def create_command(bot):

    table = db.table('insults')

    @bot.command(pass_context=True, brief="Insults another user")
    async def insult(ctx):
        """
        Insults another user.
        """
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]
            insults = table.all()
            if len(insults) < 1:
                await bot.say('No insults in the database.')
                return
            
            insult = random.choice(insults)['insult']

            await bot.say(insult.format(user.mention))
        else:
            await bot.say('Mention the user you want to insult.')
        
    return insult
