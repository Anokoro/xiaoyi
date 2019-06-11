# -*- coding:utf-8 -*-
# author：岳昊玮
# date  ：2019/6/6  
# time  : 11:47   
# IDE   : PyCharm
# description :
# 爬取豆瓣书评，存到文件里面，并调用词云分析程序做成词云图

from bs4 import BeautifulSoup as Soup
import requests

# 这里以《平凡的世界》为例
book_name = '平凡的世界'
ID = '1084165' # 图书ID，可以在豆瓣上搜索该图书，然后在网址里面会看到对应的ID
limit = 1000  # 爬取前N条热门评论,

# 第一步：爬取评论
# 因为每一页只能爬取20条，所以我们用循环来模拟翻页
all_comments = []
for page in range(1,limit//20):  # 一页显示20条评论，
    # 用我们的学过的format来拼装URL
    print('正在爬取第{}页'.format(page))
    url = 'https://book.douban.com/subject/{}/comments/hot?p={}'.format(ID,page)
    r = requests.get(url)
    html_code = r.text
    soup = Soup(html_code, "html.parser")
    comments = soup.find(id='comments')  # 根据id 找到评论，，id在一个网页中是唯一的，就像我们的身份证号码一样
    # print(all_comments)
    # 然后从评论代码里面提取出评论的内容,
    comments = comments.find_all(name='span', attrs={'class': 'short'})
    # 把爬到的评论的字符串加到已有评论的后面
    for comment in comments:
        all_comments.append(comment.string)
print('共爬取{}条评论'.format(len(all_comments))) # 看下总共爬下来是不是我们指定的条数

# 第二步：存到文件
# 接下来把评论存到文件里面去，用我们学过的with语句
filename = '{}评论.txt'.format(book_name)
with open(filename,'w') as file:
    print(all_comments)
    for comment in all_comments:
        # 评论不一定会是纯文字的，可能会有一些表情，
        # 如：写这么老多挺不容易的就多加一星吧🙄
        # 这些表情会导致在写文件的时候编码错误,所以我们忽略这些评论
        try:
            print(comment)
            str = '{}\n'.format(comment)
            file.write(str)
        except Exception as e:
            continue
    print('评论已存到文件')

# 第三步：读取文件，做成词云图
# 最后我们从文件中读取出评论
with open(filename,'r') as file:
    comment = file.read()
    # 再调用词云分析程序，将评论做成一张词云图
    from create_wordcloud import gen_cloud
    gen_cloud(content=filename,background='人.png')