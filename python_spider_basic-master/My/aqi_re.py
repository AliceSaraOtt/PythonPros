#coding:utf8
import requests,re
from multiprocessing.dummy import Pool
import json
import MySQLdb as db

def saveData(data):
    sql = "insert ignore into city_data(city,date,aqi,alevel,desert) value(%s,%s,%s,%s,%s)"
    try:
        cur.executemany(sql,data)
    except Exception,e:
        print str(e)
    conn.commit()

def AqiSpider(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    rep = requests.get(url,headers=headers)
    # 用懒惰模式匹配多行 后边没写完，但思路已经很清晰了
    trs = re.findall(r'<tr height=30 style="height:30px;">.*?</tr>',rep.content,re.S)
    for tr in trs:
        print tr

if __name__ == '__main__':
    urls = []
    for i in range(1,2):
        url = 'http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=北京市&startdate=2016-01-01&enddate=2016-05-19&page=%d' % i
        urls.append(url)
    try:
        conn = db.connect(user='root',passwd='123',host='127.0.0.1',db='aqi_data',charset='utf8')
    except Exception,e:
        print str(e)
    cur = conn.cursor()

    pool = Pool(2)
    pool.map(AqiSpider,urls)
    pool.close()
    pool.join()