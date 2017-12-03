from database import db

def create_command(bot):

    def init_db():
        if db.get('insults') is None:
            db.set('insults', [])
        

    init_db()
    print(db.get('insults'))
    
    @bot.command(pass_context=True, brief="Adds a new insult to the database.")
    async def addinsult(ctx, *args):
        insult = ' '.join(args)
        

    return addinsult
