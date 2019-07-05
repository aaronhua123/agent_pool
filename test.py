import requests
r = requests.get('http://127.0.0.1:5000/http', timeout=30)
proxies = r.json()
print(proxies)
# r = requests.get('http://www.testclass.net',proxies=proxies,timeout = 30)
r = requests.get('http://www.w3school.com.cn', proxies=proxies, timeout=5)
print(r.text)