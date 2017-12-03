SPOOK_URL = "https://github.com/emacs-mirror/emacs/raw/master/etc/spook.lines"

def create_command(bot):

    @bot.command(pass_context=True, brief="Shows words from the emacs spook file.")
    async def nsa(ctx):
        """
        !nsa will show you one term from the spook file. Adding a
        number after the command will show you multiple terms.
        """
        print(db)

    return nsa
