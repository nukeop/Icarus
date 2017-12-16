import json
import requests

QUIZ_API = "https://opentdb.com/api.php?amount=1"

def create_command(bot):

    @bot.command(pass_context=True)
    async def quiz(ctx):
        question = requests.get(QUIZ_API).text
        question = json.loads(question)
        question = question['results'][0]

        message = []
        message.append("Category: {}")

    return quiz
