# scrapyNews 热点新闻爬取
这是高彦杰和倪亚宇《Spark大数据分析实战》(Spark Big Data Analytics）中第七章热点新闻分析系统的数据采集部分。
这本书是学习spark非常好的材料，而利用scrapy构建爬虫采集新闻是相对独立的模块。利用这些代码，你可以很快的进入后续的学习。
我对书中的代码做了些许修改，以符合scrapy最新的版本。

为了使用本程序，你需要做如下几步：

1.scrapy相关:
我使用的是scrapy1.1版本
scrapy1.1下载链接：http://scrapy.org/download/
scrapy中文文档：http://scrapy.org/download/

2.mongoDB相关:
python中操作mongoDB的库pymongo下载方法：http://api.mongodb.com/python/current/installation.html
mongoDB下载链接：https://www.mongodb.com/download-center?jmp=nav#community

3.如果是linux系统 通过输入 scrapy crawl nYtimes 启动

另外本代码采集的网站需要翻墙。



