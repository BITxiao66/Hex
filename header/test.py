import io
import sys
import requests
import re
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def fun10():
    info = dict()
    list_name = list()
    my_list_id = list()
    f1 = open("d:/163music/untitled/header/my_list.txt","r")
    line1=f1.readline()
    count = 0
    while line1 !='':
        count+=1
        f2 = open("d:/163music/untitled/header/list_id.txt","r")
        line2=f2.readline()
        index=0;
        while line2 !='':
            if line2[:-1] == line1[:-1]:
                break
            line2=f2.readline()
            index+=1
        f2.close()

        f3 = codecs.open("d:/163music/untitled/header/list_name.txt","r","utf-8")
        line3 = f3.readline()
        while index > 0:
            line3 = f3.readline()
            index-=1
        f3.close()

        list_name.append(line3)
        my_list_id.append(line1)

        line1 = f1.readline()

    f1.close()

    info['count'] = count
    info['list_id'] = my_list_id
    info['list_name'] = list_name
    return info

obj=fun10()

print(obj[''])
