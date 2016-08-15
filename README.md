# GetProxy - Using python to get some proxies.
## 优雅的使用Python爬取网上的免费代理. 

### 安装
1. 下载(克隆)代码
2. 将文件 GetProxy.py 和 Data.json 拷贝至您工程目录下.
3. 在您需要调用此模块的文件顶部添加代码:
```python
import GetProxy
```

---
### 使用
1.在您需要获取代理的位置添加代码用以实例化对象:
```python
proxies = GetProxy()
```
2.通过迭代get_proxy函数获得代理地址:
```python
for x in proxies.get_proxy(provider, pattern, quantity):
```
|   参数   |   类型   |           说明           |
|----------|----------|--------------------------|
| provider |   str   |代理提供商, 详见 Data.json |
| pattern  |   str   |代理类型, 详见 Data.json |
| quantity |   num   |数量, 欲获取的代理数量 |
3.通过迭代器和requests模块访问网络
```python
requests.get("http://www.baidu.com", proxies=x)
```
####例
```python
proxies = GetProxy()
for x in proxies.get_proxy('xici', 'cn_transparent', 100):
	requests.get("http://8023.Moe", proxies=x)
```
从西刺代理网获取100个国内透明代理, 并使用代理访问 http://8023.Moe

---
###贡献
本模块分离了代码部分与配置部分, 通过读取配置文件读取url地址与正则表达式进行爬取.

配置文件为目录下的 Data.json,

Data.json 为UTF-8编码的json文件, 包含数个键为 provider 的数据.
- provider键名应存储代理商名称, 如 'xici' 或 'kuai'

每个 provider 键的值中分别必须含有 re 和 maxpage 键, 值为获取代理和页面数量的正则表达式:
- 协议可以通过内建正则表达式 {scheme} 替代
- 主机地址可以通过内建正则表达式 {host} 替代
- 端口号可以通过内建正则表达式 {port} 替代
- 最大页可以通过 {maxpage} 替代

除了 re 和 maxpage 键以外还必须含有一个或一个以上的 pattern 键
- pattern 应存储代理页面url地址, 
如"cn_transparent"用于存储国内透明代理, "intl_anonymous"用来存取国际匿名代理.
- url中页面部分请用 {page} 代替

---
###注:
- 该模块未添加至pip库.
- 欢迎大家贡献代理页面地址
- 该软件持续更新, 以后会增加错误处理, 多线程等内容.
