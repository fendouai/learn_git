import redis

# it is a bad idea to name a python file as a module name
r = redis.Redis(host='localhost',port=6379,db=0)
r.set('guo','shuai')

print r.get('guo')