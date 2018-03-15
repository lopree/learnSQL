import pymysql
db = pymysql.connect('127.0.0.1','root','123456','world')
cursor =  db.cursor()
sql = "insert into student(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values ('Rook','Stein',25,'M',2000)"
try:
    cursor.execute(sql)
    db.commit()
except :
    db.rollback()

db.close()