import threading
import time
import MySQLdb
from TransGenerator import TransGenerator

Num_Of_threads = 5

class myThread(threading.Thread):

    def __init__(self, conn, cur, transGenerator):
        threading.Thread.__init__(self)
        self.conn = conn
        self.cur = cur
        self.transGenerator = transGenerator

    def run(self):

        sql = self.transGenerator.getNext()
        while sql != 'error':
            self.cur.execute(sql)
            self.conn.commit()
            sql = self.transGenerator.getNext()

threads = []
tg = TransGenerator('low')

for i in range(Num_Of_threads):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='19921008', db='CS223')
    cur = conn.cursor()
    new_thread = myThread(conn, cur, tg)
    threads.append(new_thread)

for th in threads:
    th.start()

for t in threads:
    t.join()