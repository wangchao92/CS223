import threading
from psql_simulator import PSQL_Simulator, PSQL_Thread
import TransGenerator

NUM_THREADS = 5

threads = []
trans1 = TransGenerator.TransGenerator("low")

for i in range(NUM_THREADS):
    psim = PSQL_Simulator("qazwsx")
    new_thread = PSQL_Thread(psim, trans1)
    threads.append(new_thread)
##next_trans = trans1.getNext()
##print(next_trans)
##psim = cs223_psql_simulator.PSQL_Simulator("qazwsx")
##psim.execute(next_trans)
for th in threads:
    th.start()

for t in threads:
    t.join()

count = 0
for t in threads:
    count += t.count
    
print(count)
