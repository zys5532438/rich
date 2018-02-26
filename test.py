# 导入需要使用到的模块

from util.html import *
from db.jdbc import *


def getDetail(code):
    codeList = []
    for item in code:
        if item[0] == '6':
            codeList.append(item)
    # 抓取数据并保存到本地csv文件
    print(codeList.__len__())
    for code in codeList:
        html=''
        print('正在获取股票%s数据' % code)
        url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
         '&end=20180226&start=20180226&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        print(url)
        # url = 'http://stockpage.10jqka.com.cn/'+code+'/'
        # url='http://quote.eastmoney.com/sz002214.html';
        html = http_html.getHtml(url)
        if str(html).__len__()>90:
          return_str = (str(html).replace("日期,股票代码,名称,收盘价,最高价,最低价,开盘价,前收盘,涨跌额,涨跌幅,换手率,成交量,成交金额,总市值,流通市值",'').replace('\'', '').strip())
          print(return_str)
          finall = return_str.split(',')

          getSQL(finall)
          jdbc.insert(getSQL(finall))
        # print(html)
        # return html



def getSQL(list):
    sql='insert into rpt_event_record(datetime,code,name,last_price,max_price,min_price,start_price,yesterday_price,zd_amt,zd_rate,hs_rate,cj_qty,cj_amt,all_amt,lt_amt) ' \
        'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '\
        %("'"+list[0]+"'","'"+list[1]+"'","'"+(list[2])+"'",list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11],list[12],list[13],list[14])
    return sql
if __name__ == '__main__':
   url='http://quote.eastmoney.com/stocklist.html'
   html = getDetail(http_html.getStackCode(http_html.getHtml(url)))







