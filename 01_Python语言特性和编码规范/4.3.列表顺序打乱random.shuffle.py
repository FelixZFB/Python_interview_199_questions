# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/1 12:27
Desc:
'''
import random
a = [1, 2, 3]
# 打乱的是原列表，该方法结果为None
b = random.shuffle(a)
print(b)
print(a)