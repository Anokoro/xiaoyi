# -*- coding:utf-8 -*-
# author：岳昊玮
# date  ：2019/6/6  
# time  : 11:47   
# IDE   : PyCharm
# description :


# 我们在操作电脑时，经常会需要操作电脑上的文件/文件夹
# 现在我们来学一学怎么用python来批量地操作文件
# 我们把上节课通过爬虫爬取到的内容存到我们电脑上的一个文件里面
#

from bs4 import BeautifulSoup as Soup
import requests

# 大家平时一定都喜欢看书，今天我们就来一起来爬一爬豆瓣top250的图书
url = 'https://book.douban.com/top250?start=0'
r = requests.get(url)
html_code = r.text
soup = Soup(html_code, "html.parser")
all_book = soup.find_all('table')
count = 0
# 首先我们先将上节课爬到的内容记录到一个字典变量里面
books = {}
for book in all_book[1:]:
    count = count + 1
    # print('{:*^30}'.format('book',count))
    # print(book.div.a['title'])
    # print(book.p.string)
    # print(book.find(name='span', attrs={'class': 'inq'}).string)
    title = book.div.a['title']
    content = book.p.string
    intro = book.find(name='span', attrs={'class': 'inq'}).string
    books[title] = {'content':content, 'intro':intro}  # 记录下来

# 输出看一下这个字典
print(books)
# 通过以上代码，我们爬取到25本书的信息
# file =  open('book.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 'book.txt'
# 上面代码报错，是因为我们电脑里面没有这个文件
# 加一个参数’w‘ 表示写文件，这样python在发现文件不存在的时候，就会帮助我们新建一个
file =  open('book.txt','w')
# 看一下我们当前的目录下面是不是多了一个book.txt文件

# 接下来把我们爬到的东西存到文件里面去
# 用for循环来一本一本写，items函数就是每次取出一本书
for title, content in books.items():
    # format 不只是可以用来print，
    # 它主要的作用是帮助我们来把一个字符串格式化，把一个一个零散的信息组装到一起
    str= 'title:{}\ncontent:{} \nintro:{} \n'.format(title, content['content'], content['intro'])
    # 用write函数
    file.write(str)
    # 看一下我们的文件里面是不是已经存了下来
# 文件操作完了一定要记得关掉文件，这是一个良好的习惯
file.close()

# 但是很多时候我们容易忘掉关闭文件，没关系，python也知道我们会忘
# 所以提供给了我们一个更好的方式 with 语句
# 我们可以在with里面使用文件，当出了with语句范围之后，文件就会自动关闭
# 我们下面用这种方法来读取一下刚刚写进去的内容  把打开模式改成’r‘，表示read
with open('book.txt','r') as file:
    # 用read函数
    content = file.read()
    # content = file.readlines()  # 返回一个list,每一行是一个元素
    print(content)


# ***********************DONE