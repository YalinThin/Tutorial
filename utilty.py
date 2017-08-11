#encoding:utf-8
import random

def get_rand_ua():
    ua_list = [ua.replace('\n', '') for ua in open('useragents.txt', 'r').readlines()]
    return random.choice(ua_list)