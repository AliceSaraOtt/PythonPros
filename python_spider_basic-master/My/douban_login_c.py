#coding:utf8
import requests
from HTMLParser import HTMLParser

class DoubanClient():
    def __init__(self):
        self.session = requests.session()
        header = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'host' : 'accounts.douban.com',
        }
        self.session.headers.update(header)
    def login(self,uname,pwd,redir='http://www.douban.com',login='登陆'):
        url = 'https://accounts.douban.com/login'
        rep = self.session.get(url)
        capcha_id ,capcha_url = get_capcha(rep.content)
        if capcha_id:
            capcha_solution = raw_input(u'%s\n输入验证码：' % capcha_url)

        url = 'https://accounts.douban.com/login' # 登陆数据提交url
        data = {
            'redir':'https://www.douban.com/',
            'form_email':uname,
            'form_password':pwd,
            'login':login,
        }
        if capcha_id:
            data['captcha-solution'] = capcha_solution
            data['captcha-id'] = capcha_id

        headers = {
            'host' : 'accounts.douban.com',
            'referer' : 'https://www.douban.com/accounts/login?redir=https://www.douban.com/'
        }
        rep = self.session.post(url,data=data,headers=headers)
        print self.session.cookies.items()

def get_capcha(content):
    class CapChaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.capcha_id ,self.capcha_url = None ,None
        def handle_starttag(self, tag, attrs):
            if tag == 'img' and _attr(attrs,'id') == 'captcha_image' and _attr(attrs,'class') == 'captcha_image':
                self.capcha_url = _attr(attrs,'src')
            if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'captcha-id':
                self.capcha_id = _attr(attrs,'value')
    p = CapChaParser()
    p.feed(content)
    return p.capcha_id, p.capcha_url


def _attr(attrs,attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

if __name__ == '__main__':
    client = DoubanClient()
    client.login('1752570559@qq.com','11111111')


