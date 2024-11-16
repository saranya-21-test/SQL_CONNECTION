import pymysql
query="CREATE TABLE STUDENT_DETAILS(SID int, SNAME VARCHAR(50),SCOURSE VARCHAR(50),SPHONE VARCHAR(10))"
con=pymysql.connect(host="localhost",user="root",password="MYSQL",database="act_db")
cur=con.cursor()
cur.execute(query)
con.commit()
print("table is created sucessfully")
con.close()
