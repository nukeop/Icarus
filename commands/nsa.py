import random
import requests

SPOOK_URL = "https://github.com/emacs-mirror/emacs/raw/master/etc/spook.lines"

def create_command(bot):

    def init_words():
        words = requests.get(SPOOK_URL).text
        words = words.split('\x00')[1:]
        
        return words

    def get_words(words, num=1):
        return ' '.join([random.choice(words).strip() for _ in
                         range(num)])

    words = init_words()
    
    
    @bot.command(pass_context=True, brief="Shows words from the emacs spook file.")
    async def nsa(ctx, num=1):
        """
        !nsa will show you one term from the spook file. Adding a
        number after the command will show you multiple terms.
        """
        await bot.say(get_words(words, num))

    return nsa
