import time
import requests
from lxml import etree
import dbmodle

def getquanwang():
    url = 'http://www.goubanjia.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    r = requests.get('http://127.0.0.1:5000/http', timeout=30)
    proxies = r.json()
    print(proxies)
    r = requests.get(url, headers=headers, timeout=30)
    return r

def analyzequanwang(r):
    tree = etree.HTML(r.text)
    tr_list = tree.xpath('//table/tbody/tr')
    print(tr_list)
    _ = []
    for tr in tr_list:
        host_list = tr.xpath('./td[1]/*[not(contains(@style,"none"))]/text()')[:-1]
        host = "".join(host_list)
        # print(tr.xpath('./td[1]/*[last()]/@class'),tr.xpath('./td[1]/*[last()]/text()'))
        portnum = tr.xpath('./td[1]/*[last()]/@class')[0].split(' ')[1]
        # print(portnum)
        portlist = [str('ABCDEFGHIZ'.index(port)) for port in portnum]
        # print(_)
        result = int("".join(portlist))
        port = result >> 3
        protocol = tr.xpath('./td[3]/a/text()')[0]
        print(protocol, host, port)
        _.append({
            protocol: f'{protocol}://{host}:{port}'
        })
    return _
if __name__ == '__main__':
    while 1:
        try:
            r = getquanwang()
            result = analyzequanwang(r)
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



