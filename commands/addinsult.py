from database import db

def create_command(bot):
    
    table = db.table('insults')

    
    @bot.command(pass_context=True, brief="Adds a new insult to the database.")
    async def addinsult(ctx, *, insult):
        """
        Adds a new insult to the database. Occurences of {} will be replaced
        with username, so you can have personalized insults.

        Example of use: !addinsult {} loves Oblivion
        """
        if '{}' not in insult:
            await bot.say('Your insult does not include "{}", rejected.')
        else:
            table.insert({'insult': insult})
            await bot.say('Insult added.')
        

    return addinsult
