import pytest
import sys, os
import shutil
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from server.MusicDownloader import MusicDownloader

md = MusicDownloader('Slipknot - All Out Life [OFFICIAL VIDEO]')

def setup_module(module):
    pass

def teardown_module(module):
    shutil.rmtree('test_tmp')

def test_findVideo():
    songurl = md.findVideo()
    assert 'https://www.youtube.com/watch?v=wLoYIBEZEfw' == songurl

def test_dnSong():
    md.dnSong(md.findVideo(), 'test_tmp')
    assert os.path.isfile('test_tmp/Slipknot - All Out Life [OFFICIAL VIDEO].mp3')

