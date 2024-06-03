import json
import time
import os
import requests
from dotenv import load_dotenv

load_dotenv("../../../../.env")  
ROWING_KEY = str(os.getenv('ROWING_KEY'))

from ytmusicapi import YTMusic

# This is currently just a standalone pythong script, but it uses all the stuff
# in the django app's virtualenv so I keep it here.

yt = YTMusic('oauth.json')
likes = yt.get_liked_songs()
likes['tracks'] = likes['tracks'][:10]
timestr = time.strftime("musiclikes-%Y%m%d-%H%M%S") + ".json"
with open(timestr, 'w', encoding='utf-8') as f:
    json.dump(likes, f, ensure_ascii=False, indent=4)


response = requests.get('https://log.concept2.com/api/users/me/results', headers={'Authorization': 'Bearer ' + ROWING_KEY})

timestr = time.strftime("rowing-%Y%m%d-%H%M%S") + ".json"
with open(timestr, 'w', encoding='utf-8') as f:
    json.dump(response.json()['data'][:10], f, ensure_ascii=False, indent=4)
