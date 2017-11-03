import io
import sys
import requests
import re
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def get_song_info(song_id,local_list_id):
    url='https://music.163.com/song?id='+song_id
    s=requests.get(url)
    name=re.search(r"class=\"f\-ff2\">(.+?)<",s.text)
    singer=re.search(r"href=\"/artist\?id=\d{4,10}\">(.+?)<",s.text)
    album=re.search(r"href=\"/album\?id=\d{4,10}\"\ class=\"s\-fc7\">(.+?)<",s.text)
    right=re.search(r"u-btni u-btni-play u-btni-play-dis",s.text)
    if right==None:
        ownright=1
    else: ownright=0
    song_name=name.group(1)
    singer_name=singer.group(1)
    album_name=album.group(1)
    right_info=ownright #版权信息，有版权为1，否则为0；

    fa_name=codecs.open("d:/163music/untitled/detail/name"+local_list_id+".txt","a","utf-8")
    fa_name.write(song_name+"\n")
    fa_name.close()

    fa_singer=codecs.open("d:/163music/untitled/detail/singer"+local_list_id+".txt","a","utf-8")
    fa_singer.write(singer_name+"\n")
    fa_singer.close()

    fa_album=codecs.open("d:/163music/untitled/detail/album"+local_list_id+".txt","a","utf-8")
    fa_album.write(album_name+"\n")
    fa_album.close()

    fa_copyrights=open("d:/163music/untitled/detail/copyrights"+local_list_id+".txt","a")
    fa_copyrights.write(str(right_info)+"\n")
    fa_copyrights.close()

def get_song_id():
    f_r = open("d:/163music/untitled/header/folk_id.txt","r")
    p_id = re.compile(r'(?<=href=\"/song\?id=)\d{1,10}')
    line = f_r.readline()
    while line:
        res=requests.get('http://music.163.com/playlist?id='+line[:-1])
        count=0
        f_id=open("d:/163music/untitled/detail/id"+line[:-1]+".txt","w")
        for m in p_id.findall(res.text):
            print(m)
            count+=1
            f_id.write(m+"\n")
        f_id.close()
        line = f_r.readline()
        print(count)
    f_r.close()

def file_clear(local_list_id):
    fa_name = open("d:/163music/untitled/detail/name" + local_list_id + ".txt", "w")
    fa_name.close()

    fa_singer = open("d:/163music/untitled/detail/singer" + local_list_id + ".txt", "w")
    fa_singer.close()

    fa_album = open("d:/163music/untitled/detail/album" + local_list_id + ".txt", "w")
    fa_album.close()

    fa_copyrights = open("d:/163music/untitled/detail/copyrights" + local_list_id + ".txt", "w")
    fa_copyrights.close()

f_r1=open("d:/163music/untitled/header/folk_id.txt","r")
row_list = f_r1.readline()
while row_list[:-1].isalnum():

    file_clear(row_list[:-1])
    f_r2 = open("d:/163music/untitled/detail/id"+row_list[:-1]+".txt","r")

    row_song = f_r2.readline()
    while row_song[:-1].isalnum():
        get_song_info(row_song[:-1],row_list[:-1])
        row_song = f_r2.readline()

    f_r2.close()
    row_list = f_r1.readline()
f_r1.close()
