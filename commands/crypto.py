import datetime
import json
import requests

from discord import Colour, Embed
from Levenshtein import distance


API = "https://api.coinmarketcap.com/v1/ticker/"
CURRENCY = "usd"

def get_list_raw(requestInterface=requests):
    r = requestInterface.get(API).text
    r = json.loads(r)
    return r


def get_list(requestInterface=requests):
    r = get_list_raw(requestInterface)
    r = ', '.join([x['id'] for x in r])
    return r


def generate_help_string():
    help = "\
Shows you current prices (in US dollars) of \
various cryptocurrencies. Use BTC for bitcoin, ETH for Ethereum, and so \
on. \
\
Here's a complete list of all supported currencies: \
    "

    help += get_list()
    return help

def add_chart_emoji(change):
    return change + (' :chart_with_upwards_trend:' if float(change)
                     > 0 else ' :chart_with_downwards_trend:')

def embed_crypto(c):
    embed = Embed()
    embed.type = "rich"
    embed.title = "{} ({}) status:".format(c['name'], c['symbol'])
    embed.url = "https://coinmarketcap.com/currencies/" + c['name']
    embed.timestamp = datetime.datetime.fromtimestamp(int(c['last_updated']))

    embed.add_field(
        name='Price (USD)',
        value=c['price_usd']
    )

    embed.add_field(
        name='Price (BTC)',
        value=c['price_btc']
    )

    embed.add_field(
        name='Volume (USD)',
        value=c['24h_volume_usd']
    )

    embed.add_field(
        name='% change (1h)',
        value=add_chart_emoji(c['percent_change_1h'])
    )

    embed.add_field(
        name='% change (24h)',
        value=add_chart_emoji(c['percent_change_24h'])
    )

    embed.set_footer(
        text='Cryptocurrency prices powered by CoinMarketCap'
    )

    return embed

def get_ticker(symbol, requestInterface=requests):
    r = requestInterface.get(API + symbol).text
    r = json.loads(r)

    if 'error' in r:
        rawlist = get_list_raw()
        symbols = [x['symbol'] for x in rawlist]
        if symbol.upper() in symbols:
            for entry in rawlist:
                if entry['symbol'] == symbol.upper():
                    r = [entry]
                    break
        else:
            l = [x.strip() for x in get_list().split(',')]
            distances = [distance(x, symbol) for x in l]
            index = distances.index(min(distances))
            r = requestInterface.get(API + l[index]).text
            r = json.loads(r)

    return r[0]
    # msg = ("{} ({}) status:\nPrice (USD): {}\nPrice (BTC): {}\nVolume (USD):"
    #        "{}\n% change (1h): {}\n% change (24h): {}")

    # change_1h = r['percent_change_1h']
    # change_24h = r['percent_change_24h']
    
    # msg = msg.format(r['name'], r['symbol'], r['price_usd'], r['price_btc'],
    #                  r['24h_volume_usd'], add_chart_emoji(change_1h),
    #                  add_chart_emoji(change_24h))
    
    # return msg


def create_command(bot):
    
    @bot.command(pass_context=True, brief="Shows cryptocurrency prices", help=generate_help_string())
    async def crypto(ctx, *, symbol):
        embed = embed_crypto(get_ticker(symbol))
        embed.color = Colour.gold()
        await bot.say(None, embed=embed)

    return crypto
