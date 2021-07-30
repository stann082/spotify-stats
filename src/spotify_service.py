import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.scope_builder import ScopeBuilder


class SpotifyService:

    # Constructors
    def __init__(self, app_env):
        self.__initialize_spotify(app_env)

    # region Public Methods
    def get_playlists(self):
        pass

    def get_recently_played_tracks(self):
        playlists = []
        user_playlists = self.spotify.current_user_playlists()
        # for items in enumerate(top_artists['items']):
        #     track = items[1]['track']
        #     artist = track['artists'][0]['name']
        #     song_name = track['name']
        #     recent_tracks.append(f'{artist} - {song_name}')
        return playlists

    def get_top_artists(self, range='medium_term'):
        artists = []
        top_artists = self.spotify.current_user_top_artists(time_range=range)
        for items in enumerate(top_artists['items']):
            artists.append(items[1]['name'])
        return artists

    def get_top_tracks(self, range='medium_term'):
        artist_song_name = []
        top_tracks = self.spotify.current_user_top_tracks(time_range=range)
        for items in enumerate(top_tracks['items']):
            item = items[1]
            artist = item['artists'][0]['name']
            song_name = item['name']
            artist_song_name.append(f'{artist} - {song_name}')
        return artist_song_name

    # region Helper Methods
    def __initialize_spotify(self, app_env):
        scope = ScopeBuilder().build()
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=app_env.client_id,
                                                                 client_secret=app_env.client_secret,
                                                                 redirect_uri=app_env.redirect_uri,
                                                                 scope=scope))
