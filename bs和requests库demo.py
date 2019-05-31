# -*- coding:utf-8 -*-
# author：岳昊玮
# date  ：2019/5/31  
# time  : 10:40   
# IDE   : PyCharm
# description :

# 今天要给大家讲解的是BeautifulSoup库，这节课我来给大家演示如何用做汤的办法来做爬虫
from bs4 import BeautifulSoup as Soup
import requests

# 大家平时一定都喜欢看书，今天我们就来一起来爬一爬豆瓣top250的图书
url = 'https://book.douban.com/top250?start=0'   # 如果想爬取更多，直接把start按照25的步长就可以实现翻页功能了
# 获取服务器返回响应,,服务器根据我们是否访问成功给我们返回一个代号
r = requests.get(url)
# print(r) # 代号200说明成功响应  404问题大家一定都见过吧
# 获取html代码 它现在只是一个字符串，和普通的一段文字没有任何区别
# 这一步我们获取到了做汤的原材料
html_code = r.text
# print(type(html_code))  # 输出：<class 'str'>

# 接下来我们把它做成一锅汤
# Soup函数就是我们帮助我们把原材料转换成汤的机器，
# 我们把html代码作为原材料喂进去，他就会帮我们把它做成一锅美味的汤
# html.parser 就是这个机器的做汤说明书
# html_code 就是我们刚刚拿到的原材料
soup = Soup(html_code, "html.parser")
# print(type(soup)) # 输出：<class 'bs4.BeautifulSoup'>

# 然后我们来看一看这锅汤，，
# print(soup)   # 代码没有缩进
# 我们来将这锅汤更好看点，使用prettify()格式化显示输出
# print(soup.prettify())  # 有缩进

# 至此，我们就已经做好了一锅汤
#####################################
# 接下来，我们来一起看看这锅汤里都有什么配料，一个一个来看

# 首先我们来看看这锅汤的名字叫什么
# print(soup.title)  # 输出：<title>豆瓣图书 Top 250</title>
# 可以看到上面的输出还给内容带了标签，这不是我们想要的结果，我们只想要里面的内容，
# print(soup.title.string)  # 输出：豆瓣图书 Top 250
# 同样，如果我们想获取标签的名字
# print(soup.title.name)  # 输出：title

# 一些额外的例子
# print(soup.a)  # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
# print(soup.a.name)   # 获取a标签的名字
# print(soup.a.parent.name)   # a标签的父标签(上一级标签)的名字
# print(soup.a.parent.parent.name)  # a标签的父标签的父标签的名字

# 接下来我们来看看怎么拿出我们想要的书
# 回头去Chrome F12开发者模式定位代码  见PPT demo
# 定位完之后，回来继续写代码
# 我们先来找到所有的<table>标签
all_book = soup.find_all('table')
# print(all_book) # 是一个list列表
# 我们来看看一共返回了多少本书
# print(len(all_book))   # 输出26本 一页显示25本书，为什么会长26呢？说明其他地方还有一个表格
# print(all_book[0].prettify())  # 这是一个非书籍的表格，要忽略掉
# 下面我们来一本一本地解析 不需要再去浏览器中定位  直接打印出第一个来看就好
#
# print(all_book[1].prettify())
# 首先定位到书名，发现它是在第一个<div>标签里面，再下一级是一个<a>标签，标签里面有个属性title，里面就是我们要的书名
# （注：这里之所以不用string属性，是因为豆瓣网站本身的问题，导致这个方法并不通用，比如三体这本书用string就获取不到string）
# print(all_book[1].div.a['title]) # 输出：追风筝的人
# 接下来我们想要更多的信息，比如作者、出版社、价格、等等等等，继续来分析html代码 （见PPT截图）
# 这里我们看到它也是在div里面的，但是同时也是第一个p标签，所以我们可以直接写p
# print(all_book[1].p.string.strip()) # 输出：[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元


# 接下来我们看看如何获得简介，这一步就比较难了，大家注意
# 继续看html代码，发现它被span包着，但是它并不是第一个span,

# 而我们之前的方法只能找到第一个span,如下代码。
# print(all_book[1].span.string) # 输出：The Kite Runner

# 所以我们之前的方法就失效了，那么我们就需要新的办法去定位它
# print(all_book[1].find(name='span',attrs={'class':'inq'}).string) #输出：为你，千千万万遍

# 接下来我们就来分析定位所有的25本书,用我们学过的for循环
# 来加一个计数器
count = 0
for book in all_book[1:]:
    count = count + 1
    print('********** book',count,'***********') # 先这样写吧，下节课再教格式化输出
    print(book.div.a['title'])
    print(book.p.string)
    print(book.find(name='span', attrs={'class': 'inq'}).string)

# 后面实践课程涉及到其他定位标签的方式，比如id什么的咨询助教同学吧