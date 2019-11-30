# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/11/28 21:20
Desc:
'''

# reverse:python中列表的一个内置方法（也就是说，在字典，字符串或者元组中，是没有这个内置方法的），用于列表中数据的反转
ls1 = [1, 2, 3]
ls1.reverse()
print(ls1)

# reversed: reversed()的作用之后，返回的是一个把序列值经过反转之后的迭代器，
# 所以，需要通过for循环遍历，或者list,或者next()等方法，获取作用后的值
# 列表，元组，字符串可迭代对象都可以反转成一个迭代器
ls2 = [4, 5, 6]
print(reversed(ls2)) # 迭代器对象的内存地址
print(list(reversed(ls2)))

# 字符串反转方法1
str1 = 'abced12345'
str2 = ''.join(reversed(str1)) # 使用join拼接反转后的字符
print(str2)

# 字符串反转方法2
str3 = str1[::-1]
print(str3)


