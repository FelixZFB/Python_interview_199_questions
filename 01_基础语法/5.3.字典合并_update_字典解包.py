# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 11:23
Desc:
'''
# 方法1：
# 使用update方法，将b字典添加到a中，类似于列表的append方法
a = {"A": 1,"B": 2}
b = {"C": 3,"D": 4}
a.update(b)
print(a)

# 方法2:
# 使用字典解包
a = {"A": 1,"B": 2}
b = {"C": 3,"D": 4}
print({**a})
print({**a,**b})



