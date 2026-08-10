
'''
#star pattern programs
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' *(2* i -1))
    
output
    
   *
   ***
  *****
 *******
*********
ex;
rows = 5
for i in range( rows, 0, -1):
    print(' ' * (rows - i) + '*' *(2* i -1))
    
output

*********
 *******
  *****
   ***
    *
ex;
#upper half
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' *(2* i -1))
#lower half
rows = 5
for i in range( rows, 0, -1):
    print(' ' * (rows - i) + '*' *(2* i -1))
    
output

    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

ex;
import math
def main():
    q = math.tan(math.pi * 0.4)
    w = math.tan(math.pi * 0.2)

    n = int(input("Enter the size\n"))
    
    for j in range(math.ceil(n * q),-1,-1):
        for i in range(-math.ceil(0.55 * n * q / w - n),math.ceil(0.55 * n * q / w - n)):
            if  (j <= 0.55 * n * q and j >= (i + n) * w and j >= (n - i) * w)or \
                (j >= (i + n) * w and j <= (i + n) * q and j <= (n - i) * q )or \
                (j <= (n - i)* q and j >= (n - i) * w and j <= (i + n) * q):
                print("*",end="")
            else:
                print("", end="")
                print()
     if__name__ == "_main_"
     main()

 ex;
import calendar
year = int (input("Enter year:"))
month = int (input("Enter month:"))
cal = calendar.month(year,month,)
print(cal)

output:
    output:
Enter year:2025
Enter month:6
     June 2025
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

ex;
#upper decrement
for i in range(5, 0, -1):
    print('*' *i)
#lower increment
for i in range(2,6):
    print('*' *i)
    
output:    
*****
****
***
**
*
**
***
****
*****

    
ex:
for i in range (1,5):
    for j in range (1,1+i):
         print(j, end ='')
    print()

for i in range (5 , 0 ,-1):
    for j in range (1,1+i):
         print(j, end ='')
    print()
    
output:
1
12
123
1234
12345
1234
123
12
1

ex
for i in range (1,6):
    for j in range(1,1+i):
        print(j,end = '')
    print()    
for i in range (1,6):
    for j in range(1,1+i):
        print(j,end = '')
    print()
output:    
1
12
123
1234
12345
1
12
123
1234
12345
ex:
for i in range(1,5):
    for j in range(i):
        print(chr(65+j),end='')
    print()

for i in range(5, 0,-1):
    for j in range(i):
        print(chr(65+j),end='')
    print()
    
for i in range(2,6):
    for j in range(i):
        print(chr(65+j),end='')
    print()
    
output:
A
AB
ABC
ABCD
ABCDE
ABCD
ABC
AB
A
AB
ABC
ABCD
ABCDE

ex;
'''
import math
def main():
    q = math.tan(math.pi * 0.4)
    w = math.tan(math.pi * 0.2)

    n = int(input("Enter the size\n"))
    
    for j in range(math.ceil(n * q),-1,-1):
        for i in range(-math.ceil(0.55 * n * q / w - n),math.ceil(0.55 * n * q / w - n)):
            if  (j <= 0.55 * n * q and j >= (i + n) * w and j >= (n - i) * w)or \
                (j >= (i + n) * w and j <= (i + n) * q and j <= (n - i) * q )or \
                (j <= (n - i)* q and j >= (n - i) * w and j <= (i + n) * q):
                print("*",end="")
            else:
                print("", end="")
        print()
                
    if __name__ == "__main__":
        main()












    

    

