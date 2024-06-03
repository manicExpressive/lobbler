import json
import time
from ytmusicapi import YTMusic

# This is currently just a standalone pythong script, but it uses all the stuff
# in the django app's virtualenv so I keep it here.

yt = YTMusic('oauth.json')
listens = yt.get_liked_songs()
timestr = time.strftime("%Y%m%d-%H%M%S") + ".json"
with open(timestr, 'w', encoding='utf-8') as f:
    json.dump(listens, f, ensure_ascii=False, indent=4)
