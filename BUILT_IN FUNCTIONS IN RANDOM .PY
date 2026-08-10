#asscii_letters --> this string module function that can give 
'''
# BUILT IN FUNCTIONS
------------------
IMPORT RAMDOM
-------------

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#asscii_letters --> this string module function that can give 
#upper and lower letters

 import string
 print(asscii_letters)
                        output:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
                                0123456789
                                !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

 
#digits --> string module function that can give number (0-9)

import string
print(string.digits)

#punctuation --> this this string module function that can give

import string
print(string.punctuation)

ex:

import random
import string
letters = string.ascii_letters
digits = string.digits
special_char = '@#*$'
punctuation = string.punctuation
all_chars = letters + digits + punctuation
password =''
for i in range(5):
    password += random.choice(all_chars)
print(password)

ex:

import random

num = random.randint(1,100)
user_opt = int(input("pick a number(1-100): "))
if user_opt == num:
    print(f'you have picked {user_opt} number')
else:
    print('Better luck next time')




ex:
'''
bank_balance = 10000
from datatime
import datatime
import sys
now = datatime.now()

while true:
    print("---Welcome to SBI ATM---")
    user_opt = int(input("\n1.withdraw \n2.Deposit \n3.Check balance \n4.exit"))
    if user_opt ==1:
       with_m = int(input('Enter the money you want to withdraw'))
       if with_m > bank_balance:
           bank_balance -= With_m        
            print(f'remaining money {bank_balance} {now.strftime("%H:%M %Y-%M-%d")}')
       else:
            print('insufficient money')
    elif user_opt == 2:
        deposit_m = int(input('Enter the money you want to deposit'))
        bank_balance += Deposit_m
        print(f'money added successfully: {bank_balance} {now.strftime("%H:%M %Y-%M-%d")}')               
    elif user_opt == 3:
        print(f'Available balance: {bank_balance} {now.strftime("%H:%M %Y-%M-%d")}')               
    elif user_opt == 4:
        sys.exit()
    else:
        print("incorrect choice")
        print('thank for visiting the ATM')
        sys.exit()
























