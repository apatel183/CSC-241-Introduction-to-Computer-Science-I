>>> from hw2 import *

##### returnThree #####

>>> returnThree('hello')
'hel'
>>> returnThree('BYE')
'BYE'
>>> returnThree('an')
''
>>> 

##### returnN ######

>>> returnN('hello',2)
'he'
>>> returnN('hello',5)
'hello'
>>> returnN('BYE',1)
'B'
>>> returnN('BYE',10)
''
>>> 


##### firstChars #####


>>> firstChars(['hello','bye','TEST','Done'])
h
b
T
D
>>> firstChars(['first','','third'])
f
t
>>> firstChars([])
The list provided as a parameter was empty.
>>> 

##### printGreater #####

>>> printGreater([1,-3,12,-5,0],0)
1 12 
>>> printGreater([2,4,6,8,10],5)
6 8 10 
>>> printGreater([-1,-2,-3],-1)
>>> printGreater([],10)
>>> printGreater([1,2,3,4,5,6,7,8],0)
1 2 3 4 5 6 7 8 
>>> 

