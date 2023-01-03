from api import addacc,accdict 
  
print("Add Account to authenticator")

name = input("Enter Name:")
token = input("Enter token: ")  

print(addacc(name,token))
