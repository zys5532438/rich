# 导入需要使用到的模块

from util.html import *


def getDetail(code):
    codeList = []
    for item in code:
        if item[0] == '6':
            codeList.append(item)
    # 抓取数据并保存到本地csv文件
    for code in codeList:
        print('正在获取股票%s数据' % code)
        # url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
        #  '&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        url = 'http://stockpage.10jqka.com.cn/'+code+'/'
        # url='http://quote.eastmoney.com/sz002214.html';
        html = http_html.getHtml(url)
        print(html)
        return html

if __name__ == '__main__':
   html = getDetail(['600000'])
   print(http_html.getStackCode(html, r'<div style="display:none" id="pageStockName">(.*?)</div>')) # 获取名字
   print(http_html.getStackCode(html, r'<span class="price" id="hexm_curPrice">(.*?)</span>')) # 当前价格




