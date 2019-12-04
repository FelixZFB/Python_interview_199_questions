# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 20:26
Desc:
'''
# 自定义时间序列化
import json
from datetime import datetime, date

# JSONEncoder 不知道怎么去把这个数据转换成 json 字符串的时候
# ，它就会去调 default()函数,所以都是重写这个函数来处理它本身不支持的数据类型，
# default()函数默#认是直接抛异常的。
class DateToJson(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


d = {'name': 'cxa', 'data': datetime.now()}
print(json.dumps(d, cls=DateToJson))