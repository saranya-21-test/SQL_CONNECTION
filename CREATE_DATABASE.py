import pymysql
#write a query to create a database on specific mysql software
query="CREATE DATABASE ACT_DB"
#write a code to establsh connection betwee python and mysql
con=pymysql.connect(host="localhost",user="root",password="MYSQL")

#cursor to make database access as global or concurrent
cur=con.cursor()
#write a code to execute ur desired query
cur.execute(query)
#call commit method
con.commit()
#once the query executed , then close connection
print("database created successfully")
con.close()