#!/usr/bin/python

import argparse
import sys

from src.spotify_service import SpotifyService
from src.application_environment import ApplicationEnvironment

# region Helper Methods
def __print_items(items):
    for item in items:
        print(item)
    pass

# region Main Method
def main():
    app_env = ApplicationEnvironment()
    if not app_env.env_vars_are_set():
        print("One of the required environment variables are not set... Check logs for details")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("-ta", "--top-artists", nargs='*', choices=['short_term', 'medium_term', 'long_term'],
                        help="Shows my top artists (optional arguments: short_term, medium_term (default), long_term")
    parser.add_argument("-tr", "--top-tracks", nargs='*', choices=['short_term', 'medium_term', 'long_term'],
                        help="Shows my top tracks (optional arguments: short_term, medium_term (default), long_term")
    parser.add_argument("-rt", "--recent-tracks", nargs='*',
                        help="Shows recently played tracks")
    parser.add_argument("-p", "--playlists", nargs='*',
                        help="Shows user playlists")
    args = parser.parse_args()

    service = SpotifyService(app_env)

    if args.top_tracks is not None:
        range = args.top_tracks[0] if len(args.top_tracks) > 0 else None
        __print_items(service.get_top_tracks(range))
    elif args.top_artists is not None:
        range = args.top_artists[0] if len(args.top_artists) > 0 else None
        __print_items(service.get_top_artists(range))
    elif args.recent_tracks is not None:
        __print_items(service.get_recently_played_tracks())
    elif args.playlists is not None:
        __print_items(service.get_playlists())
    else:
        print("No arguments were provided... Pass -h or --help for more information")
        sys.exit(1)


if __name__ == "__main__":
    main()
