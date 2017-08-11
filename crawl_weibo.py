#encoding:utf-8
# from bs4 import BeautifulSoup
#
# with open('news.html', 'r') as f:
#     con = f.read()
#
# soup = BeautifulSoup(con, 'lxml')
# soup = soup.find('div', id='he')
# soup.find('script').extract()
# print soup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# cookies = {'Cookie':'_s_tentry=cuiqingcai.com; Apache=8030881472165.597.1502291498003; SINAGLOBAL=8030881472165.597.1502291498003; ULV=1502291498219:1:1:1:8030881472165.597.1502291498003:; login_sid_t=b5f8f4e414f550858fb7085e19774b98; appkey=; un=18696582150; wvr=6; UOR=finance.ifeng.com,widget.weibo.com,python.jobbole.com; SCF=Avud0S4eakpHs1kYDKDx7MmzER_Ksn0Jokyr7t61wa5sOm-V88pKPNvaqq2NFvxQaY05hhRfMEeG6PrHnxBTETs.; SUHB=0Yhho5ITkuXJcB; SRT=D.QqHBJZ4nT4mrNmMb4cYGSPSGiFoHPDb9S!ywTcsHNEYddEyzTbBpMERt4EP1RcsrAcPJ4!ArTsVud4m-NFsIiQR3iQimAd!3WDBCUFyI4b9BAZEeI8t7*B.vAflW-P9Rc0lR-ykbDvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWQJDEuWsHgJQWTJcSIAd4-5DWj4cbEi49ndDP6JevsO!YmKOPMJDEfIZWbU3mrSd0kSbWqimMoR-9M5Evu5dM8NDYOM!YFJ4izP-PDNDXoApsN4r4k4eYDNDYOM!YFA!izP-PDNDXoArYQ5mRk4cPlWGA7; SRF=1502379607'}

url = 'https://m.weibo.cn/'

# resp = requests.get(url, cookies=cookies)
resp = requests.get(url)
print resp.text
