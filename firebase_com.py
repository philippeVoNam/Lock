# * author : Philippe Vo 
# * date : Feb-28-2020 09:16:42
 
# * Imports
# 3rd Party Imports
import pyrebase
import time
# User Imports

# * Code
class FirebaseCom:
    """
    communication component to send and read data from our firebase app
    we are assuming that the data itself looks like this
    """
    def __init__(self):
        self.config = {
        "apiKey": "AIzaSyDwK1MDTqKawKrbr_GrIF6nhYjnwxdFWoo",
        "authDomain": "lock-eb626.firebaseapp.com",
        "databaseURL": "https://lock-eb626.firebaseio.com",
        "storageBucket": "lock-eb626.appspot.com"
        }

        print("Signing in to Firebase ...")
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password("philippe.vo.nam@gmail.com", "secretPassword555") # you need to make a user in Firebase first (under Authentication)
        self.db = self.firebase.database()

        # before the 1 hour expiry:
        self.user = self.auth.refresh(self.user['refreshToken']) # need this or we will have keyError

    def update(self, status):
        """
        update data to firebase for a specific plant
        Parameters
        ----------
        plant : str
            name of the plant id
        dataType : str
            type of data we want to write (moisture, name, ph, type)
        data : str
            data itself
        Returns
        -------
        """
        self.db.child("status").update({"status": status})
    
    def read(self):
        """
        read data to firebase
        """
        status = self.db.child("status").get()
        data = status.val()["status"]

        return data