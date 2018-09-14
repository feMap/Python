# -*- coding: utf-8 -*-

################################################
# 01 -- 变量交换
# Bad
tmp = a
a = b
b = tmp

# Pythonic
a, b = b, a

################################################
# 02 -- 列表解析式
# Bad
my_list = []
for i in range(10):
    my_list.append(i*2)

# Pythonic
my_list = [i*2 for i in range(10)]

################################################
# 03 -- 当行表达式
# Bad
print 'one'; print 'two'

if x == 1: print 'one'

if <complex comparison> and <other complex comparison>:
    # do something

# Pythonic
print 'one'
print 'two'

if x == 1:
    print 'one'

cond1 = <complex comparison>
cond2 = <other complex comparison>

if cond1 and cond2:
    # do something

################################################
# 04 -- 带索引的遍历
# Bad
for i in range(len(my_list)):
    print(i, "->", my_list[i])

# Pythonic
for i,item in enumerate(my_list):
    print(i, "->", item)

########################
# 05 -- 序列解包
# Pythonic
a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]

a, *mid, c = [1, 2, 3, 4]
# a = 1, mid = [2, 3], c = 4

################################################