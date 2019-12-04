# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/3 10:39
Desc:
'''
s1 = 'abaFAAabEDJHGA'

count = 0
for i in s1:
    if i.isupper():
        count += 1
print(count)