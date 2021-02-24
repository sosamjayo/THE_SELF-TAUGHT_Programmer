import queue
import time
import random

def simulate_line(till_show, max_time):
    q = queue.Queue()
    tix_sold = []
    
    for i in range(100):
        q.put("person" + str(i))
    
    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not q.empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = q.get()
        print(person)
        tix_sold.append(person)
    
    return tix_sold


sold = simulate_line(20, 3)
print(sold)