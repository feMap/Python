# -*- coding: utf-8 -*-

################################################
# 06 -- 字符串拼接
# Bad
letters = ['s', 'p', 'a', 'm']
s = ""
for let in letters:
    s += let

# Pythonic
letters = ['s', 'p', 'a', 'm']
s = ''.join(letters)

################################################
# 07 -- 真假判断
# Bad
if attr == True:
    print "True!"

if attr == None:
    print "Attr is None"

# Pythonic
if attr:
    print "Attr is True!"

if not attr:
    print "Attr is False!"

if attr in None:
    print "Attr is None!"

################################################
# 08 -- 访问字典元素
# Bad
d = {'hello': 'world'}
if d.has_key('hello'):
    print d['hello']
else:
    print 'default_value'

# Pythonic
d = {'hello': 'world'}
print d.get('hello', 'default_value')
print d.get('hello2', 'default_value')


# OR
d = {'hello': 'world'}
print d['hello'] if d.has_key('hello') else 'default_value'
print d['hello'] if 'hello' in d else 'default_value'

################################################
# 09 -- 操作列表
# Bad-1
a = [3, 4, 5]
b = []
for i in a:
    if i > 4:
        b.append(i)

# Pythonic-1
a = [3, 4, 5]
b = [i for i in a if i > 4]
# Or:
b = filter(lambda x: x > 4, a)

# Bad-2
a = [3, 4, 5]
for i in range(len(a)):
    a[i] += 3

# Pythonic-2
a = [3, 4, 5]
b = [i + 3 for i in a]
# Or:
b = map(lambda i: i + 3, a)

################################################
# 10 -- 文件读取
# Bad
f = open('file.txt')
# 这个应该是相当于将文件内容全部读到内存里面
a = f.read()
print a
f.close()

# Pythonic
with open('file.txt') as f:
    for line in f:
        print line

################################################