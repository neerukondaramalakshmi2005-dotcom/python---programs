'''
#Functions
Anonymous function
----------------
-->Anonymous function is a function that don't any name
-->This also called as lambda function
--> lambda function will take n mumber arguments but only one expression

syntax --> lambda arguments : expression

ex;
so = lambda a,b,c : a+b+c  ,a-b-c ,a*b*c
print(so(2,45,6))                       output:+53,-49,*540    

1. map()
----
--> The map  function will be applied on the given function of each and every element of an itterable
                                       

ex;
nums = [1,2,3,45,]
so = list(map(lambda x: x*x,nums))
print(so)
                                         output:[1, 4, 9, 2025]
2.Filter()
-------
--> function will only consider if the condition true,then it will keep that values...
ex:
nums = [1,2,3,4,5]
so =list(filter(lambda x: x%2==0,nums))
print(so)
                                          output:[2, 4]

'''
from functools import reduce

nums = [1,2,3,4,5]

so =(reduce(lambda x,y: x+y,nums))
print(so)
                                      














                                        
