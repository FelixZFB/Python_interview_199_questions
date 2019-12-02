# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 20:55
Desc:
'''
def outer(num):
    def inner(val):
        return num * val
    return inner

# 闭包函数，外部函数返回值是内部函数
m = outer(8)
print(m(5))
# 传入8返回内部函数，内部函数传入参数5，外部的参数8乘以内部的参数5就是最终的值