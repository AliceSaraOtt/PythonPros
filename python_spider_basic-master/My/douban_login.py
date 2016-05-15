#coding:utf8
import requests
from HTMLParser import HTMLParser

class DoubanClient():
    def __init__(self):
        self.session = requests.session()
        header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        self.session.headers.update(header)
    def login(self,uname,pwd,redir='http://www.douban.com',login='登陆'):
        url = 'https://accounts.douban.com/login'
        data = {
            'source':'None',
            'redir':'https://www.douban.com/',
            'form_email':uname,
            'form_password':pwd,
            'login':login
        }
        headers = {
            'host' : 'accounts.douban.com',
            'referer' : 'https://www.douban.com/accounts/login?redir=https://www.douban.com/'
        }
        rep = self.session.post(url,data=data,headers=headers)
        print rep.content
        print self.session.cookies.items()


if __name__ == '__main__':
    client = DoubanClient()
    client.login('1752570559@qq.com','11111111')


