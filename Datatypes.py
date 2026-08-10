'''
# Data Types
# To find datatype--type(variable_name)
# To find memory---id(variable_name)
int
number=9
float
number=2.35638
# string
-->str is a sequence of character that are inclosed in ('',"",''' ''')
-->str is immutable
-->method

 replace()
syntax;
varable_name.replace('old_str','new_str','how many)
ex;
so="python is language"
print(so.replace('python','java'))
print(so)
used to replace old str with new str'''

'''


#@join();
sytanx;
'new_string'.join(variable_name)
this method will add the new char after every sub-str
ex;
so ='python is language'
print('_'.join(so))



#@split()
ex;
so ='python is language'
print(so.split(' '))
----------------------------

index()
so ='python is language'
print(so.index('g'))
-------------------------------
count()
so ='python is language'
print(so.count('n',1,10))
----------------------------------
indexing()
so ='python is language'
print(so[12])
------------------------------------
list
---> list is the collection of different datatypes that are represented in [] and seperated by.....
--->muttable datatypes
ex;
any_= [1,'python','vyshnavi',[5,7]]
print(any_[2][4])
-----------------------------------
methods
--->append(): append is using add
any_= [1,4,3,9,6]
any_.append("python")
print(any_)
any_.append(100)
print(any_)
-----------------------
extend;

------------------
remove;
the remove will del the item based on the value given....
if the value not the list will the error
ex
any_= [1,4,3,9,6]
any_.remove(3)
print(any_)
--------------------------
pop
remove index position
ex
any_= [1,4,3,9,6]
any_.append("python")
print(any_)
any_.append(100)
print(any_)
-----------------------
extend;

------------------
remove;
the remove will del the item based on the value given....
if the value not the list will the error
ex
any_= [1,4,3,9,6]
any_.remove(3)
print(any_)
--------------------------
pop
remove index position
ex
any_= [1,4,3,9,6]
any_.pop(3)
print(any_)
---------
            
