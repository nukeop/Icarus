import datetime
import requests

from bs4 import BeautifulSoup
from discord import Colour, Embed

CODEX_ROOT = 'https://rpgcodex.net/forums/'
CODEX_RECENT = 'https://rpgcodex.net/forums/index.php?find-new/posts'
CODEX_PROFILE_POSTS = 'http://rpgcodex.net/forums/index.php?find-new/profile-posts'


def embed_thread(thread):
    embed = Embed()
    embed.type = "rich"
    embed.color = Colour.dark_red()
    
    author = thread.get('data-author')
    author_profile = thread.select('.avatarContainer a')[0].get('href')
    avatar = thread.select('.avatarContainer img')[0].get('src')
    
    thread_url = thread.select('.PreviewTooltip')[0].get('href')
    thread_title = thread.select('.PreviewTooltip')[0].get_text()
    
    last_post_date = thread.select('abbr.DateTime')[0].get('data-time')
    last_post_date = datetime.datetime.fromtimestamp(int(last_post_date))
    
    forum = thread.select('.forumLink')[0].get_text()
    
    replies = thread.select('.major dd')[0].get_text()
    views = thread.select('.minor dd')[0].get_text()
    
    last_post_author = thread.select('.lastPostInfo a')[0].get_text()
    
    embed.title = thread_title
    embed.url = CODEX_ROOT + thread_url
    embed.timestamp = last_post_date
    embed.set_author(
        name=author,
        url=CODEX_ROOT + author_profile,
        icon_url=CODEX_ROOT + avatar
    )
    
    embed.add_field(
        name='Forum',
        value=forum
    )
    
    embed.add_field(
        name='Last message',
        value=last_post_author
    )
    
    embed.add_field(
        name='Replies',
        value=replies,
        inline=True
    )
    
    embed.add_field(
        name='Views',
        value=views,
        inline=True
    )

    return embed


def embed_tweet(tweet):
    embed = Embed()
    embed.type = "rich"
    embed.color = Colour.dark_red()

    author = tweet.get('data-author')
    author_profile = tweet.select('.avatar')[0].get('href')
    avatar = tweet.select('.avatar img')[0].get('src')
    
    embed.title = tweet.select('.messageContent blockquote')[0].get_text()
    embed.url = CODEX_ROOT + tweet.select('.privateControls a')[0].get('href')
    embed.timestamp = datetime.datetime.fromtimestamp(int(
        tweet.select('.privateControls abbr')[0].get('data-time')
    ))
    embed.set_author(
        name=author,
        url=CODEX_ROOT + author_profile,
        icon_url=CODEX_ROOT + avatar
    )
    
    return embed
    

def create_command(bot):
    @bot.group(pass_context=True, brief="Shows most recently active RPG Codex "
               "thread")
    async def codex(ctx):
        if ctx.invoked_subcommand is None:
            recent = requests.get(CODEX_RECENT).text
            soup = BeautifulSoup(recent, 'html.parser')
            discussionList = soup.select('.discussionList')[0]
            threads = discussionList.select('li')

            for thread in threads[:1]:
                embed = embed_thread(thread)
                await bot.say(None, embed=embed)

    @codex.command(pass_context=True)
    async def tweets(ctx, num=1):
        tweets = requests.get(CODEX_PROFILE_POSTS).text
        soup = BeautifulSoup(tweets, 'html.parser')
        profilePostList = soup.select('#ProfilePostList')[0]
        posts = profilePostList.select('.primaryContent')

        for tweet in posts[:num]:
            embed = embed_tweet(tweet)
            await bot.say(None, embed=embed)
        
