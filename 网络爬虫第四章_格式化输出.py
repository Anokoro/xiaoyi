# -*- coding:utf-8 -*-
# author：岳昊玮
# date  ：2019/6/6  
# time  : 11:01   
# IDE   : PyCharm
# description :

# **********引入**********
# 今天分享一下Python的format格式化输出的一些基本函数，什么叫做format格式化输出？
# 相对基本格式化输出采用%号的方法，format（）功能更加强大，
# 该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用{}号作为特殊字符代替%号。
# 我们之前所使用的普通版本
name = 'Alex'
gender = 'boy'
age = 15
print('姓名',name,'性别',gender, '年龄',age,)
# 它有什么缺点呢？
# 1、编写麻烦：需要写很多的分隔符
# 2、不清晰：看得时候结构太乱
# 3、不灵活，名字、年龄这类都是可变的参数

# **********入门*********

# 下面我们来学习一种更加简洁的写法 使用format函数
print("姓名：{} 性别：{} 年龄：{}".format(name,gender,age))

# 使用参数位置来进行填充  修改一下，如果我们需要输出两次名字，我们是不是就需要写两次名字呢？
print('我有个朋友叫{},{}有个小狗'.format(name,name))
# 我们有更简洁的办法，根据位置来定位   在大括号里面协商数字表示位置
print('我有个朋友叫{0},{0}有个小狗'.format(name))
# 使用参数名称，
print('姓名：{name} 性别：{gender} 年龄： {age}'.format(name=name,gender=gender,age=age))
# 不知道大家有没有学过字典，这种格式就是字典的格式
dictionary = {'name':name,'gender':gender,'age':age}
print('姓名：{name} 性别：{gender} 年龄： {age}'.format(**dictionary))


# **********分割线**********
# 大家想一想，我们写东西的时候经常会用到分割线，这样可以让看的人很快地看清楚，
# 下面我们来看看如何快速打出一个分割线
# 正常版本  左右各10个*   （突出这个数*号的过程比较繁琐）  数了半天还不一定数的对
print('**********分割线**********')
# 高级版本：  用我们的format来解决  如下所示
# 假如我们要左右各10个星号，那么总共就是20个*，再加上我们的分割线三个字占掉三个星号，
# 所以我们总共需要10*2+3 = 23个星号。这样一算，既快又准
print('{:*^23}'.format('分割线'))  # 居中
# 除了可以居中，我们也可以让它居左或者居右，但是没有居中好看罢了
print('{:*<23}'.format('分割线'))  # 居左
print('{:*>23}'.format('分割线'))  # 居右

####### 到此为止吧  不需要讲太多了，，，下面讲文件操作




