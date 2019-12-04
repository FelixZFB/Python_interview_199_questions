# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 11:40
Desc:
'''
# 字典键值交换
d = {'a': '1', 'b': '2', 'c': '3'}
print({v: k for k,v in d.items()})


# 字符串分割后得到字典
cookies = "anonymid=k06r6sdauyh36v; depovince=ZGQT; _r01_=1; JSESSIONID=abcOraT1E7z0JhHDATb0w; ick_login=8f53ebf1-b972-4572-8f77-810953dcfdfe; first_login_flag=1; ln_uact=908851835@qq.com;loginfrom=null; wp_fold=0"
# 使用字典推导式将上述字符串转化为一个字典, 先使用;分割得到一个列表，
# 列表中每一个元素再用=进行分割，列表第一个值为键，第二个值为值
cookies ={i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
print(cookies)