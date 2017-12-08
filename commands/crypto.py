import json
import requests

API = "https://api.coinmarketcap.com/v1/ticker/"
CURRENCY = "usd"


def get_list(requestInterface=requests):
    r = requestInterface.get(API).text
    r = json.loads(r)
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

def get_ticker(symbol, requestInterface=requests):
    r = requestInterface.get(API + symbol).text
    r = json.loads(r)[0]
    msg = ("{} ({}) status:\nPrice (USD): {}\nPrice (BTC): {}\nVolume (USD):"
           "{}\n% change (1h): {}\n% change (24h): {}")

    change_1h = r['percent_change_1h']
    change_24h = r['percent_change_24h']
    
    msg = msg.format(r['name'], r['symbol'], r['price_usd'], r['price_btc'],
                     r['24h_volume_usd'], add_chart_emoji(change_1h),
                     add_chart_emoji(change_24h))
    
    return msg


def create_command(bot):
    
    @bot.command(pass_context=True, brief="Shows cryptocurrency prices", help=generate_help_string())
    async def crypto(ctx, *, symbol):
        await bot.say(get_ticker(symbol))