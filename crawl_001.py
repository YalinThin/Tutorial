#encoding: utf-8
import random
import re
import urllib, urllib2, cookielib
import sys

import time
import urlparse

import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

ua_list = [ua.replace('\n', '') for ua in open('useragents.txt', 'r').readlines()]            #懒人写法


def simple_crawl_01():
    '''
    抓取豆瓣图书top250
    :return:
    '''
    page_list = ['https://book.douban.com/top250?start=%s' % i for i in range(0, 250, 25)]  # 生成top250的10个页面list
    top250_book_list = []

    for page in page_list:
        time.sleep(1)
        # resp = urllib.urlopen(page)
        headers = {'User-Agent': random.choice(ua_list)}
        req = urllib2.Request(page, headers=headers)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'fail to reach the server, reason is %s'%e.reason
            elif hasattr(e, 'code'):
                print 'error code is %s'%e.code
        else:
            source_html = resp.read().decode('utf-8')

            p = re.compile(r'<div class="pl2">\n\n\s*<a.*title="(.*)"')
            book_list = re.findall(p, source_html)

            top250_book_list.extend(book_list)

    # print top250_book_list
    with open('top250.txt', 'w') as f:
        for book in top250_book_list:
            f.write(book + '\n')

# def simple_crawl_02():


def crawl_51job():
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=1&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    try:
        resp = urllib2.urlopen(url)
    except urllib2.URLError, e:
        print e.reason
        print e.message
    else:
        cont = resp.read().decode('gbk')

        soup = BeautifulSoup(cont, 'html.parser')

        all_jobs = soup.find_all('div', attrs={'class':'el'})

        print all_jobs



def crawl_sougou():
    url = 'http://news.sogou.com/news?query=site%3Aqq.com+%C5%D3%B4%F3%BC%AF%CD%C5'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    next_url = soup.find('a', id='sogou_next')
    print next_url

crawl_sougou()
