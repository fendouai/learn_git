from urlparse import urlparse
o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print o   
#ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',params='', query='', fragment='')
print o.scheme
#'http'
print o.port
#80
print o.geturl()
#'http://www.cwi.nl:80/%7Eguido/Python.html'
