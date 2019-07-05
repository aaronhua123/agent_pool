# agent_pool
一个简单的代理池（后台接口，redis）

# 原理
抓取全网代理等免费代理，保存到redis数据库，然后用flask搭建接口

# 安装方法
安装python3，安装对应的依赖库（flask，requests，lxml），安装redis数据库

# 架构图
![架构图](https://tva4.sinaimg.cn/large/007DFXDhgy1g4p3p2ojpwj30wm0fvmyb.jpg
)

# 使用方法
按照架构图，启动四个部分即可运行。
1. 启动redis数据库
2. 启动server.py（用于后台接口）
3. 启动quanwangcrawler.py（用于采集免费代理,推荐使用全网）
4. 启动checkproxy.py（用于检测代理，推送到可用的代理池）


![使用方法](https://ws3.sinaimg.cn/large/007DFXDhgy1g4p3vee9doj30cj0ar0tr.jpg
)


# 使用代理demo
```
import requests
r = requests.get('http://127.0.0.1:5000/http', timeout=5)
proxies = r.json()
print(proxies)
r = requests.get('http://www.w3school.com.cn', proxies=proxies, timeout=5)
print(r.status_code)
```

# 结果
从redis上可以看到，采集到的代理用19个，其中17个是能用的。当然，你也可以编辑crawler部分，增加更多的代理。  
![结果](https://tva4.sinaimg.cn/large/007DFXDhgy1g4p3vebq3qj309q05vaa3.jpg
)