import urllib2,urllib

# res = urllib2.urlopen('http://www.douban.com')\
url = 'http://www.douban.com'
data = {1:'a',2:'b'}
data = urllib.urlencode(data)
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

req = urllib2.Request(url,data,header)
rep = urllib2.urlopen(req)
# print rep.geturl()
html = rep.read()

print html
