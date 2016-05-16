#coding:utf8
import requests,json
from HTMLParser import HTMLParser

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

class MoveParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.moves = []
        self.in_move = False

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
            self.in_move = True
            # print '%(title)s|%(score)s|导演：%(director)s|主演：%(actors)s' % move
        if tag == 'img' and self.in_move == True:
            self.in_move = False
            move = self.moves[-1]
            move['poster-url'] = _attr(attrs,'src')
            downPoster(move)
            move = json.dumps(move,indent=1,ensure_ascii=False) # ensure_ascii=False  不确保按照asciII编码  按照默认参数encoding编码
            print move

def getHotMove():
    url = 'https://movie.douban.com/nowplaying/beijing/'
    rep = requests.get(url,headers=headers)
    parser = MoveParser()
    parser.feed(rep.content)

def downPoster(move):
    url = move['poster-url']
    rep = requests.get(url,headers=headers)
    print('downloading post cover from %s' % url)
    fname = url.split('/')[-1]
    with open(fname,'wb') as f:
        f.write(rep.content)
    move['poster'] = fname

if __name__ == '__main__':
    getHotMove()
