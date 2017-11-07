import io
import sys
import requests
import re
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


res=requests.get('http://music.163.com/discover/playlist/?cat=%E4%B9%A1%E6%9D%91&order=hot')

p_id = re.compile(r'(?<=playlist\?id=)\d{,9}(?=\" class=\"msk\")')
p_name=re.compile(r'(?<=class=\"tit f-thide s-fc0\">).{,25}(?=<\/a>)')

f1 = open("d:/163music/untitled/header/country_id.txt","w")
f2 = codecs.open("d:/163music/untitled/header/country_name.txt","w","utf-8")

count=0
for m in p_id.findall(res.text):
    print(m)
    count+=1
    f1.write(m+"\n")
print(count)
#f1.write(str(count))
f1.close()

count=0
for m in p_name.findall(res.text):
    print(m)
    count+=1
    f2.write(m+"\n")

print(count)
f2.close()