import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="db_mikon"
)

mycursor = mydb.cursor()

sql = "INSERT INTO arduino1 (temp, ultra, hum, ldr) VALUES (%s, %s, %s, %s)"
val = [("10 celcius", " 20 ultrasonik", "30 %", "5 ldr"),("11 celcius","21 ultrasonik","31 %","6 ldr"),("12 celcius","22 ultrasonik","32 %","7 ldr"),("13 celcius","23 ultrasonik","33 %","8 ldr"),("14 celcius","24 ultrasonik","34 %","9 ldr")]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
