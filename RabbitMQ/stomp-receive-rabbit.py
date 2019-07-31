import stomp
import os
import time

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', '123456', wait=True)
conn.subscribe(destination='/queue/test', id=1, ack='auto')
time.sleep(1000)
conn.disconnect()
