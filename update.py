from github import Github
import logging
import subprocess

from config import config
from commands.version import get_long_hash, get_version_hash

log = logging.getLogger(__name__)
gh = Github(config['github_token'])


def get_full_repo_name():
    return '/'.join(config['repository'].split('/')[-2:])


def check_for_updates():
    repo = gh.get_repo(get_full_repo_name())
    newest_hash = repo.get_commits()[0].sha.strip()
    current_hash = get_long_hash().strip()

    if newest_hash != current_hash:
        return True

    return False


def after_update_message():
    repo = gh.get_repo(get_full_repo_name())
    msg = ['Update downloaded and applied.']

    current_hash = get_version_hash()
    msg.append('New version: {}'.format(current_hash))

    newest_commit = repo.get_commits()[0]
    msg.append('Committed by {} on {}'.format(newest_commit.author.login,
                                              newest_commit.commit.last_modified))
    msg.append(newest_commit.commit.message)

    return msg


async def send_after_update_message(bot, channel):
    for line in after_update_message():
        await bot.send_message(channel, line)


def autoupdate():
    subprocess.run(['chmod', '+x', 'update.sh'])
    subprocess.run(['./update.sh'])
