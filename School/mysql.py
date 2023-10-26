import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='root', db='Spider')
cur = conn.cursor()
cur.execute("insert into spider (title, time, article) values ('你好', '2023-5-8', '你好，spiderman')")
cur.close()
conn.commit()
conn.close()
