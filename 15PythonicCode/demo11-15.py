# -*- coding: utf-8 -*-

################################################
# 11 -- 代码续行
# Bad
my_very_big_string = """For a long time I used to go to bed early. Sometimes, 
    when I had put out my candle, my eyes would close so quickly that I had not even 
    time to say “I’m going to sleep.”"""

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, 
    yet_another_nice_function

# Pythonic
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)

from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)

################################################
# 12 -- 显式代码
# Bad
def make_complex(*args):
    x, y = args
    return dict(**locals())

# Pythonic
def make_complex(x, y):
    return {'x': x, 'y': y}

################################################
# 13 -- 使用占位符
# Pythonic
filename = 'foobar.txt'
basename, _, ext = filename.rpartition(".")

########################
# 14 -- 链式比较
# Bad
if age > 18 and age < 60:
    print('young man')

# Pythonic
if 18 < age < 60:
    print("young man")
# Python 中的链式比较原则 18 < age < 60 等价于 (18 < age) and (age < 60)

################################################
# 15 -- 三目运算符
# Bad
a = 3
if a > 2:
    b = 2
else:
    b = 1

# Pythonic
a = 3
b = 2 if a > 2 else 1

################################################