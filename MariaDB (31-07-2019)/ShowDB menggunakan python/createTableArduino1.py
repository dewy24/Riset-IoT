import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="db_mikon"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE arduino1 (temp VARCHAR(100), ultra VARCHAR(100), hum VARCHAR(100), ldr VARCHAR(100))")
