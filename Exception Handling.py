'''
-------------------------------- Exception  Handling----------------------------------
--------------------
--> An exception is an error can be handled bt try and except

1.try:
------
-->We can check the code here which may cantain any error
ex:

try:
    print(n)
except:
    print('some error')

                           output:
                             some error
                             
2.except:
---------
--> Exception can handle any error that come in the try block

ex:1
try:
    num = 6
    num_2 = 0
    print(num / num_2)
except:
    print("will get an error")
    num = 8
    num_2 = 0
    print("Zero Division")

    output:
       will get an error
        Zero Division

ex:2
try:
    print(9+'python')
except:
    print('error')

output:
error

ex:3

try:


3.else:
----------
--> if error in the code were raised then the else block will execute
ex:1
    
try:
    print(9+6)
except:
    print('error')
else:
    print('no error')
    
    output:
       15
       no error


ex:2
   
try:
    print(9+'python')
    print(9/6)
    print(num)
except  ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except  NameError:
    print('This will raise NameError')
else:
    print('no error')

output:
    1.5
    This will raise NameError

ex:3
    
try:
    print(9+'python')
    print(9/6)
    print(num)
except  ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except  NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise TypeError')
else:
    print('no error')


          output:
                 This will raise TypeError  
4.#finally
-------
--> The finally block will execute the error present in the try block or not

ex:1

try:
    print(9+' Hello')   
except  ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except  NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise TypeError')
else:
    print('no error')
finally:
    print('end')



------------------------------- -----File handling----------------------
---------------
--> file handling is an file handler it is an object used to connect with that particular file..

1. With(keyword)
----------------
--> by the using with keyword no need to close the file ,it will close it by itself

syntax
------
by file name
-----------
--> with open('file_name','mode') as name:

by file path
------------
--> with open(r'file_path','mode') as name:

ex:
with open('Demofile.txt','r') as file_:
    print(file_.read())

2. open()
------------
--> by using this open() we have to close the file by using close()

ex:

any_ = open('Demofile.txt','r')
print(any_.read())
any_.close()

modes
------
1. 'r'
------
--> it 'r' mode is used for  functions read() ,readline() and readlines()
ex:
with open('Demofile.txt','r') as file_:
print(file_.read())

output:


2. 'w'
-------
--> the 'w' mode is used for write() function
ex:
with open('demofile.txt','w') as file:
    file.write('time')

3. 'a':append
------
--> the 'a' mode is used for write() function and it will add the text at last position

ex:
with open('demofile.txt','a') as file:
    file.write('python is a programming')




4. 'x' : create file
---------
-->
with open('rama.txt','x') as file:
    file.write('python module take 2 hour per day')


functions
------------
1. write()

2. read():
--------
-->It will read() function will read the file check by check where we can specify the size

with open('demo.txt','r') as file:
    print(file.read(2))


3. readline():
------------
-->It will only read one line at a time

with open('demo.txt','r') as file:
    print(file.read(2))


4. readlines():
--------------
--> The readlines() will read whole file and written it in a list where each line is a one index in the list

ex:

with open('demo.txt','r') as file:
    print(file.read(2))













