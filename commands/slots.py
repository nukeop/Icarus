import random

symbols = [
    ":bell:",
    ":spades:",
    ":cherries:",
    ":lemon:",
    ":tangerine:",
    ":grapes:",
    ":melon:",
    ":gem:",
    ":moneybag:",
    ":seven:"
]

rewards = {
    ":bell:": "100 internets.",
    ":spades:": "200 internets.",
    ":cherries:": "250 internets.",
    ":lemon:": "300 internets",
    ":tangerine:": "500 internets",
    ":grapes:": "750 internets",
    ":melon:": "1000 internets and a free drink at the bar.",
    ":gem:": "1500 internets and a vintage CRT monitor.",
    ":moneybag:": "5000 internets and a candy bar.",
    ":seven:": "JACKPOT! You win all the internets."
}


def gen_slot_results(symbols, columns, random=random):
    return [random.choice(symbols) for _ in range(columns)]

def check_win(results):
    return (
        type(results) == type([]) and
        len(results) > 0 and
        results.count(results[0]) == len(results)
    )


def create_command(bot):

    @bot.command(pass_context=True)
    async def slots(ctx):
        await bot.say(":slot_machine: {} decided to give the slot machine a spin.".format(ctx.message.author.mention))
        slot_results = gen_slot_results(symbols, 3)
        await bot.say(''.join(slot_results))
        if check_win(slot_results):
            await bot.say('{} has won!'.format(ctx.message.author.mention))
            await bot.say('Your reward is: {}'.format(rewards[slot_results[0]]))
        
    return slots
