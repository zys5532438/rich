# 导入需要使用到的模块
import urllib.request
import re

class http_html(object):

 # 爬虫抓取网页函数
 def getHtml(url):
    request = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/50.0.2657.3 Safari/537.36'
    })
    html = urllib.request.urlopen(request).read()
    print(html);
    html = html.decode('UTF-8')
    return html


 # 抓取网页股票代码函数
 def getStackCode(html,s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'):
    pat = re.compile(s)
    code = pat.findall(html)
    return code