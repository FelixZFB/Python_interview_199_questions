# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/1 12:12
Desc:
'''
# 嵌套列表到单层列表
l1 = [[1,2],[3,4],[5,6]]
# 先从列表l1中取出每个列表i，然后从每个列表i中取出元素j，然后由j生成一个新的列表
l2 = [j for i in l1 for j in i]
print(l2)

# 字符串到列表，使用逗号分隔，如果只是单纯的字符串，直接使用list就可以生成列表
s1 = 'a,b,c,1,2,3'
l3 = s1.split(',')
print(l3)
