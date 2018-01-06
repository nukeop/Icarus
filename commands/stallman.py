import datetime
import requests

from bs4 import BeautifulSoup
from discord import Colour, Embed
from html.parser import HTMLParser

RSS = 'https://stallman.org/rss/rss.xml'
WEBSITE = 'https://stallman.org/'
PHOTO = "https://stallman.org/rms-icon.jpg"

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def embed_note(note):
    embed = Embed()
    embed.type = "rich"
    embed.color = Colour.blue()

    desc = ""
    for tag in note.select('description')[0].recursiveChildGenerator():
        desc += tag
    date = note.select('pubdate')[0].get_text()
    date = datetime.datetime.strptime(date, "%d %b %Y %H:%M:%S %z")
    
    embed.title = note.select('title')[0].get_text()
    embed.url = note.select('link')[0].get_text()
    embed.description = strip_tags(desc)
    embed.timestamp = date
    embed.set_author(
        name=note.find('dc:creator').get_text(),
        url=WEBSITE,
        icon_url=PHOTO
    )

    return embed

def get_note(notes):
    soup = BeautifulSoup(notes, 'lxml')
    items = soup.find_all('item')

    return embed_note(items[0])

def create_command(bot):
    @bot.command(pass_context=True, brief="Shows Richard Stallman's recent political notes")
    async def stallman(ctx):
        notes = requests.get(RSS).text
        await bot.say(None, embed=get_note(notes))
