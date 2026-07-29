
'''
#Default arguments
----------------
ex;
def any_( name,age,edu):
    print(age)
any_('Rama',21,'Bsc. computers')

ex;

def any_( name,age,edu):
    print(age)
    print(name)
any_( name 'Rama', age =21,edu ='Bsc. computers')

variables - length positional arguments
--------------------------------------
1.
*args
----
--> we can pass tuple of arguments and stored in a single parameter by just adding * before the parameters..
--> and we can access the arguments using indexing

nums = (10,23,34,5,89)
ex;

def all_va(*nums):
    print(nums[1]+nums[3])
all_va(10,34,23,5,89)    
    
2.
**kargs
-------
-->By pass keywoard arguments in the arguments,will get it as dictonary it  just adding ** before the parameters
-->And it can access by using dictionary methods..

ex:1

def dct(**all_in):
    for key, val in all_in.items():
        print(key,':',val)
dct(name='Rama',age ='21',role ='mentor')

ex:2
---
def dct_nums(*args,**kargs):
    print(args)
    print(kargs)
dct_nums(12,56,7,name='rama',age='21',edu='bsc.computers')


scope of variables
------------------
ex:

def nums( num_2):
    num = 90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)

globe of variables
-------------------
ex;
num_2 = 89
def nums( num_2):
    num = 90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)

ex:

limit_=int(input('Enter the limit'))
num = 0
num_2 = 1
def fibonocci( limit_,num,num_2):
    print(num,num_2,end='')
    for j in range(1,limit_+1):
        num_3=num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
fibonocci(limit_,num,num_2)

output:Enter the limit:10
0 11 2 3 5 8 13 21 34 55 89 


passing by values
------------------
-->pass the direct values in the arguments
ex:

def any_(a,b):
    print(a)
    print(b)
any_(8,56)    

ex:
'''
def any_(num,num_2):
    print(num)
    print(num_2)
any_( num = 8, num_2 = 56)




















    



    
    

















