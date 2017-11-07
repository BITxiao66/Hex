# 后端开发记录
-------
> *** 当前版本  v3.0
> * 修改日期 2017年11月7日
> * 修改人 肖子原 许达**

此版本为发布版本，爬虫模块与Server模块完全分离
爬虫模块获取的数据存放在文件中，供Server模块使用
Server模块采用 Flask 架构，前后端间采用 ajax+json模式
本地歌单信息以属性为单位，每一个歌单的各个属性建立一
个文件，爬虫模块负责写文件，Server模块只负责读文件

> **功能摘要
> * 爬去网易云音乐`歌单`和歌曲信息
> * 获取`版权信息`并分析是否可以播放
> * 爬去其他音乐网站同一资源的`URL`**

在本地运行时，使用如下代码以启动Server模块

```python
if __name__ == '__main__':
    f=open("d:/163music/untitled/header/my_list.txt","w")
    f.close()
    app.run(host='0.0.0.0')
```
