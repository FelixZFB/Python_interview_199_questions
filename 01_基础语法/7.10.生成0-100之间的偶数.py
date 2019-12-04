# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/3 10:09
Desc:
'''
# 方法1：二进制数（整型）数的第零位的值是1，那么这个数就是奇数；而如果该位是0，那么这个数就是偶数
l1 = [i for i in range(1, 101) if i & 0x1 == 0]
print(l1)

# 方法2：余数为0
l2 = [i for i in range(1, 101) if i % 2 == 0]
print(l2)

# 方法3: 效率最高
l3 = list(range(2, 101, 2))
print(l3)