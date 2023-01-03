from api import *
if accdict:
 for account, token in accdict.items():
     print("--------------------")
     print("User: ", account)
     print("OTP:", getOTP(token))
     print("--------------------")
else:
  print("Please Add Your Tokens in addacc.py")
  exit()      
 