# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 17:00
Desc:
'''
from itertools import islice
gen = iter(range(10)) #iter()函数用来生成迭代器
# 第一个参数是迭代器，第二个参数起始索引，第三个参数结束索引，不支持负数索引
# 生成器使用for循環取出每個值
for i in islice(gen, 4):
    print(i)
# 只給一個索引指的是結束的位置，從第一個值開始
for i in islice(gen,3):
    print(i)