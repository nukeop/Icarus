import json
import requests

API = "https://api.cryptonator.com/api/ticker/{}-{}"
CURRENCY = "usd"

def create_command(bot):

    def get_price(symbol):
        data = requests.get(API.format(symbol, CURRENCY)).text
        data = json.loads(data)
        if data.get('error'):
            return 'Error fetching data for symbol {}, it might not exist'.format(symbol)
        else:
            message = "Current price of {}: {} USD".format(symbol, round(float(data['ticker']['price']), 2))
            change = data['ticker']['change']
            change = round(float(change), 2)
            if change > 0:
                change = '+' + str(change)
                change += ' USD :chart_with_upwards_trend:'
            else:
                change = str(change)
                change += ' USD :chart_with_downwards_trend:'
                                                            
            return message + ' ({})'.format(change)
    
    @bot.command(pass_context=True, brief="Shows cryptocurrency prices")
    async def crypto(ctx, *, symbol):
        """
        !crypto <symbol> will show you current prices (in US dollars) of
        various cryptocurrencies. Use BTC for bitcoin, ETH for Ethereum, and so
        on. a complete list of valid symbols can be found here:
        https://www.cryptonator.com/api/currencies
        """
        await bot.say(get_price(symbol))
