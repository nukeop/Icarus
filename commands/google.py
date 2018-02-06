import requests

from bs4 import BeautifulSoup

GOOGLE_URL = 'https://www.google.com/search?q={}'


def google_search(terms):
    page = requests.get(GOOGLE_URL.format(terms.replace(' ', '+'))).text
    soup = BeautifulSoup(page, 'html.parser')
    
    for link in soup.findAll('a'):
        if link.get('href').startswith('/url?q='):
            result = link.get('href')[7:]
            return result[:result.index('&')]
    return None


def create_command(bot):
    @bot.command(pass_context=True, brief='Search for terms on Google')
    async def google(ctx, *, term):
        result = google_search(term)

        await bot.say(result)

    return google
