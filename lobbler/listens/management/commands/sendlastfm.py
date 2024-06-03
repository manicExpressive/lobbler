import datetime
import json
import time
import pytz
import pylast
from django.core.management.base import BaseCommand #, CommandError
from listens.models import Listen, Artist, Song, Release

# importing these for future use, auth is handled via the session code below
import os
API_KEY = str(os.getenv('API_KEY'))
API_SECRET = str(os.getenv('API_SECRET'))

# Lifted from the pylast docs entirely, works great
SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")
network = pylast.LastFMNetwork(API_KEY, API_SECRET)
if not os.path.exists(SESSION_KEY_FILE):
    skg = pylast.SessionKeyGenerator(network)
    url = skg.get_web_auth_url()

    print(f"Please authorize this script to access your account: {url}\n")
    import time
    import webbrowser

    webbrowser.open(url)

    while True:
        try:
            session_key = skg.get_web_auth_session_key(url)
            with open(SESSION_KEY_FILE, "w") as f:
                f.write(session_key)
            break
        except pylast.WSError:
            time.sleep(1)
else:
    session_key = open(SESSION_KEY_FILE).read()

network.session_key = session_key
class Command(BaseCommand):
    help = "Gets listens from YouTube Music"


    def handle(self, *args, **options):
        listens_to_send = Listen.objects.filter(lastfm_when__isnull=True, played="Yesterday")
        today = datetime.date.today()
        # Last.fm likes unix epocs for timestamps, so we pull the epoc for noon my time
        # and then we use that to build times for the plays of each song, which YT Music doesn't provide
        yesterday_epoc = (today - datetime.timedelta(hours=24)).strftime("%s")
        yesterday_epoc = int(yesterday_epoc) + 50000
        print(type(yesterday_epoc))

        listens_to_send.reverse()

        for listen in listens_to_send:
            # set a lastfm time - last lastfm time + this songs length?
            listen.lastfm_when = int(yesterday_epoc) + listen.song.length
            yesterday_epoc = listen.lastfm_when

            last_lastfm_time = listen.lastfm_when
            listen.save()
            if listen.lastfm_when:
                print("Heard: %s" % listen.song.name)
                print("at: %s" % listen.lastfm_when)
            else:
                print("DIdn't hear somehow: %s" % listen.song.name)
            # store this as unix thing so I don't have to convert later
            if network and listen.lastfm_when:
            #    # send to lastfm
                response = network.scrobble(artist=listen.song.artist.name, title=listen.song.name, timestamp=listen.lastfm_when)
            #
                print('got em: %s' % response)
