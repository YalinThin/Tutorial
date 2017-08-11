#encoding:utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# url = 'http://search.ifeng.com/sofeng/search.action?q=%E6%B3%B8%E5%B7%9E%E4%B8%AD%E5%8D%87%E4%B9%8B%E6%98%9F&c=1&chel=&p=1'
# resp = requests.get(url)
#
# soup = BeautifulSoup(resp.text, 'html.parser')
#
# news_divs = soup.find_all('div', attrs={'class':'searchResults'})
# for news in news_divs:
#     url = news.find('p').find('a').get('href')
#     print url

#
# with open('news.html', 'r') as f:
#     cont = f.read()
#
# soup = BeautifulSoup(cont, 'lxml')
# print soup.find('div')

# url = 'http://auto.gasgoo.com/Search.aspx?keyWord=庞大集团'
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, 'html.parser')
# print soup.find('a', text='>>')

with open('news.html', 'r') as f:
    cont = f.read()

print cont


