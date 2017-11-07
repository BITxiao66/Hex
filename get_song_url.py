import requests
from bs4 import BeautifulSoup
import re
import io
import sys

def get_url(songname):
    url1='http://songsearch.kugou.com/song_search_v2?callback=jQuery112405045777256455997_1509628943974&keyword='+songname+'&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1509628943976'
    songlist=requests.get(url1)
    albumid=re.search(r"\"AlbumID\":\"(.+?)\"",songlist.text)
    hash=re.search(r"\"FileHash\":\"(.+?)\"}",songlist.text)

    url='http://www.kugou.com/song/#hash='+hash.group(1)+'&album_id='+albumid.group(1)
    print(url)





