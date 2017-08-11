#encoding:utf-8
import json

from bs4 import BeautifulSoup
from lxml import etree

import requests
import sys
import urllib2
import cookielib
import utilty
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {'User-Agent': utilty.get_rand_ua()}
# # from_url = 'http://dw.xcar.com.cn/analyticsx.php'
cookies = {
# # #            # 'place_crid':'539',
# # #            # 'place_ip':'183.228.117.92_1',
# # #            'place_prid':'4',
           '_PVXuv':'e989safd'
          }
# #
# #            # '_Xdwstime':'1502075471',
# #            # '_Xdwuv':'5987da4fb0db0',
# #            # '_Xdwnewuv': '1'
# #
url = 'http://sou.xcar.com.cn/XcarSearch/infobbssearchresult/bbs/%E5%B9%BF%E6%B1%87/none/none/none/none/1'
resp = requests.get(url, headers=headers, cookies=cookies)
print resp.apparent_encoding
with open('test', 'w') as f:
    f.write(resp.text)
print resp.text.encode('utf-8')
sys.exit(0)
for i in range (len(resp.text)):
    print i
    print resp.text[i]
    dict_result = resp.text[0:i+1].decode('utf-8')

# for post in dict_result:
#     print post['title']
