# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/11/28 18:39
Desc:
'''

def print_max(x,y):
    '''
    打印两个整数中较大的值
    :param x: 整数
    :param y: 整数
    :return: 返回较大值
    '''
    if x > y:
        print(x)
    else:
        print(y)

print_max(3, 5)
print(print_max.__doc__)