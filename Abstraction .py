#-----------Abstraction-------------
------------
--> Abstraction means hiding the implemented data and showing only need data to user
--> ABC (Abstract Base Class)
--> The abstractmethod is used to hide that particular information of base class
ex:1

from abc import ABC,abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('Government interest is 3.5')
class SBI_bank(gov_bank):
    def interest(self):
        print('SBI bank interest is 7.8')
class ICICI_bank(gov_bank):
    def interest(self):
        print('ICICI bank interest is 8.9')
obj = SBI_bank()
obj.interest()
obje =ICICI_bank()
obje.interest()

output:
SBI bank interest is 7.8
ICICI bank interest is 8.9


ex:2
from abc import ABC,abstractmethod
class cls_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print('college fee 45000')
class manag(cls_fee):
    def fee_str(self):
        print('college fee 100000')
class Em_(cls_fee):
    def fee_str(self):
        print('college fee 15000')
obj = manag()
obj.fee_str ()
gov = Em_()
gov.fee_str()

output:
    college fee 100000
    college fee 15000

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
cex:3
--> create a cal using add method it should be display the arguments
--> create a class vechicle child class like bike or car


class Vehicle:
    def veh(self):
        print(' This Vehicle')
class Bike(Vehicle):
    def bi(self):
        print('This is a Bike')
class Car(Vehicle):
    def ca(self):
        print('This ia a Car')
b = Bike()
b.bi()
c = Car()
c.ca()

        























    

