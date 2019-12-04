# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 20:05
Desc:
'''
# 元组里面元素严格是不可变，不能修改的
# 但是元组是支持索引操作的，如果里面有元素是列表是可以修改的，不推荐这么做

a = (1,2,3,[4,5,6,7],8)
# a[2] = 2 # 语法提示错误
print(a)
# TypeError: 'tuple' object does not support item assignment

a[3][0] = 2
print(a)
# (1, 2, 3, [2, 5, 6, 7], 8)