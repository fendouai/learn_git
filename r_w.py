f = open('test.txt', 'r')
print f.read()


f = open('test.txt', 'w')
f.write('Hello, world!')

f = open('test.txt', 'r')
print f.read()

f.close()