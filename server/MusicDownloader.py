from youtube_search import YoutubeSearch
import youtube_dl
import time

#--------------------#
# MusicDownloader
# started 22.07.2020
# author mar4elkin
#--------------------#


class MusicDownloader(object):
    def __init__(self, request):
        self.request = request
    
    def findVideo(self):
        ytSearch = YoutubeSearch(self.request, max_results=1).to_dict()[0].get('url_suffix')
        url = 'https://www.youtube.com' + ytSearch
        return url
        
    
    def dnSong(self, links, dirr=''):
        if dirr == '':
            toDir = 'tmp/%(title)s.%(ext)s'
        else:
            toDir = dirr + '/%(title)s.%(ext)s'

        ydl_opts = {
            'outtmpl': toDir,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([links])
        