# --------------Regular Expressions (RegEx)---------------
------------------------
--> Regular Expressions  This is a RegEx iit is used to form a search  pattern to find out the string contain sequence char or not.
--> To use this RegEx ,we need to import re module
--->

Functions
------------
1. Findall
------------
1.ex:

import re
some = 'python is a programming language'
print(re.findall('[a]',some))

output:
    ['a', 'a', 'a', 'a']

---> The searching pattern is found then, it will be gives the o/p in the list[].

2. Search
-----------
--> This is also used to form a search pattern, but it will be give only the first matched object.
--> Where it will gives with the index positions, where the matched object is found by the pattern

ex:

import re
some = 'python is a programming language'
print(re.search('[a]',some))

output:
    
<re.Match object; span=(10, 11), match='a'>

ex:

import re
do = 'I have 1000 rupees with me'
print(re.search('0',do))

output:
    
<re.Match object; span=(8, 9), match='0'


 meta characters
 ----------------
 
---> meta characters are the symbols used in the search pattern
1. []
---> this [] symbol is used find a group char that present in the string,where
we can also specify the range

sytanx:

---> re.findall('[range]',variable_name)
--> by using this symbol we can search cap(A-Z),small(a-z and digit(0-9)

ex:
import re
some = ' This is all also Alphbetics  is a 26'
print(re.findall('[A-Z]',some))
print(re.findall('[aeiou]',some))
print(re.findall('[a-z]',some))
print(re.findall('[0-9]',some))
print(re.search('[a-z]',some))

output:
 ['T', 'A']
['i', 'i', 'a', 'a', 'o', 'e', 'i', 'i', 'a']
['h', 'i', 's', 'i', 's', 'a', 'l', 'l', 'a', 'l', 's', 'o', 'l', 'p', 'h', 'b', 'e', 't', 'i', 'c', 's', 'i', 's', 'a']
['2', '6']
<re.Match object; span=(2, 3), match='h'>


2. . char
---------
--> This symbol will refer only one mean can match only a single char in the patrern...
syntax
----> re.search('C...',variable_name)
ex:

He--0

import re
some = 'Python Is A Hello! World'
print(re.findall('H...o',some))
print(re.findall('....H',some))
print(re.search('....H',some))

output:
 ['Hello']
['s A H']
<re.Match object; span=(8, 13), match='s A H'>




3. +
-----
--> The symbol max number of sequence from the string is from a atleast one character
syntax:
-------
--> re.findall('.+',variable_name)

ex:
import re
some = ' The symbol is used to find the group of char that present'
print(re.findall('T.+r',some))
print(re.findall('T.+r',some))

output:
['The symbol is used to find the group of char that pr']
['The symbol is used to find the group of char that pr']


4. ^
------
--> The symbol is used to find the pattern where string is a starting match or not
syntax:
-----
--> re.findall('^',variable_name)
ex:
import re
some = 'Hello! World'
print(re.search('^Hello',some))
print(re.findall('^Hello',some))

output:
<re.Match object; span=(0, 5), match='Hello'>
['Hello']


5. $
------
--> This symbol will find out if the string is ending with pattern or not

ex:
import re
any_ = 'Hello World'
print(re.search('Hello World$',any_))
print(re.findall('Hello World$',any_))

output:
    
<re.Match object; span=(0, 11), match='Hello World'>
['Hello World']

6. ?
-----
--> This symbol will  find max upto 1 match in a string
syntax:
------
--> re.findall('.?',variable_name)

ex:
import re
some = 'Hello! World Hello'
print(re.findall('Hell.?o',some))

output:
    
['Hello', 'Hello']



7. *
-----
-->  This symbol is max  number of sequence
syntax:
-----
-->re.findall('T.*r',variable_name)
ex:
import re
some = ' The symbol is used to find the group of char that present'
print(re.findall('T.*r',some))
output:
['The symbol is used to find the group of char that pr']



8. {}
------
--> This  symbol is used to find a group char that is present in a string
syntax:
-------
--> re.findall('I.{size}',variable_name))

ex:

import re
any_ = 'I have a 5000 ruppees with me'
print(re.findall('I.{15}',any_))
print(re.search('I.{2}',any_))

output:
['I have a 5000 ru']
<re.Match object; span=(0, 3), match='I h'>


ex:
import re
user_name = input("please enter your name:")
pattern = re.findall('^[a-z,A-Z]{0-100,}$',user_name)
pattern = re.search('^[a-z,A-Z]{3,}$',user_name)

if pattern:
    print('correct')
else:
    print('in correct')


ex:
import re
num = input("please enter a number:")
fnd = re.findall('^[6-9][0-9]{9}$',num)
if fnd:
    print('Indian')
else:
    print('not indian')

output:
    please enter a number:9876654456
    Indianr
    please enter a number: 9987654323
     not  indian
