'''
tuple;
-->tuple is collection different datatype that are represented in () and seprated by ,
-->tuple is immuttable
'''
#index
#go = ( 1,'java',[3,4],('python',78))
#print(go.index('java'))
#print(go[2][1])
'''print(go.count(('python',78)))
-----------------
'''
'''count();
syntax-- variable_name.count(item)
ex;
'''
'''go = (1,'java',[3,4],'python',78)
print(go.count(('python',78)))
print(go.count('python'))
'''

dictionary
'''
-->dict is key:value pair
-->keys and values seperated by
-->dict is represented by ()
-->keys must be immutable datatypes

 1 keys()
 details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.keys(name ))
                    
                
 2 values()
 syntax:dict.value ()
 details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.values(Ac ))

               
 
 3 items()
 #@-->syntax;dict.keys()
 
 
details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.items('Aadar' ))
                    
4 update()
#@-->syntax;dict.keys()
 
 
details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.update('gender' ))
                    

5 clear()
#@-->syntax;dict.keys()
 
 
details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.clear('pincode' ))

                    
 6 get()

#@-->syntax;dict.keys()
 
 
details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
print(details.get('name' ))

                    
details ={'name':'rama',
         'Ac':34567897,
         'Aadar':799349488116,
         'pincode':14370}
details.update({'gender':'female')}
print(details['name'])










