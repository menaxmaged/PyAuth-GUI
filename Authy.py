from api import *
import pyotp
def huh():
 for account, token in accdict.items():
    print("--------------------")
    print("User: ", account)
    print("OTP:", getOTP(token))
    print("--------------------")
    
