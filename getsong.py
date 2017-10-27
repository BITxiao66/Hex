import io
import sys
import requests
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

tmp_str="，"
p = re.compile(r'(?<=song\?id=)\d{1,9}')
p1 =re.compile(r'name=\"keywords\" content=\"')

f = open("d:/163music/test.txt","w")
f.close()

f1 = open("d:/163music/test.txt","a")
count=0
#print(str(res.text))
for line in {"963463438"}:#"964072485"}:}:
    res = requests.get("http://music.163.com/playlist?id="+line)
    for m in p.findall(res.text):
        count+=1
        f1.write(m+"\n")
    print(count)
    f1.write("\n"+"\n"+"\n"+"\n")
f1.close()
