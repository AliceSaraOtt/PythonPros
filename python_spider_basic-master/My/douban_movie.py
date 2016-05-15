#coding:utf8
import urllib2,json
from HTMLParser import HTMLParser

class MoveParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.moves = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        if tag == 'li' and _attr(attrs,'data-title') and _attr(attrs,'data-category') == 'nowplaying':
            move = {}
            move['title'] = _attr(attrs,'data-title')
            move['score'] = _attr(attrs,'data-score')
            move['director'] = _attr(attrs,'data-director')
            move['actors'] = _attr(attrs,'data-actors')
            self.moves.append(move)
            # print '%(title)s|%(score)s|导演：%(director)s|主演：%(actors)s' % move
            move = json.dumps(move,indent=1,ensure_ascii=False) # ensure_ascii=False  不确保按照asciII编码  按照默认参数encoding编码
            print move

def getHotMove():
    url = 'https://movie.douban.com/nowplaying/beijing/'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = urllib2.Request(url,headers=header)
    rep = urllib2.urlopen(req)
    parser = MoveParser()
    parser.feed(rep.read())


if __name__ == '__main__':
    getHotMove()
