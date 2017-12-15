import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "All signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

def create_command(bot):

    @bot.command(name='8ball', pass_context=True, brief="You got a question, you ask the 8-ball.")
    async def eightball(ctx):
        """
        Answers a yes/no question.
        """
        await bot.say(':8ball: ' + random.choice(answers))
