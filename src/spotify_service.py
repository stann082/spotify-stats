import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.scope_builder import ScopeBuilder


class SpotifyService:

    def __init__(self, app_env):
        self.__initialize_spotify(app_env)

    def get_playlist_tracks(self, playlist_id):
        playlist_tracks = []
        items = self.__get_items(self.spotify.playlist_tracks(playlist_id), True)
        for item in items:
            track = item['track']
            album_name = track['album']['name']
            album_release_date = track['album']['release_date']
            artist = track['artists'][0]['name']
            song_name = track['name']
            playlist_tracks.append(f'{artist} - {song_name}; {album_name} ({album_release_date})')
        return playlist_tracks

    def get_playlists(self, playlist_name):
        playlists = []
        items = self.__get_items(self.spotify.current_user_playlists(), True)
        for item in items:
            playlists.append(item)

        if playlist_name is None:
            return list(map(lambda p: f"{p['name']} (Total tracks: {p['tracks']['total']})", playlists))

        matching_playlists = list(filter(lambda x: playlist_name.lower() in x['name'].lower(), playlists))
        if len(matching_playlists) == 0:
            return [f"Could not find any playlists matching {playlist_name}"]

        playlist_info = ""
        for matching_playlist in matching_playlists:
            playlist_info += f"        Name: {matching_playlist['name']}\n"
            playlist_info += f"          Id: {matching_playlist['id']}\n"
            playlist_info += f"         Uri: {matching_playlist['uri']}\n"
            playlist_info += f"Total tracks: {matching_playlist['tracks']['total']}\n\n"
        return [playlist_info]

    def get_recently_played_tracks(self):
        recent_tracks = []
        items = self.__get_items(self.spotify.current_user_recently_played())
        for item in items:
            track = item['track']
            artist = track['artists'][0]['name']
            song_name = track['name']
            recent_tracks.append(f'{artist} - {song_name}')
        return recent_tracks

    def get_top_artists(self, range='medium_term'):
        top_artists = []
        items = self.__get_items(
            self.spotify.current_user_top_artists(time_range=range))
        for item in items:
            top_artists.append(item['name'])
        return top_artists

    def get_top_tracks(self, range='medium_term'):
        top_tracks = []
        items = self.__get_items(
            self.spotify.current_user_top_tracks(time_range=range))
        for item in items:
            artist = item['artists'][0]['name']
            song_name = item['name']
            top_tracks.append(f'{artist} - {song_name}')
        return top_tracks

    def __get_items(self, results, should_get_all_items=False):
        items = results['items']
        if not should_get_all_items:
            return items

        while results['next']:
            results = self.spotify.next(results)
            items.extend(results['items'])
        return items

    def __initialize_spotify(self, app_env):
        scope = ScopeBuilder().build()
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=app_env.client_id,
                                                                 client_secret=app_env.client_secret,
                                                                 redirect_uri=app_env.redirect_uri,
                                                                 scope=scope))
