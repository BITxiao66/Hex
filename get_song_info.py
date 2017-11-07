import requests
from bs4 import BeautifulSoup
import re
import io
import sys
def get_song_info(song_id):
    url='https://music.163.com/song?id='+song_id
    s=requests.get(url)
    name=re.search(r"class=\"f\-ff2\">(.+?)<",s.text)
    singer=re.search(r"href=\"/artist\?id=\d{4,10}\">(.+?)<",s.text)
    album=re.search(r"href=\"/album\?id=\d{4,10}\"\ class=\"s\-fc7\">(.+?)<",s.text)
    right=re.search(r"u-btni u-btni-play u-btni-play-dis",s.text)
    if right==None:
        ownright=1
    else: ownright=0
    print(type(name))
    song_name=name.group(1)
    singer_name=singer.group(1)
    album_name=album.group(1)
    right_info=ownright #版权信息，有版权为1，否则为0；
get_song_info('185699')













