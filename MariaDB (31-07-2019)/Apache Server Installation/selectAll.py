#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import mysql.connector
import json
print 'Content-type: text/html\n\n'
print '<h1>Python Script Test</h1>'


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="db_mikon"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM arduino1");
myresult = mycursor.fetchall();

row_headers=[x[0] for x in mycursor.description]
json_data=[]
for result in myresult:
   json_data.append(dict(zip(row_headers,result)))
   json_data.reverse()
print (json.dumps(json_data))
