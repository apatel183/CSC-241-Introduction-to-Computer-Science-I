# randomNamespacesModules.py

##### random #####

'''
random
    randrange(stop)
    randrange(start,stop)
    uniform(start,stop) - random float
    choice(indexable) - random item
    sample(indexable,size) - random sample
    shuffle( indexable ) - shuffles in place, must be mutable
    
    seed( int ) - seed to repeat sequence
    
>>> random
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    random
NameError: name 'random' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> vars()
{'__doc__': None, '__package__': None, '__spec__': None, '__name__': '__main__', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__builtins__': <module 'builtins' (built-in)>}
>>> import random
>>> vars()
{'__doc__': None, '__package__': None, 'random': <module 'random' from 'C:\\Python\\lib\\random.py'>, '__spec__': None, '__name__': '__main__', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__builtins__': <module 'builtins' (built-in)>}
>>> random
<module 'random' from 'C:\\Python\\lib\\random.py'>
>>> random.randrange(10)
8
>>> random.randrange(10)
8
...
>>> random.randrange(10)
3
>>> random.randrange(5,7)
5
>>> random.randrange(5,7)
5
>>> random.randrange(5,7)
6
>>> random.randrange(5,7)
5
>>> # die roll
>>> random.randrange(1,7)
3
>>> random.randrange(1,7)
4
>>> random.randrange(1,7)
5
>>> d1 = random.randrange(1,7)
>>> d1
1
>>> 
>>> 
>>> random.uniform(0,1)
0.6170569996059627
>>> random.uniform(0,1)
0.0354498230973066
>>> 
>>> 
>>> random.choice( [1,2,3])
3
>>> random.choice( [1,2,3])
2
>>> random.choice( [1,2,3])
1
>>> random.choice( ['apple','pear'])
'pear'
>>> random.choice( ['apple','pear'])
'pear'
>>> 
>>> # coin fli[
>>> random.choice( ['H','T'])
'H'
>>> random.choice( ['H','T'])
'T'
>>> random.choice( ['H','T'])
'T'
>>> random.choice('HT')
'T'
>>> 
>>> random.choice( {1,2,1,1,1,3})
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    random.choice( {1,2,1,1,1,3})
  File "C:\Python\lib\random.py", line 256, in choice
    return seq[i]
TypeError: 'set' object does not support indexing
>>> random.choice( list({1,2,1,1,1,3}) )
3
>>> random.choice( list({1,2,1,1,1,3}) )
1
>>> random.choice( list({1,2,1,1,1,3}) )
3
>>> random.sample(  range(10), 3)
[4, 2, 7]
>>> random.sample(  range(10), 3)
[9, 5, 1]
>>> random.sample(  'abcdefghijlk', 3)
['g', 'l', 'a']
>>> random.sample(  'abcdefghijlk', 3)
['c', 'g', 'h']
>>> 
>>> 
>>> lst = list(range(10))
>>> lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.shuffle( lst )
>>> lst
[8, 7, 5, 9, 6, 4, 1, 0, 3, 2]
>>> random.shuffle( (1,2,3))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    random.shuffle( (1,2,3))
  File "C:\Python\lib\random.py", line 272, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> random.choice('HT')
'H'
>>> random.choice('HT')
'T'
>>> random.choice('HT')
'T'
>>> random.choice('HT')
'T'
>>> random.seed(0)
>>> random.choice('HT')
'T'
>>> random.seed(0)
>>> random.choice('HT')
'T'
>>> random.seed(0)
>>> random.choice('HT')
'T'
>>> random.seed(0)
>>> [ random.choice('HT') for i in range(20)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T']
>>> random.seed(0)
>>> [ random.choice('HT') for i in range(20)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T']
>>> random.seed(1)
>>> [ random.choice('HT') for i in range(20)]
['H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T']
>>> random.seed(1)
>>> [ random.choice('HT') for i in range(20)]
['H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T']
>>> 
'''

'''
simulate dice game -- roll a pair of dice, keep
rolling as long as you have doubles, return your score,
that is the total number of all pips shown

simulation:
2 2
5 5
1 4
your score: 19

>>> diceTotal()
19
'''

import random
def diceTotal():
    
    d1,d2 = 0,0 # fake values guarantee loop entered
    total = 0
    while d1==d2:
        d1 = random.randrange(1,7)
        d2 = random.randrange(1,7)
        total += d1+d2
        #print(d1,d2)
    return total

'''
>>> maxDiceTotal(100)
... return the best score out of 100 games ...
'''

def maxDiceTotal(n):
    return max([ diceTotal() for i in range(n)])
    
'''
>>> random.seed(0)
>>> maxDiceTotal(100)
18
>>> random.seed(10)
>>> maxDiceTotal(100)
18
>>> random.seed(3)
>>> maxDiceTotal(100)
20
'''

# want to take frequencies

'''
>>> import dictTupleSet
>>> dictTupleSet.frequencies
<function frequencies at 0x02E3E4B0>
>>> dictTupleSet.frequencies( [ diceTotal() for i in range(1000)])
{3: 58, 4: 54, 5: 113, 6: 135, 7: 162, 8: 114, 9: 133, 10: 62, 11: 52, 12: 12, 13: 9, 14: 10, 15: 23, 16: 6, 17: 12, 18: 6, 19: 11, 20: 5, 21: 6, 22: 4, 23: 5, 25: 2, 27: 2, 28: 1, 34: 1, 35: 1, 37: 1}
>>> random.seed(0)
>>> dictTupleSet.frequencies( [ diceTotal() for i in range(1000)])
{3: 48, 4: 63, 5: 112, 6: 116, 7: 173, 8: 120, 9: 114, 10: 71, 11: 68, 12: 9, 13: 20, 14: 4, 15: 12, 16: 8, 17: 16, 18: 9, 19: 10, 20: 4, 21: 7, 22: 2, 23: 5, 24: 2, 25: 1, 27: 2, 29: 1, 30: 1, 31: 2}
>>> dictTupleSet.frequencies( [ diceTotal() for i in range(10000)])
{3: 572, 4: 543, 5: 1108, 6: 1100, 7: 1772, 8: 1228, 9: 1176, 10: 610, 11: 697, 12: 78, 13: 109, 14: 84, 15: 172, 16: 100, 17: 144, 18: 88, 19: 123, 20: 58, 21: 69, 22: 27, 23: 37, 24: 11, 25: 17, 26: 16, 27: 14, 28: 6, 29: 6, 30: 6, 31: 3, 32: 3, 33: 4, 34: 4, 35: 2, 36: 1, 37: 3, 38: 1, 39: 3, 40: 1, 41: 1, 43: 1, 44: 1, 46: 1}
>>> 
'''

##### namespaces #####

'''
vars() - returns the current namespace, a dictionary

how things are looked up, in order:

1) in local function namespace
2) in global/module namespace
3) builtins namespace

'''

def f(x):
    print( vars()) # 3) print,vars in builtins
    print( y )   # 2) y in global namespace
    return 2*x  # 1) x in local namespace

'''
>>> vars()['x']
2
>>> x
2
>>> y
3
>>> f
<function f at 0x02E5E468>
>>> f(y)
{'x': 3}
6
>>>

>>> x,y=2,3
>>> x
2
>>> z
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> vars()['z']=77
>>> z
77
>>> 
'''

##### import and namespaces #####
'''
more than one way to import

1) import random - import module into namespace
2) from random import randrange, import function
   into current namespace
3) from random import * - imports all functions/variables
   into current namespace  (not good practice in general)

>>> import random
>>> random.randrange(5)
1
>>> from random import randrange
>>> randrange(5)
4
>>> from random import *
>>> uniform(0,1)
0.4641804463303453
>>> 
''' 










