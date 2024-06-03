from datetime import datetime
import json
from ytmusicapi import YTMusic
import time
import pytz

from django.core.management.base import BaseCommand #, CommandError
from listens.models import Listen, Artist, Song, Release


class Command(BaseCommand):
    help = "Gets listens from YouTube Music"


    def handle(self, *args, **options):
        tz_local = pytz.timezone('America/Los_Angeles')
        count = 0
        # for comparison to see what we have
        yt = YTMusic('oauth.json')
        listens = yt.get_history()
        listens.reverse()

        for listen in listens:
            if (listen['played'] == 'Yesterday'):
                print(listen['title'])

            artist, artist_created = Artist.objects.get_or_create(name=listen['artists'][0]['name'])

            if listen['album']:
                release, album_created = Release.objects.get_or_create(artist=artist, name=listen['album']['name'])
                song, song_created = Song.objects.get_or_create(
                    name=listen['title'],
                    artist=artist,
                    length=listen['duration_seconds'],
                    videoId=listen['videoId'],
                    release=release
                )
            else:
                song, song_created = Song.objects.get_or_create(
                    name=listen['title'],
                    videoId=listen['videoId'],
                    length=listen['duration_seconds'],
                    artist=artist
                )


            if listen['played'] == 'Yesterday':
                this_listen = Listen(song=song, played=listen['played'], when=datetime.now(tz=tz_local), json_from_source=str(listen))
                this_listen.save()
