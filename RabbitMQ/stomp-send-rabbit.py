import stomp
import time
import sys

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', '123456', wait=True)
conn.send(body='SUHU 10', destination='/queue/test')
conn.disconnect()
