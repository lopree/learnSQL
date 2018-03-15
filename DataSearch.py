import pymysql
db = pymysql.connect('127.0.0.1', 'root', '123456', 'world')
cursor = db.cursor()
# SQL 查询语句
sql = "select Name from city where CountryCode = 'CHN'"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        CityName = row[0]
        # 打印结果
        print("CityName=%s" % CityName)
except:
    print("Error: unable to fecth data")
