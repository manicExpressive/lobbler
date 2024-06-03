from django.db import models
from django.contrib.humanize.templatetags import humanize

class Artist(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Release(models.Model):
    name = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=500)
    length = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release = models.ForeignKey(Release, on_delete=models.CASCADE, blank=True, null=True)
    videoId = models.CharField(max_length=90, blank=True, null=True) # source of truth for YouTube Music

    def __str__(self):
        return self.name

class Listen(models.Model):
    created_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    # when we processed this listen
    when = models.DateTimeField(blank=True, null=True)
    # a guess at when it might have happened, mostly for last.fm
    lastfm_when = models.IntegerField(blank=True, null=True)
    played = models.CharField(max_length=100)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    json_from_source = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['when']

    def __str__(self):
        return self.song.name + self.played
