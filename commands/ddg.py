import json
import requests

DDG_API_URL = "https://api.duckduckgo.com/?q={}&format=json"

def create_command(bot):

    @bot.command(pass_context=True, brief="Search for terms on DuckDuckGo")
    async def ddg(ctx, *, term):
        """
        !ddg lets you search for things on DuckDuckGo. The bot will then return
        the first link it returns and a short definition.
        """
        url = DDG_API_URL.format(term)
        text = requests.get(url).text
        parsed = json.loads(text)

        abstract = parsed['AbstractText']
        abstracturl = parsed['AbstractURL']

        if abstract == "":
            related = parsed['RelatedTopics']
            relatedstr = ""

            if len(related) < 1:
                await bot.say("No information about term {}.".format(term))
                return

            for i, entry in enumerate(related):
                try:
                    relatedstr += "({}) {}\n".format(i+1, entry['Text'])
                except KeyError:
                    pass

            await bot.say(relatedstr)
            return

        await bot.say(abstract + '\n' + abstracturl)
