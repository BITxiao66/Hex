import io
import sys
import requests
import re
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def fun7():
    info = dict()
    list_name = list()
    list_id = list()
    f1 = open("d:/163music/untitled/header/folk_id.txt","r")
    f2 = codecs.open("d:/163music/untitled/header/folk_name.txt","r","utf-8")
    line1 = f1.readline()
    line2 = f2.readline()
    count = 0
    while line1:
        count+=1
        list_id.append(line1[:-1])
        list_name.append(line2[:-1])
        line1 = f1.readline()
        line2 = f2.readline()
    f1.close()
    f2.close()
    info['count'] = count
    info['list_id'] = list_id
    info['list_name'] = list_name
    return info

print(fun7())