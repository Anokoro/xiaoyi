# -*- coding:utf-8 -*-
# author：岳昊玮
# date  ：2019/6/11  
# time  : 16:43   
# IDE   : PyCharm
# description :

from bs4 import BeautifulSoup as Soup
import requests

url = 'https://maoyan.com'
r = requests.get(url)
html_code = r.text
soup = Soup(html_code, "html.parser")
comments = soup.find(id='comments')  # 根据id 找到评论，，id在一个网页中是唯一的，就像我们的身份证号码一样
# print(all_comments)s
# 然后从评论代码里面提取出评论的内容,
list = soup.find_all(name='div', attrs={'class': 'panel-content'})[0]
top_1_movie_name = list.find(name='span', attrs={'class': 'ranking-top-moive-name'})
left_9_movie_names = list.find_all(name='span', attrs={'class': 'ranking-movie-name'})

hot_movies_name = [top_1_movie_name.string]
for movie in left_9_movie_names:  # 提取名称
    hot_movies_name.append(movie.string)
print(len(hot_movies_name),hot_movies_name)

href = list.find_all('a')
hot_movies_href = []
for h in href:
    hot_movies_href.append('https://maoyan.com{}'.format(h['href']))
print(len(hot_movies_href),hot_movies_href)
# 下面就得到了最热门的top10的电影名称以及他们的URL
hot_movies = zip(hot_movies_name,hot_movies_href)

# 接下来我们爬取每一个电影的详细信息
movie_info = {}  # 用一个字典来记录
print('\n正在爬取电影信息...')
for movie in hot_movies:
    print(movie[0])
    url = movie[1]
    r = requests.get(url)
    html_code = r.text
    soup = Soup(html_code, "html.parser")
    head = soup.find(name='div',attrs={'class':'movie-brief-container'})
    # print(head) # head 里面包括电影名，别名、上映时间等信息
    # 提取head信息
    movie_info[movie[0]]={}
    movie_info[movie[0]]['别名'] = head.find(name='div',attrs={'class':'ename ellipsis'}).string.strip()
    movie_info[movie[0]]['类型'] = head.find_all(name='li',attrs={'class':'ellipsis'})[0].string.strip()
    movie_info[movie[0]]['国家/时间'] = head.find_all(name='li',attrs={'class':'ellipsis'})[1].string.strip()
    movie_info[movie[0]]['上映'] = head.find_all(name='li',attrs={'class':'ellipsis'})[2].string.strip()
    # 找演员
    actor_group = soup.find_all(name='div',attrs={'class':'celebrity-group'})

    # print(actor_group[0].find(name='div',attrs={'class':'info'}))
    movie_info[movie[0]]['导演'] = actor_group[0].find(name='div',attrs={'class':'info'}).a.string.strip()
    movie_info[movie[0]]['演员'] = []  # 演员有好多个
    actors = actor_group[1].find_all(name='div',attrs={'class':'info'})
    for actor in actors:
        movie_info[movie[0]]['演员'].append(actor.a.string.strip())

# print(movie_info)  # 直接打印字典当然可以
# 这里教给大家一个格式化打印字典的方法，可以让输出更清晰
from pprint import pprint
# pprint(movie_info)

# # 第二步：存到文件
# # 接下来把信息存到文件里面去，用我们学过的with语句
print('\n正在存入文件...')
filename = 'hot_movies_top10.txt'
with open(filename,'w',encoding='utf-8') as file:
    for name,info in movie_info.items():
        print(name)
        str='《{}》\n'.format(name)
        file.write(str)
        for info_key,info_value in info.items():
            str='\t{}:{}\n'.format(info_key,info_value)
            file.write(str)
    print('存入文件完成...')
