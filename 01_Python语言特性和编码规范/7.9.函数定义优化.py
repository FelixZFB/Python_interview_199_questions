# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/3 10:00
Desc:
'''

# 不合理写法
def strappend(num):
    str='first'
    for i in range(num):
        str+=str(i)
    return str


# 优化后写法
def str_append(num):
    s = 'first'
    for x in range(num):
        s += str(x)
        yield s

if __name__ == '__main__':
    for i in str_append(5):
        print(i)