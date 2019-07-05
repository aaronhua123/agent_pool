import requests
from gevent import monkey

import dbmodle

monkey.patch_all()
import gevent

def check_proxy(proxy):
    '''
    检测代理池
    :param proxy:
    :return:
    '''
    try:
        if proxy.get('http'):
            r = requests.get('http://www.testclass.net', proxies=proxy, timeout=5)
            r.encoding='utf-8'
            print(r.status_code)
            print(r.text[:100])
            return proxy if r.status_code==200 else False
        else:
            r = requests.get('https://www.baidu.com', proxies=proxy, timeout=5, verify=False)
            r.encoding = 'utf-8'
            print(r.status_code)
            print(r.text[:100])
            return proxy if r.status_code==200 else False
    except Exception as e:
        return False


def check_proxy_by_gevent(proxylist):
    '''
    使用gevent包进行代理池检测
    :param proxylist:
    :return:
    '''
    print('check_proxy')
    jobs = [gevent.spawn(check_proxy, proxy) for proxy in proxylist]
    gevent.joinall(jobs,timeout=20)
    return [job.value for job in jobs]


if __name__ == '__main__':
    import time
    while 1:
        httplist = [{'http':proxy.decode('utf-8')} for proxy in dbmodle.getsrandmember(protocol='http', number=20)]
        httpslist = [{'https':proxy.decode('utf-8')} for proxy in dbmodle.getsrandmember(protocol='https', number=20)]
        checked = check_proxy_by_gevent([*httplist,*httpslist])
        for proxy in checked:
            if proxy:
                for protocol, url in proxy.items():
                    print("save ", proxy)
                    if 'https' in url:
                        dbmodle.setkey(url, protocol='https')
                    else:
                        dbmodle.setkey(url)
        time.sleep(20)