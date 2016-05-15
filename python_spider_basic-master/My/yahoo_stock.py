import urllib


class Stock():
    # stock_list = []
    def __init__(self, stock_list=None):
        self.stock_list = stock_list

    def get_all(self):
        print self.stock_list
        for sid in self.stock_list:
            # url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
            url = 'http://real-chart.finance.yahoo.com/table.csv?s=' + sid
            fname = sid
            res = urllib.urlretrieve(url, sid)

if __name__ == '__main__':
    stock_list = ['000001.ss', '300287.sz']
    gs = Stock(stock_list)
    gs.get_all()
