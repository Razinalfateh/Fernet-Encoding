
# Fernet module is imported from the  
# cryptography package 
from cryptography.fernet import Fernet 
#Input Message
message=input("Enter the mesage want to encrypt: \n")  
# key is generated 
key = Fernet.generate_key() 
  
# value of key is assigned to a variable 
f = Fernet(key) 
  
# the plaintext is converted to ciphertext 
res = bytes(message, 'utf-8')

token = f.encrypt(res)

string_token= str(token, 'utf-8')

string_key=str(key,'utf-8')



# display the ciphertext
print("Token:")

print(string_token) 

print("key:")

print(string_key)


