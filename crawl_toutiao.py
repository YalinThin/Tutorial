#encoding:utf-8
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


def crawl_toutiao():
    url = 'https://www.toutiao.com/search'
    driver = webdriver.PhantomJS()
    # driver.set_window_size(1920, 2000)
    driver.set_window_size(1000, 1000)
    resp = driver.get(url)

    # resp = driver.page_source
    driver.find_element_by_name('keyword').send_keys(u'庞大集团')
    driver.find_element_by_class_name('search-btn').click()
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp, 'html.parser')
    js = '''
        return document.documentElement.scrollTop + document.documentElement.clientHeight == document.body.scrollHeight;
    '''
    scroll_js = "window.scrollTo(0, document.documentElement.scrollHeight);"
    time.sleep(1)
    # while True:
    while True:
        print driver.execute_script('return document.body.scrollHeight;')
        driver.execute_script(scroll_js)
        time.sleep(1)

        if driver.execute_script(js):
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print soup


    titles = soup.find_all('span', attrs={'class': 'J_title'})
    for title in titles:
        print title.text

    # driver.get_screenshot_as_file('pangda.png')


    # print driver.page_source
    # print soup.find('div', attrs={'class': 'normal rbox '})
    # driver.close()


crawl_toutiao()