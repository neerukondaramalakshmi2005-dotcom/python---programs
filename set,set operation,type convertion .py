
'''
     SET
--->set is an unorder collection
--->set does not allows duplicate values inside it..
-->set is a mutable
---->set is represented in {}
ex;

do = {1,2,3,45,}
print(do)
#creating empty set
so = set()
print(type(so))

methods
1.update()
-------
sytax--->variable_name.update(value)
use to add new value into a set
ex

do = {1,2,3,45,}
do.update('Rama')
print(do)

output
{1, 2, 3, 'a', 'm', 45, 'R'}


2.add()
--------
use to add exact new value into a set
sytax--->variable_name.update(value)
ex

do = {1,2,3,45,}
do.add('Rama')
print(do)

 output
 {1, 2, 3, 45, 'Rama'}

3.remove()
-------------
used to del the value from the set ,incase if the value is not present in the set will get the keyerror
sytax--->variable_name.remove(value)
ex
do = {1,2,3,45,}
do.remove( 3)
print(do)

output
{1, 2, 45}
{1, 2, 45}

4.discard()
-----------
sytax---->variable_name.discard(value)
used to del the value from the set but never give any error incase value is not present inside the set
ex
do = {1,2,3,45,}
do.discard(2)
print(do)

output
1, 3, 45}
{1, 3, 45}

5.pop()
--------
sytax--->variable_name.pop(value)
used to del the value but this pop()will take 0 arguments inside it
ex
do = {1,2,3,45,}
do.pop()
print(do)

output
{2, 3, 45}
{2, 3, 45}

---operations----
1.union
-------
gives all sets value together but no duplicates
ex
do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.union(so))

output
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3}

2.intersection
---------------
common values in both sets
ex

do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.intersection(so))

output
{1, 2, 3, 4, 5}
{3}
{1, 2, 3}

3.difference
-----------
ex
do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.difference(so))

output
{1, 2, 3, 4, 5}
{1, 2}
{1, 2, 3}

-----type convertion------
1.int :
ex
num = 9
print(type(num))
so = str(num)
print(type(so))

output
class 'int'>
<class 'str'>

2.string---str
ex
num = 9.678
print(type(num))
num_ = int(num)
print(num_int)
print(type(num_int))

output
<class 'float'>
9
<class 'int'>

3.float
-------
ex;
num = 9.678
print(type(num))
num_ = int(num)
print(num_int)
print(type(num_int))

output
class 'float'>

2.string
--------
i)integer---int()
ex
how = '67'
print(type(how))
who=int(how)
print(type(who))

it conot take

how = 'i have 67 rupp'
print(type(how))
who=int(how)
print(type(who))

ii)float()
ex
how = 23.765
print(type(how))
who=float(how)
print(type(who))

iii)list()
ex
how = '23765'
print(type(how))
who=float(how)
print(type(who))

iv)tuple()
ex
how = '23765'
print(type(how))
who=tuple(how)
print(type(who))


list()
-----

**string--str()
tuple--tuple()***
ex
nums =[1,2,3,4]
print(type(nums))
all_n = str(num)
print(type(all_n))

**tuple----tuple()***
ex
nums =[1,2,3,4]
print(type(nums))
all_n = tuple(num)
print(type(all_n))

**list----list
ex
nums =[1,2,3,4]
print(type(nums))
all_n = list(num)
print(type(all_n))

**string----str
ex
nums =[1,2,3,4]
print(type(nums))
all_n = str(num)
print(type(all_n))
------------------------------------
 cancatenation(+)
 -----------
 ex
num=8
num_2=9
print(num+num_2)

output
17

ex
any_ ='python is a'
we = ' language'
print(any_+we)

output
python is a language

ex
nums = [1,2]
all_ = [3,4]
print(nums + all_)

output
[1, 2, 3, 4]

example all combination;
num = 8
num_2 = 9
print(num+num_2)
any_='python is a'
we = 'language'
print(any_+we)
nums=[1,2]
alls_=[3,4]
print(nums + all_)

'''























































































































































































































print(do)
 

