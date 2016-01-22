#coding:utf-8
import os
print os.name #绝对路径
print os.path.abspath('.')


# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
path=os.path.join(os.path.abspath('.'), 'testdir')

print  path
#'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir(path)
print  os.listdir('.')

# 删掉一个目录:
os.rmdir(path)

print  os.listdir('.')