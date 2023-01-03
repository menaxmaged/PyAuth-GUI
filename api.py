import pyotp
import time
import csv
import pickle
import os

otpsfile= ".priv"


def getdata():
 try:
    with open(otpsfile, "rb") as myFile:
        accdict = pickle.load(myFile)
        return accdict

 except:
    accdict={}
    return accdict

     
accdict=getdata()


def savedata():
 with open(otpsfile, "wb") as myFile:
    pickle.dump(accdict, myFile)

def verifyOTP(token,otp):
  totp = pyotp.TOTP(token)
  return totp.verify(otp) # => True

 


def getOTP(token):
 totp = pyotp.TOTP(token)
 otp = totp.now()
 return otp




def addacc(accname,token):
  if accname not in accdict.keys():
   accdict[accname]=token
   savedata()
   return accname + " Added Succesfully"
  else:
    return "alreadyhere"

 

def clear():
  # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')