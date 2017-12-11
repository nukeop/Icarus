from github import Github
import logging
from config import config
from commands.version import get_long_hash

log = logging.getLogger(__name__)
gh = Github(config['github_token'])

def check_for_updates():
    full_name = '/'.join(config['repository'].split('/')[-2:])
    repo = gh.get_repo(full_name)
    newest_hash = repo.get_commits()[0].sha
    current_hash = get_long_hash()
    if newest_hash != current_hash:
        log.info("Bot outdated, update needed")
