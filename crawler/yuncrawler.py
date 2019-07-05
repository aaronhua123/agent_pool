import time
from random import choice
import requests
import dbmodle
from checkproxy import check_proxy_by_gevent


def queryyun(page):
    url = 'http://www.ip3366.net/?stype=1&page=%s'%page
    r = requests.get('http://127.0.0.1:5000/http', timeout=30)
    proxies = r.json()
    r = requests.get(url, proxies=proxies,timeout=30)
    r.encoding = 'gbk'
    return r

from lxml import etree


def analyzeyun(r):
    tree = etree.HTML(r.text)
    tr_list = tree.xpath('//div[@id="list"]//tbody/tr')
    _ = []
    for tr in tr_list:
        # td = tr.xpath('./td/text()')
        td = tr.xpath('./td[4]/text()')
        if td:
            if td[0].lower() in ['http', 'https']:
                proxy = {
                    td[0].lower(): f"{td[0].lower()}://{tr.xpath('./td[1]/text()')[0]}:{tr.xpath('./td[2]/text()')[0]}"
                }
                print(proxy)
                _.append(proxy)
    return _
if __name__ == '__main__':
    while 1:
        try:
            page = choice(range(1, 11))
            r = queryyun(page)
            result = analyzeyun(r)
            print('result', result)
            for proxy in result:
                for protocol, url in proxy.items():
                    print("save ", proxy)
                    if 'https' in url:
                        dbmodle.sethttps(url)
                    else:
                        dbmodle.sethttp(url)
        except Exception as e:
            print(e)
            # raise
        time.sleep(30)



