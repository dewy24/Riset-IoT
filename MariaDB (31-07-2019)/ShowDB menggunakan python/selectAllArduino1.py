import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="db_mikon"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM arduino1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
