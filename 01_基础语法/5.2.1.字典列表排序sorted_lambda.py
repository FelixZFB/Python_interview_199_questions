# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/1 16:25
Desc:
'''
d1 = [
    {'name':'alice', 'age':38},
    {'name':'bob', 'age':18},
    {'name':'Carl', 'age':28},
]

# 排列列表中字典，直接排列字典也是相同的方法
# 默认reverse=False
d2 = sorted(d1, key=lambda x: x['age'])
print(d2)

# 倒序，传入reverse=True
d3 = sorted(d1, key=lambda x: x['age'], reverse=True)
print(d3)


# 也可以传入索引值，用于排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
d4 = sorted(students,key=lambda x: x[2])
print(d4)
