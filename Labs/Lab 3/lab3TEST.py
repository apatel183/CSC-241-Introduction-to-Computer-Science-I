[3,7,22]
[-12.3,77.2,99]
[]

>>> from lab3 import *
>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('lab3TEST.py')



##### print3Chars #####

>>> print3Chars(['hello','goodbye','no','','later'])
hel
goo
no
<BLANKLINE>
lat
>>> print3Chars(['a','b'])
a
b
>>>

##### avgLst #####

>>> avgLst()
Please enter a list: 10.666666666666666
>>> avgLst()
Please enter a list: 54.63333333333333
>>> avgLst()
Please enter a list: n/a
>>>


##### magnitude #####


>>> magnitude( [3,4,11,22])
22
>>> magnitude( [3,-4,11,-22])
22
>>> magnitude( [])
'n/a'
>>>

##### printevens #####

>>> printevens( [3,4,11,22])
4
22
>>> printevens( [3,5,11,19])
>>> printevens([])
Sorry, that list is empty.

##### printDivisors #####

>>> printDivisors(12)
1
2
3
4
6
12
>>> printDivisors(17)
1
17


>>> sys.stdin = si  # return stdin
