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
        print('正在获取股票%s数据' % code)
        url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
         '&end=20180226&start=20180226&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
        # url = 'http://stockpage.10jqka.com.cn/'+code+'/'
        # url='http://quote.eastmoney.com/sz002214.html';
        html = http_html.getHtml(url)
        return_str = (str(html)[-133:].replace('\'', '').strip())
        finall = return_str.split(',')
        print(finall)
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







