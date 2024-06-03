import json
import time
from ytmusicapi import YTMusic

# This is currently just a standalone pythong script, but it uses all the stuff
# in the django app's virtualenv so I keep it here.

yt = YTMusic('oauth.json')
likes = yt.get_liked_songs()
likes['tracks'] = likes['tracks'][:10]
timestr = time.strftime("%Y%m%d-%H%M%S") + ".json"
with open(timestr, 'w', encoding='utf-8') as f:
    json.dump(likes, f, ensure_ascii=False, indent=4)
