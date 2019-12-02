# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 20:51
Desc:
'''
import datetime

def datetime_operate(n: int):
    now = datetime.datetime.now()  # 获取当前时间
    _new_date = now + datetime.timedelta(days=n)  # 获取指定天数后的新日期
    new_date = _new_date.strftime("%Y%m%d")  # 转换为指定的输出格式
    return new_date

if __name__ == '__main__':
    print(datetime_operate(2))