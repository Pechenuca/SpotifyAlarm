import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from server.SpotifyParser import SpotifyParser

sp = SpotifyParser('1Fz9Jggqk3q7D4bT99ONLz?si=04koqXY4RGy6vjVXnIAcEw')

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_getSongs(): 
    spotifySongsArray = sp.getSongs()
    songs = ['Reset - Dj Mad Dog', 'Drop The Deal - TNT,                 Technoboy,                 Tuneboy', 'Primal Energy (Defqon.1 2020 Anthem) - D-Block & S-te-Fan', 'Fine Day - Coone,                 Brennan Heart', 'Sick Of It All - Nosferatu,                 Evil Activities', 'Freedom of Expression - Dark Acid Mix - A*S*Y*S,                 Kai Tracid,                 Tom Wax', 'There Is Something Evil Here - DJ Traumatic', 'Lose My Mind - Radio Edit - Wildstylez,                 Brennan Heart', 'Dungeon - Gydra', 'Get It Lit - Angerfist,                 Miss K8']
    if spotifySongsArray[1] == 1:
        assert songs == spotifySongsArray[0]
    else:
        assert 0 == spotifySongsArray[1]

def test_statusCode():
    assert sp.statusCode() == 200 or 404
