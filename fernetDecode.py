#!/usr/bin/python
#!/usr/bin/env python

# cryptography package 
from cryptography.fernet import Fernet

from bs4 import BeautifulSoup
from termcolor import colored
from urllib.request import urlopen
import os
import time
import socket
import datetime








time.sleep(1)
print(colored("-"*50, "blue"))
print(colored("Starting time... ", "magenta"))
time.sleep(3)
t =  datetime.datetime.now()
print(t)
print(colored("-"*50, "blue"))

print("")
print("")
time.sleep(.5)
print("                        _______                         ")
time.sleep(.5)
print("                       / .===. \                        ")
time.sleep(.5)
print("                       \/ 6 6 \/                        ")
time.sleep(.5)
print("                       ( \___/ )                        ")
time.sleep(.6)
print("  _________________ooo__\_____/_____________________    ")
time.sleep(.5)
print(" /                                                  \   ")
time.sleep(.5)
print(colored(" |         Hey, Welcome to Fernet Encoding!        |   ", "blue"))
time.sleep(.6)
print(" \______________________________ooo_________________/   ")
time.sleep(.6)
print("                       |  |  |                          ")
time.sleep(.6)
print("                       |_ | _|                          ")
time.sleep(.5)
print("                       |  |  |                          ")
time.sleep(.5)
print("                       |__|__|                          ")
time.sleep(.5)
print("                       /-'Y'-\                          ")
time.sleep(.5)
print("                      (__/ \__)                         ")
time.sleep(.5)
print(colored(" By \ ", "white")) 
print(colored("Razin", "red"))
print(colored("V 0.1", "red"))


print(colored("-" * 50, "blue"))

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






