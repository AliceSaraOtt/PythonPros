#coding:utf8
from lxml import etree
import requests
import urllib

root_url = 'http://www.maiziedu.com/course/python/'

last = 0.0
def progress(blk, blk_size, total_size):
    global last
    if ((float)(blk * blk_size) * 100 / total_size) - last > 5:
        print('%d/%d - %.02f%%' % (blk * blk_size, total_size, (float)(blk * blk_size) * 100 / total_size))
        last = (float)(blk * blk_size) * 100 / total_size
# urllib.urlretrieve('http://ocsource.maiziedu.com/csshtml1.m4v','f:/csshtml1.m4v',reporthook=progress)

def get_url(root_url):
    urls = []
    rep = requests.get(root_url)
    tree = etree.HTML(rep.content)
    links = tree.xpath('//div[@class="lead-img"]/a/@href')
    for link in links:
        urls.append(root_url + '/' + link.split('/')[-1])
    return urls

# 需要所有单个课程url
def get_course_url(url):
    course_urls = []
    req = requests.get(url)
    tree = etree.HTML(req.content)
    links = tree.xpath('//a')
    for link in links:
        if link.xpath('@lesson_id'):
            course_urls.append(link.xpath('@href')[0])
    print len(course_urls)
    exit()

if __name__ == '__main__':
    urls = get_url(root_url) # 获取单个课程总页面
    for url in urls:
        course_urls = get_course_url(url)
        break