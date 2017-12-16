import random
import time

from discord import Colour, Embed

# rolling a dice with X sides

def get_value(sides):
    sides = int(sides)
    if sides < 1:
        return False
    
    if sides >= 1:
        value = random.randint(1, sides)

    return value
    
def create_command(bot):
    @bot.command(pass_context=True, brief="Roll a dice")
    async def dice (ctx, *, sides):
        if get_value(sides):
            
            embed= Embed()
            embed.type= "rich"
            embed.color= Colour.dark_teal()
            embed.add_field(
                name=":game_die::wave: {} rolled and got".format(ctx.message.author.display_name),
                value=get_value(sides)
            )
            await bot.say(None, embed=embed)
        
