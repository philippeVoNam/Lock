from firebase_com import FirebaseCom

com = FirebaseCom()

quitStatus = False
status = "lock"

while not quitStatus:
    request = input("Would you like to open Pleasure Planet ? (y/n/q)")

    if request == "y":
        com.update("open")
        print("open")
    
    elif request == "n":
        com.update("lock")
        print("lock")

    elif request == "q":
        print("roger.")
        break
    
    else:
        print("invalid")