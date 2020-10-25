from firebase_com import FirebaseCom
from lock import Lock
import time

com = FirebaseCom()
lock = Lock()

while True:
    time.sleep(1)
    status = com.read()
    
    if status == "open":
        print(status)
        lock.unlock()
        
    else:
        print(status)
        lock.lock()
        
        