# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/2 20:45
Desc:
'''
import json

# file = open('papers.json', 'w', encoding='utf-8')
# 将item字典类型的数据转换成json格式的字符串,
# 注意json.dumps序列化时对中文默认使用的ascii编码，要想写入中文，加上ensure_ascii=False
# line = json.dumps(dict(item), ensure_ascii=False) + "\n"
# file.write(line)

a=json.dumps({"name": "张三"}, ensure_ascii=False)
# 转换后，中文字符还是显示中文，不会转换成ascii编码
# 写入文件后也还是显示中文
print(a)