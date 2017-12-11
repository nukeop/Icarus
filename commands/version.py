import subprocess

from config import config

def get_version_hash(subprocess=subprocess):
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8')


def get_long_hash(subprocess=subprocess):
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')


def get_commit_msg(subprocess=subprocess):
    return subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8')


def create_command(bot):

    @bot.command(pass_context=True, brief="Shows version info and changelog")
    async def version(ctx):
        """
        !version shows you the short git hash of the latest commit, as well as
        its commit message. In the future, it might also show the latest
        changelog entries.
        """
        await bot.say("Icarus does not use discrete versioning, it uses the "
        "rolling release model. It is continuously updated from github as "
        "soon as a new commit becomes available.")
        await bot.say(config['repository'] + '/commits/master')
        await bot.say("Version hash: {}".format(get_version_hash()))
        await bot.say("Commit message: {}".format(get_commit_msg()))

    return version
