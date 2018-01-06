import requests
from config import config

API = "https://discordbots.org/api/bots/{}/stats"

def update_server_count(user_id, count):
    payload = {"server_count": count}
    headers = {"Authorization": config['discord_bot_list_api_key']}
    s = requests.post(
        API.format(user_id),
        data=payload,
        headers=headers
    ).text
