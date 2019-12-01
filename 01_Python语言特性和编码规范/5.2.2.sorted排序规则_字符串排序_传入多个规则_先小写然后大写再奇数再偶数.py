# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/1 16:42
Desc:
'''

# 先看一下Boolean value 的排序：
# Boolean 的排序会将 False 排在前，True排在后
print(sorted([True,False]))

s = 'abC234568XYZdsf23'
# 排序规则：小写<大写<奇数<偶数
# 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x.isdigit() and int(x) % 2 == 0, x))))

# False排在后面
# 1.x.isdigit()的作用是把字母放在前边,数字放在后边.
# 2.x.isdigit() and int(x) % 2 == 0的作用是保证奇数在前，偶数在后。
# 3.x.isupper()的作用是在前面基础上,保证字母小写在前大写在后.
# 4.最后的x表示在前面基础上,对所有类别数字或字母排序。
# 同时满足上面的规则


list1=[7, -8, 5, 4, 0, -2, -5]
# 要求1.正数在前负数在后 2.整数从小到大 3.负数从大到小
# 先按照正负排先后，再按照大小排先后
print(sorted(list1,key=lambda x:(x<0, abs(x))))

# x<0，表示负数在后面，正数在前面
# abs(x)表示按绝对值，小的前面，大的在后面


