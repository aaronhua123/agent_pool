import time
import requests
from lxml import etree
import pymysql

def getquanwang():
    url = 'http://www.goubanjia.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    r = requests.get(url, headers=headers, timeout=30)
    return r

def analyzequanwang(r):
    tree = etree.HTML(r.text)
    tr_list = tree.xpath('//table/tbody/tr')
    _ = []
    for tr in tr_list:
        host_list = tr.xpath('./td[1]/*[not(contains(@style,"none"))]/text()')[:-1]
        host = "".join(host_list)
        portnum = tr.xpath('./td[1]/*[last()]/@class')[0].split(' ')[1]
        portlist = [str('ABCDEFGHIZ'.index(port)) for port in portnum]
        result = int("".join(portlist))
        port = result >> 3
        protocol = tr.xpath('./td[3]/a/text()')[0]
        _.append((f'{protocol}://{host.strip()}:{port}',protocol,))
    return _

if __name__ == '__main__':
    conn = pymysql.connect(user='root',password='root',host='127.0.0.1',port=3306,db='proxy')
    sql = 'insert into proxy.proxy_cache (proxy,protocol,modify_date) values(%s,%s,NOW())'
    while 1:
        r = getquanwang()
        result = analyzequanwang(r)
        for proxy,protocol in result:
            print(proxy,protocol)
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,args=(proxy,protocol,))
                conn.commit()
            except Exception as e:
                raise
        time.sleep(60)




