# cryptography package 
from cryptography.fernet import Fernet 

#user input the key 
key=input("Enter the key: ")
token=input("Enter the token: ")

#convert string to bytes
key_bytes = bytes(key, 'utf-8') 
token_bytes = bytes(token, 'utf-8') 

#value of key is assign to a variable
f = Fernet(key_bytes) 


# decrypting the ciphertext 
d = f.decrypt(token_bytes) 

string_decryption=str(d,'utf-8')
  
# display the plaintext 
print("Message Decryption:")
print(string_decryption) 






