import sys
import psycopg2
import TransGenerator
import threading

class PSQL_Simulator:
    def __init__(self, pw=""):
        self.conn = psycopg2.connect(dbname="proj1", user="postgres", password=pw)
        self.cur = self.conn.cursor()
        #self.set_session(isolation level)
        
    def execute(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

class PSQL_Thread(threading.Thread):
        def __init__(self, psim, tgen):
            threading.Thread.__init__(self)
            self.psim = psim
            self.tgen = tgen
            self.count = 0
            
        def run(self):
            query = self.tgen.getNext()
            while query!= 'error':
                try:
                    self.psim.cur.execute(query)
                    self.psim.conn.commit()
                    self.count += 1
                    query = self.tgen.getNext()
                except:
                    query = self.tgen.getNext()        
