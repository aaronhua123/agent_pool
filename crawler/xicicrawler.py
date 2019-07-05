import time
from random import choice
import requests
from lxml import etree
from retrying import retry
import dbmodle


@retry(stop_max_attempt_number=10)
def get_ci_chi(page=1):
    session = requests.Session()
    url = 'https://www.xicidaili.com/nn/' + str(page)
    r = requests.get('http://127.0.0.1:5000/https', timeout=30)
    proxies = r.json()
    print(proxies)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version'
                      '/10.1.2 Safari/603.3.8'
    }
    r = session.get(url, timeout=10, verify=False, headers=headers, proxies=proxies)
    return r


@retry(stop_max_attempt_number=10)
def analyze_ci_chi(r):
    _ = []
    tree = etree.HTML(r.text)
    try:
        table = tree.xpath('//table')[0]
    except:
        return _
    tr_list = table.xpath('.//tr')
    for tr in tr_list:
        result = {}
        if tr.xpath('./td[2]/text()'):
            result["host"] = tr.xpath('./td[2]/text()')[0]
        else:
            continue
        if tr.xpath('./td[3]/text()'):
            result["port"] = tr.xpath('./td[3]/text()')[0]
        else:
            continue
        if tr.xpath('./td[6]/text()'):
            result["protocol"] = tr.xpath('./td[6]/text()')[0].lower()
        else:
            continue
        if result["protocol"] == "http":
            proxies = {
                "http": f'http://{result["host"]}:{result["port"]}'
            }
        else:
            proxies = {
                "https": f'https://{result["host"]}:{result["port"]}'
            }
        _.append(proxies)
    return _


if __name__ == '__main__':
    while 1:
        try:
            page = choice(range(1, 1000))
            r = get_ci_chi(page)
            result = analyze_ci_chi(r)
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
            raise
        time.sleep(30)
