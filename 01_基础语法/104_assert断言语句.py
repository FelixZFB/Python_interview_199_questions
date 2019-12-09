# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/9 11:17
Desc:
'''
def deallist(l):
    """
    此函数是用来返回列表中元素的和
    """
    assert len(l) > 1, '此列表中没有元素'
    return sum(l)

l1 = [1,2,3,4,5]
l2 = []
try:
    a = deallist(l2)
except AssertionError as err:
    print('出现错误，错误类型是：', err)
else:
    print('和是：', a)