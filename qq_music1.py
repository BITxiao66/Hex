import io
import sys
import requests
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
res=requests.get('http://music.163.com/discover/playlist/?cat=%E4%B9%A1%E6%9D%91')
#print(res.text)


p = re.compile(r'(?<=playlist\?id=)\d{9}(?=\" class=\"msk\")')

f1 = open("d:/163music/country_num.txt","w")
count=0
for m in p.findall(res.text):
    print(m)
    count+=1
    #f1.write(m+"\n")
print(count)
f1.write(str(count))
f1.close()
