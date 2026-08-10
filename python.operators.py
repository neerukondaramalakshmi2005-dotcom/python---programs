#python operators
'''
 1 .Arithmetic operators
 Arithmetic operators are used to perform
mathematical operations on numbers.

 operators| meaning Example
 "+"|Addition|"5+3=8"
 "-"|Subtraction|"5-3=8"
 "*"|multiplication|"5*3=15"
 "/"|Division| " 10 / 2 = 5.0 "
 "//"|Floor Division |"// 3 = 3"
 "%"|modulus ( Remainder )|"10 % 3 = 1"
 "**"|Exponent (power)|"2**3=8"


#python Example

a=10
b=3   
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

output

Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor division: 3
Modulus: 1
Exponent: 1000


'''
# 2. Assignement operators
'''
Assignement operators are used to assign values to variables and update their values .

Operator| Meaning| Example
"="| Assign| "a = 10"
"+="| Add and assign| "a += 5"
"-="| Subtract and assign| "a -= 5"
"*="| Multiply and assign| "a *= 5"
"/="| Divide and assign| "a /= 5"
"//="| Floor divide and assign| "a //= 5"
"%="| Modulus and assign| "a %= 5"
"*="| Exponent and assign| " a *= 2

Example'''

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /=4 
print("After /= :", a)

a //= 2
print("After //= :", a)

a %= 3
print("After %= :", a)

a**=2
print("After **=:",a)

output

After +=  15
After -=  12
After *=  24
After /=  6.0
After //=  3.0
After %=  0.0
After **= 0.0

'''

3.#comparison operators

 comparison operators are used to compare  two values .They always return a Boolean value:
True or False.

Operator| Meaning| Example
"=="| Equal to| "5 == 5"
"!="| Not equal to| "5 != 3"
">"| Greater than| "8 > 5"
"<"| Less than| "3 < 7"
">="| Greater than or equal to| "8 >= 8"
"<="| Less than or equal to| "5 <= 7"

example

a= 10
b = 5
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
'''
output;
Equal to: False
Not equal to: True
Greater than: True
Less than: False
Greater than or equal to: True
Less than or equal to: False
Practice Questions
'''

4.Membership Operators

Membership operators are used to check whether a value exists in a sequence such as a string, list, tuple, or set. They return a Boolean value: True or False.

Operator| Meaning| Example
"in"| Returns "True" if the value exists in the sequence| "'a' in "apple""
"not in"| Returns "True" if the value does not exist in the sequence| "'z' not in "apple""


example'''
colors = ["red", "green", "blue"]
print("red" in colors)
print("yellow" in colors)
print("green" not in colors)
print("black" not in colors)

'''output;

True
False
False
True

5.Identity Operators

Identity operators are used to check whether two variables refer to the same object in memory. They return a Boolean value: True or False.

Operator| Meaning| Example
"is"| Returns "True" if both variables refer to the same object| "a is b"
"is not"| Returns "True" if both variables refer to different objects| "a is not b" 

is not"| Returns "True" if both variables refer to different objects| "a is not b" 

example'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)
print("a is not c:", a is not c)

'''output;

a is b: True
a is c: False
a is c: False
a == c: True
a is not c: True

6.Logical Operators

Logical operators are used to combine two or more conditions. They return a Boolean value: True or False.
Operator

Example'''
#and
'''Returns True if both conditions are True
a > 5 and b < 10
or
Returns True if at least one condition is True
a > 5 or b < 10
not
Reverses the result (True becomes False and vice versa)'''

'''7.Bitwise Operators
Bitwise operators perform operations on the binary (bits) representation of integer

7.Bitwise Operators
Bitwise operators perform operations on the binary (bits) representation of integers.
Operator


&
Bitwise AND
5 & 3
`
`
Bitwise OR
^
Bitwise XOR
5 ^ 3
~
Bitwise NOT
~5
<<
Left Shift
5 << 1
>>
Right Shift
5 >> 1

example '''

a = 5
b = 3
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

'''Output

AND: 1
OR: 7
XOR: 6
NOT: -6
Left Shift: 10
Right Shift: 2'''

  
