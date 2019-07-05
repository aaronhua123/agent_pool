import requests
from gevent import monkey

import dbmodle

monkey.patch_all()
import gevent

def check_proxy(proxy):
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
        # print(e)
        return False


def check_proxy_by_gevent(proxylist):
    print('check_proxy')
    jobs = [gevent.spawn(check_proxy, proxy) for proxy in proxylist]
    gevent.joinall(jobs,timeout=20)
    return [job.value for job in jobs]


if __name__ == '__main__':
    import time
    while 1:
        httplist = [{'http':proxy.decode('utf-8')} for proxy in dbmodle.getsrandmember(protocol='http', number=20)]
        # print(httplist)
        httpslist = [{'https':proxy.decode('utf-8')} for proxy in dbmodle.getsrandmember(protocol='https', number=20)]
        # print(httpslist)
        # proxylist = [{'http': 'http://120.83.101.189:9999'}, {'https': 'https://59.32.37.161:3128'}, {'https': 'https://114.230.69.10:9999'}, {'https': 'https://117.28.97.90:8118'}, {'http': 'http://218.91.112.32:9999'}, {'http': 'http://123.169.34.7:9999'}, {'http': 'http://112.85.130.119:9999'}, {'http': 'http://59.52.101.89:8118'}, {'https': 'https://222.189.191.236:9999'}, {'http': 'http://119.41.192.60:53281'}, {'https': 'https://121.233.251.97:9999'}, {'https': 'https://112.87.70.212:9999'}, {'https': 'https://163.204.243.6:9999'}, {'http': 'http://121.233.251.250:9999'}, {'https': 'https://111.177.107.136:9999'}, {'https': 'https://113.121.20.11:9999'}, {'http': 'http://60.13.42.21:9999'}, {'http': 'http://112.85.129.25:9999'}, {'http': 'http://120.83.105.26:9999'}, {'https': 'https://112.87.69.24:9999'}, {'https': 'https://113.121.21.4:9999'}, {'https': 'https://163.204.245.250:9999'}, {'https': 'https://113.121.20.20:27473'}, {'https': 'https://122.193.244.165:9999'}, {'http': 'http://163.204.242.234:9999'}, {'http': 'http://123.163.96.237:9999'}, {'http': 'http://112.85.151.71:9999'}, {'http': 'http://112.85.171.8:9999'}, {'https': 'https://114.230.69.163:9999'}, {'http': 'http://113.121.23.25:9999'}, {'http': 'http://112.85.168.230:9999'}, {'http': 'http://120.83.104.79:9999'}, {'https': 'https://121.233.251.123:9999'}, {'https': 'https://113.120.36.203:9999'}, {'https': 'https://117.91.232.201:9999'}, {'http': 'http://112.87.68.243:9999'}, {'http': 'http://113.121.20.216:9999'}, {'https': 'https://116.208.53.201:9999'}, {'https': 'https://222.189.190.69:9999'}, {'http': 'http://222.89.32.155:9999'}, {'http': 'http://112.85.130.107:9999'}, {'https': 'https://113.121.23.252:9999'}, {'https': 'https://112.85.170.159:9999'}, {'http': 'http://59.32.37.117:8010'}, {'https': 'https://121.239.55.16:8118'}, {'http': 'http://112.85.171.216:9999'}, {'http': 'http://120.83.98.3:9999'}, {'https': 'https://112.85.171.212:9999'}, {'http': 'http://59.32.37.28:8010'}, {'http': 'http://112.85.171.200:9999'}, {'https': 'https://116.208.55.69:9999'}, {'http': 'http://49.86.179.73:9999'}, {'http': 'http://49.86.178.47:9999'}, {'http': 'http://163.204.240.152:9999'}, {'http': 'http://1.198.72.131:9999'}, {'http': 'http://111.178.181.53:37520'}, {'https': 'https://1.192.240.72:9999'}, {'https': 'https://27.40.146.23:808'}, {'https': 'https://221.227.73.11:9999'}, {'https': 'https://117.85.20.130:9999'}, {'https': 'https://1.199.31.49:9999'}, {'https': 'https://117.85.105.122:9999'}, {'http': 'http://49.73.14.216:9999'}, {'http': 'http://122.193.244.87:9999'}, {'http': 'http://36.45.160.88:8118'}, {'http': 'http://112.85.168.127:9999'}, {'http': 'http://49.84.172.94:8118'}, {'http': 'http://1.197.10.153:9999'}, {'https': 'https://125.123.142.140:9999'}, {'https': 'https://27.40.134.23:9999'}, {'https': 'https://1.197.16.5:9999'}, {'http': 'http://163.204.244.99:9999'}, {'http': 'http://222.184.7.206:40908'}, {'http': 'http://163.204.244.253:9999'}, {'https': 'https://36.248.132.143:9999'}, {'https': 'https://58.240.143.157:8118'}, {'http': 'http://1.193.158.217:9999'}, {'http': 'http://36.250.156.223:9999'}, {'http': 'http://125.120.153.83:8118'}, {'http': 'http://112.85.130.199:9999'}, {'http': 'http://58.54.69.193:27092'}, {'http': 'http://1.193.158.190:9999'}, {'https': 'https://36.250.156.160:808'}, {'http': 'http://121.227.87.215:9999'}, {'https': 'https://171.12.112.169:9999'}, {'https': 'https://1.198.110.76:9999'}, {'https': 'https://171.12.112.174:9999'}, {'https': 'https://113.64.146.3:8118'}, {'http': 'http://113.110.77.115:8118'}, {'https': 'https://122.4.41.128:9999'}, {'https': 'https://123.101.213.243:9999'}, {'http': 'http://125.90.255.74:8118'}, {'https': 'https://112.85.128.87:9999'}, {'http': 'http://113.128.24.99:25364'}, {'https': 'https://112.85.148.242:9999'}, {'https': 'https://112.85.128.251:9999'}, {'http': 'http://218.73.131.24:9999'}, {'http': 'http://58.219.63.117:9999'}, {'https': 'https://112.85.170.81:9999'}, {'http': 'http://27.40.141.25:61234'}]
        # print([*httpslist])
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