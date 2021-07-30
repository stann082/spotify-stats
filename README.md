# Spotify Stats

An app that utilizes spotipy library to analyze my usage of Spotify

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install spotipy lib.

```bash
pip install spotipy --upgrade
```

## Usage

```python
./main.py --top-tracks # same as passing medium_term argument
./main.py --top-tracks short_term # shows your most listened tracks in last 4 weeks
./main.py --top-tracks medium_term # shows your most listened tracks in last 6 months
./main.py --top-tracks medium_term # shows your most listened tracks of all time

./main.py --top-artists # same as tracks
```
