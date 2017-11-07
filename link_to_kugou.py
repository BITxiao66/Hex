import io
import sys
import requests
import re
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def get_url(songname):
    url1='http://songsearch.kugou.com/song_search_v2?callback=jQuery112405045777256455997_1509628943974&keyword='+songname+'&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1509628943976'
    songlist=requests.get(url1)
    albumid=re.search(r"\"AlbumID\":\"(\d{0,15})\"",songlist.text)
    hash=re.search(r"\"FileHash\":\"(.+?)\"}",songlist.text)
    if albumid==None and hash==None:
        url='null'
    else:
        url = 'http://www.kugou.com/song/#hash=' + hash.group(1) + '&album_id=' + albumid.group(1)
    print(url)

    return url

f1 = open("d:/163music/untitled/header/list_id.txt","r")
line1 = f1.readline()
while line1 !='':
    f2 = codecs.open("d:/163music/untitled/detail/name"+line1[:-1]+".txt","r","utf-8")
    fw = open("d:/163music/untitled/detail/_link" + line1[:-1] + ".txt", "w")
    f_cp=open("d:/163music/untitled/detail/copyrights"+line1[:-1]+".txt","r")
    f_id=open("d:/163music/untitled/detail/id"+line1[:-1]+".txt","r")
    fw.close()

    line2 = f2.readline()
    line_cp = f_cp.readline()
    line_id = f_id.readline()
    while line2 != '':
        if line_cp[:-1] == '1':
            temp = 'http://music.163.com/#/song?id=' +  line_id[:-1]
        else:
            temp = get_url(line2[:-1])
        fw = open("d:/163music/untitled/detail/_link" + line1[:-1] + ".txt", "a")
        fw.write(temp+'\n')
        fw.close()
        line2 = f2.readline()
        line_cp = f_cp.readline()
        line_id = f_id.readline()
    f2.close()
    f_cp.close()
    f_id.close()

    line1 = f1.readline()
f1.close()



