# 导入pymysql的包
import pymysql


class jdbc(object):
 def insert(sql):
  try:
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='rich', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    # sql = " INSERT INTO library ( t_name , t_automer , t_keyword , t_coden  ) VALUES (%s,%s,%s,%s );"
    print(sql)
    cur.execute(sql)  # 加载sql语句
    conn.commit()  # 提交事务
    cur.close()  # 释放游标
    conn.close()  # 释放资源
  except Exception as e:
    print("异常" + e)
