import json
import requests


UD_API= "http://api.urbandictionary.com/v0/define?term={}"
NO_RESULTS= "no_results"
RESULT_EXACT="exact"


def generate_help_string():
    help= "Shows definition from Urban Dictionary"

def get_meaning(phrase):
    url = UD_API.format(phrase)
    text = requests.get(url).text
    parsed = json.loads(text)

    if parsed["result_type"] == NO_RESULTS:
        return "Term {} not found.".format(phrase)

    if parsed["result_type"] == RESULT_EXACT:
        num = 1
        msg = ""
        for i, entry in enumerate(parsed["list"]):
            if i < num:
                msg += "{}\n".format(entry['definition']
                )
            else:
                break
       # msg="Definition of {}:{}".format(phrase, parsed["list"]["definition"][1])
        return msg

    

def create_command(bot):
    @bot.command(pass_context = True, brief="UD search", help= generate_help_string())
    async def ud(ctx, *, phrase):
        await bot.say(get_meaning(phrase))
