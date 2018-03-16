import pymysql
db = pymysql.connect('localhost', 'root', '123456', 'world')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()
