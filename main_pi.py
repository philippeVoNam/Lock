from firebase_com import FirebaseCom
from lock import Lock
import time

com = FirebaseCom()
lock = Lock()
currentState = "locked"

while True:
    time.sleep(1)
    status = com.read()
    
    if status == "open" and currentState == "locked":
        print(status)
        lock.unlock()
        currentState = "unlocked"
        
    elif status == "lock" and currentState == "unlocked":
        print(status)
        lock.lock()
        currentState = "locked"
    
    else:
        print("should not come here")