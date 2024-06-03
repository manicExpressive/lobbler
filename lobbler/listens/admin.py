from django.contrib import admin

# Register your models here.
from .models import Artist, Release, Song, Listen


class SongInline(admin.TabularInline):
    model = Song

class ReleaseInline(admin.TabularInline):
    model = Release

class ArtistAdmin(admin.ModelAdmin):
    inlines = [
        SongInline,
        ReleaseInline
    ]
    list_display = ('name', 'get_song_count')

    @admin.display(description='Song Count', ordering='song__count')
    def get_song_count(self, obj):
        return Song.objects.filter(artist=obj).count()

class ReleaseAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

class ListenAdmin(admin.ModelAdmin):
    readonly_fields = ["created_date"]
    model = Listen
    list_display = ('get_song_name', 'get_artist_name', 'played', 'created_date')

    @admin.display(description='Song Name', ordering='song__name')
    def get_song_name(self, obj):
        return obj.song.name

    @admin.display(description='Artist Name', ordering='artist__name')
    def get_artist_name(self, obj):
        return obj.song.artist.name

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Listen, ListenAdmin)
