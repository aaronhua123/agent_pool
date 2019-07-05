import redis

poolhttp = redis.ConnectionPool(host='localhost', port=6379, db=0)
poolhttps = redis.ConnectionPool(host='localhost', port=6379, db=1)
poolset = redis.ConnectionPool(host='localhost', port=6379, db=2)
rhttp = redis.Redis(connection_pool=poolhttp)
rhttps = redis.Redis(connection_pool=poolhttps)
rset = redis.Redis(connection_pool=poolset)

def sethttp(value):
    '''
    集合？
    :param url:
    :return:
    '''
    return rset.sadd("httpprotocol", value)  # 向集合添加元素
    # print(r.smembers(key)) # 获取所以集合

def sethttps(value):
    '''
    集合？
    :param url:
    :return:
    '''
    return rset.sadd("httpsprotocol", value)


def getsrandmember(protocol='http', number=1):
    '''
    随机获取元素，返回byte列表
    :param name:
    :param number:
    :return:
    '''
    if protocol == 'http':
        return rset.srandmember('httpprotocol', number)  # 随机获取两个集合
    elif protocol == 'https':
        return rset.srandmember('httpsprotocol', number)


def setkey(url, protocol='http'):
    if protocol == 'http':
        return rhttp.set(url, protocol, ex=600)
    elif protocol == 'https':
        return rhttps.set(url, protocol, ex=600)

def getkey(protocol='http'):
    if protocol == 'http':
        key = rhttp.randomkey()
        return key
    elif protocol == 'https':
        key = rhttps.randomkey()
        return key

def getkeys():
    key = rhttp.keys()
    keys = rhttps.keys()
    return {'http':key,'https':keys}


# if __name__ == '__main__':
#     print(setkey("http://127.0.0.1:123"))
#     print(setkey("https:/11616:123",protocol='https'))