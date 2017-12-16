import html
import json
import random
import requests

from database import db
from discord import Colour, Embed
from tinydb import Query


QUIZ_API = "https://opentdb.com/api.php?amount=1"
userdata = db.table('userdata')


def difficulty_to_stars(difficulty):
    if difficulty == 'easy':
        return ':star:'
    elif difficulty == 'medium':
        return ':star:'*2
    elif difficulty == 'hard':
        return ':star:'*3
    else:
        return 'Unknown'

def format_answers(correct, incorrect):
    incorrect.append(correct)
    answers = incorrect
    random.shuffle(answers)

    answers = '\n'.join(['{}. {}'.format(x+1, y) for (x, y) in enumerate(answers)])
    
    return answers

def create_command(bot):

    @bot.command(pass_context=True)
    async def quiz(ctx):
        question = requests.get(QUIZ_API).text
        question = json.loads(question)
        question = question['results'][0]

        embed = Embed()
        embed.type="rich"
        embed.color = Colour.green()
        embed.add_field(
            name="Category",
            value=question['category']
        )
        embed.add_field(
            name="Difficulty",
            value=difficulty_to_stars(question['difficulty'])
        )
        embed.add_field(
            name="Question",
            value=html.unescape(question['question'])
        )
        embed.add_field(
            name="Answers",
            value=format_answers(question['correct_answer'], question['incorrect_answers'])
        )

        user_entry = Query()
        user_entry = userdata.get(user_entry.id == ctx.message.author.id)
        userdata.update(
            {'quiz_last_question': json.dumps(question)},
            doc_ids=[user_entry.doc_id]
        )
        
        await bot.say(None, embed=embed)

    return quiz
