import json
import requests
import urllib.parse
from lxml import html

DDG_API_URL = "https://api.duckduckgo.com/?q={}&format=json"
DDG_SEARCH_URL = "https://duckduckgo.com/html/"

def ddg_search(term):
    params = {
        'q': term,
        's': '0'
    }
    text = requests.post(DDG_SEARCH_URL, data=params).text
    document = html.fromstring(text)
    
    result = document.cssselect('#links .links_main a')[0].get('href')
    return result

def create_command(bot):

    @bot.command(pass_context=True, brief="Search for terms on DuckDuckGo")
    async def ddg(ctx, *, term):
        """
        lets you search for things on DuckDuckGo. The bot will then return
        the first link it returns and a short definition.
        """
        if '!' in term:
            term = term.replace('!', '')
        
        url = DDG_API_URL.format(urllib.parse.quote(term))
        text = requests.get(url).text
        parsed = json.loads(text)

        abstract = parsed['AbstractText']
        abstracturl = parsed['AbstractURL']

        if abstract == "":
            related = parsed['RelatedTopics']
            relatedstr = ""

            if len(related) < 1:
                await bot.say(ddg_search(term))
                
                #await bot.say("No information about term {}.".format(term))
                return

            for i, entry in enumerate(related):
                try:
                    relatedstr += "({}) {}\n".format(i+1, entry['Text'])
                except KeyError:
                    pass

            await bot.say(relatedstr)
            return

        await bot.say(abstract + '\n' + abstracturl)
