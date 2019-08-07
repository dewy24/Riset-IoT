import stomp
import os
import time
import mysql.connector

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        # print('received a message "%s"' % message)
        global var
        var = message
        print('message "%s"' % var)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="db_mikon"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO arduino1 (temp) VALUES (%s)"
        val = [(var)]

        mycursor.execute(sql, val)

        mydb.commit()


conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', '123456', wait=True)
conn.subscribe(destination='/queue/test1', id=2, ack='auto')
time.sleep(1)
conn.disconnect()
