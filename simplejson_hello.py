#http://blog.csdn.net/hshl1214/article/details/45291011

import simplejson

info = {'name' : 'jay', 'sex' : 'male', 'age': 22}
jsoninfo = simplejson.dumps(info)
print jsoninfo
print type(jsoninfo)


dictinfo = simplejson.loads(jsoninfo) 

print dictinfo
print type(dictinfo)

print dictinfo['name']
