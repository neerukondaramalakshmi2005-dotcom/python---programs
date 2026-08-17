'''polymorphism
-----------------
super() method
---------------
--> This super() method is used to get the constructor from the parent and use in the child class

--> And also can get any method from the class...


class person:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role
        print('person constructor called')
class employee(person):
    def __init__(self,name,age,salary,role):
        super().__init__(name,age,role)
        self.salary = salary
        print('employee constructed called')
obj = employee('Rama',21,100,'pythonDevelpoer')
print(obj.name)
print(obj.age)
print(obj.salary)
print(obj.role)

output:
person constructor called
employee constructed called
Rama
21
100
pythonDevelpoer


class all:
    def job_(self):
        print("I'm looking for job")
class looking(all):
    def job_(self):
        print("we are looking for candiadate")
    def an_(self):
        super().job_()
        print("No jobs")
any_ =looking()
any_.an_()

output:
     ================================================
I'm looking for job
No jobs

Ploymorphism
--------------
--> ploymorphism is means a same name but different forms
Types of ploymorphism
---------
1. method overloading
---------------------
--> This method is overloading happens in a class a method is created this same name ,
but the recent method will be activated before one will not the considered

ex:
class data_:
    def add_(self,a,b,c=0):
        return a+b+c
    def add_(self,a,b,c):
        return a+b+c
    def add_(self,a,b,c,d):
        return a+b+c+d
obj = data_()
print(obj.add_(2,3,9,7))

output:
    21


2.method overriding
-------------------
--> This method overriding happens when parent class and child class have
the same method and the child take its own implementation

ex:
class pay:
    def payment(self):
        print('payment called')
class UPI(pay):
    def payment(self):
        print('UPI payment called')
class paytm(pay):
    def payment(self):
        print('paytm payment called')

obj = pay()
obj.payment()
go = paytm()
go.payment()


3. operation overloading
-----------------------
-->  Operation  overloading which gives special meaning to the operator when it is called by object

1. __add__ +
2. __sub__ _
3. __mul__ *
4.__truediv__ /


ex:
class cal:
    
    def __add__(self,a,b):
        print(a+b)
how=cal()
how.__add__(7,8)

output:
15
 1. ___add__
 
class cal:
    def __init__(self,any_):
        self.any_ = any_
    
    def __add__(self,do):
        print(self.any_ + do.any_)
how=cal(98)
who=cal(45)
how.__add__(who)

output:
    143



2. __truediv__

class cal:
    def __init__(self,any_):
        self.any_ = any_
    
    def __truediv__(self,do):
        
        print(self.any_ / do.any_)
how=cal(98)
who=cal(45)

print(how / who)

output:
    
2.1777777777777776
None

3. __sub__
class cal:
    def __init__(self,any_):
        self.any_ = any_
    
    def __sub__(self,do):
        
        print(self.any_ - do.any_)
how=cal(98)
who=cal(45)

print(how - who)

output:
    53
    None

4. __mul__

class cal:
    def __init__(self,any_):
        self.any_ = any_
    
    def __mul__(self,do):
        
        print(self.any_ * do.any_)
how=cal(98)
who=cal(45)

print(how * who)

output:
    4410
    None

































