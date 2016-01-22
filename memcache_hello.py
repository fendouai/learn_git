#coding=utf8

import memcache

mcache= memcache.Client(['127.0.0.1:11211'])
print mcache.set('say','hello,memcache') #display - True
value = mcache.get('say')
print value #display - hello,memcache