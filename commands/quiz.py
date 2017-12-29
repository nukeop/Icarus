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
    answers = []
    answers.extend(incorrect)
    answers.append(correct)
    random.shuffle(answers)
    answers = list(enumerate(answers))

    answers_fmt = html.unescape('\n'.join(['{}. {}'.format(x+1, y) for (x, y) in answers]))
    
    return (answers, answers_fmt)

def create_command(bot):

    @bot.group(pass_context=True,brief="Answer trivia questions")
    async def quiz(ctx):
        """
        !quiz - shows you a random trivia question.
        !quiz <answer> - lets you answer the question. You can either use the
        answer index or type it (watch out for typos).
        """ 
        if ctx.invoked_subcommand is None:
            question = requests.get(QUIZ_API).text
            question = json.loads(question)
            question = question['results'][0]

            answers = format_answers(question['correct_answer'], question['incorrect_answers'])
            question['answers'] = answers[0]

            embed = Embed()
            embed.type="rich"
            embed.color = Colour.green()
            embed.set_thumbnail(url='https://i.imgur.com/pdcfd7L.jpg')
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
                value=answers[1]
            )

            user_entry = Query()
            user_entry = userdata.get(user_entry.id == ctx.message.author.id)
            userdata.update(
                {'quiz_last_question': json.dumps(question)},
                doc_ids=[user_entry.doc_id]
            )

            await bot.say(None, embed=embed)

    @quiz.command(pass_context=True)
    async def answer(ctx, *, ans):
        user_entry = Query()
        user_entry = userdata.get(user_entry.id == ctx.message.author.id)
        question = user_entry['quiz_last_question']

        if not question:
            await bot.say('Try using "!quiz" first to pick a question')
            return

        question = json.loads(question)

        selected_answer = [x for x in question['answers'] if ans.lower() == x[1].lower() or str(x[0]+1) == ans]
        if len(selected_answer) < 1:
            await bot.say('No such answer.')
        else:
            ans = selected_answer[0]

            if ans[1] == question['correct_answer']:
                await bot.say(':white_check_mark: Correct answer, {}'.format(ctx.message.author.mention))
            else:
                await bot.say(':x: Incorrect answer, {}'.format(ctx.message.author.mention))
                await bot.say('The correct answer was: {}'.format(question['correct_answer']))

            userdata.update(
                {'quiz_last_question': None},
                doc_ids=[user_entry.doc_id]
            )
        
    return quiz
