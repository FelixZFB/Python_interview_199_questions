# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/11/28 16:58
Desc:
'''


# 用 : 类型 的形式指定函数的参数类型，用 -> 类型 的形式指定函数的返回值类型。
# 然后特别要强调的是，Python 解释器并不会因为这些注解而提供额外的校验，
# 没有任何的类型检查工作。也就是说，这些类型注解加不加，对你的代码来说没有任何影响

def add(x: int, y: int) -> int:
    return x + y


print(add(1, 2))
print(add('a', 'b'))
print(add(1.2, 2.6))

# 变量注释
aaa: str = 'this is string type'

# 上面代码提示语法警告，但是结果都是可以运行出来的

# 好处是：
# 1. 让别的程序员看得更明白
# 2. 让IDE了解类型，从而提供更准确的代码提示、补全和语法检查（包括类型检查，可以看到 str 和 float 类型的参数被高亮提示）
