
# Fernet module is imported from the  
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
time.sleep(1)
print(colored("-"*50, "blue"))
print(colored("Starting time... ", "magenta"))
time.sleep(3)
t =  datetime.datetime.now()
print(t)
print(colored("-"*50, "blue"))

print("")
print("")
time.sleep(.2)
print("                        _______                         ")
time.sleep(.2)
print("                       / .===. \                        ")
time.sleep(.2)
print("                       \/ 6 6 \/                        ")
time.sleep(.2)
print("                       ( \___/ )                        ")
time.sleep(.3)
print("  _________________ooo__\_____/_____________________    ")
time.sleep(.2)
print(" /                                                  \   ")
time.sleep(.2)
print(colored(" |         Hey, Welcome to Fernet Encoding!        |   ", "blue"))
time.sleep(.3)
print(" \______________________________ooo_________________/   ")
time.sleep(.3)
print("                       |  |  |                          ")
time.sleep(.3)
print("                       |_ | _|                          ")
time.sleep(.3)
print("                       |  |  |                          ")
time.sleep(.3)
print("                       |__|__|                          ")
time.sleep(.3)
print("                       /-'Y'-\                          ")
time.sleep(.3)
print("                      (__/ \__)                         ")
time.sleep(.3)
print(colored(" By \ ", "white")) 
print(colored("Razin", "red"))
print(colored("V 0.1", "red"))


print(colored("-" * 50, "blue"))
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


