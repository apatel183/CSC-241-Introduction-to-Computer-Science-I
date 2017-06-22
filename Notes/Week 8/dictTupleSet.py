# dictTupleSet.py

##### dict(ionary) #####

'''

want to store and retrieve phone numbers

names = ['fred','sue','sally']
nums = [222,444,555]

or

[ ('fred',222), ('sue',444),...]

or

use a dict(ionary)!!!!!



dict:
    {} empty dict
    {key:value, key:value,...}
    like a list, but indexed by key
    keys are unique, values are not
    not ordered
    dictionary is mutable
    keys must be IMMUTABLE

operators
    in, not in - work on KEYS
    d[key] - retrieves value
    d[key]=value - assigns a value
    can iterate over keys

methods
    .items(), .keys()
    .pop(key) - removes pair, returns value
    .update(dict2)
    
    
    

>>> phonenums = {'fred':222, 'sue':444, 'sally':555}
>>> phonenums
{'fred': 222, 'sally': 555, 'sue': 444}
>>> hash('fred')
1737008176
>>> hash('sue')
2023667451
>>> hash('sally')
1830288504
>>> phonenums['sally']
555
>>> phonenums['axel'] = 333  # new entry
>>> phonenums
{'fred': 222, 'sally': 555, 'sue': 444, 'axel': 333}
>>> hash('axel')
-711706747
>>> phonenums['axel'] = 666
>>> phonenums
{'fred': 222, 'sally': 555, 'sue': 444, 'axel': 666}
>>> # in works on keys
>>> 555 in phonenums
False
>>> 'sally' in phonenums
True
>>> for name in phonenums:
	print(name,end=' ')

	
fred sally sue axel 
>>> for name in phonenums:
	print(name,phonenums[name])

	
fred 222
sally 555
sue 444
axel 666
>>> phonenums
{'fred': 222, 'sally': 555, 'sue': 444, 'axel': 666}
>>> # cannot edit keys directly
>>> phonenums.pop( 'sue')
444
>>> phonenums
{'fred': 222, 'sally': 555, 'axel': 666}
>>> phonenums['Sue'] = 444
>>> phonenums
{'fred': 222, 'sally': 555, 'Sue': 444, 'axel': 666}
>>> phonenums[ ['Trump','Donald'] ] = 111
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    phonenums[ ['Trump','Donald'] ] = 111
TypeError: unhashable type: 'list'
>>> # list mutable, bad for keys
>>> # tuples are ok
>>> phonenums[ ('Trump','Donald') ] = 111
>>> phonenums
{'fred': 222, 'sally': 555, 'Sue': 444, 'axel': 666, ('Trump', 'Donald'): 111}
>>> phonenums.keys()
dict_keys(['fred', 'sally', 'Sue', 'axel', ('Trump', 'Donald')])
>>> phonenums.pop( ('Trump', 'Donald') )
111
>>> list(phonenums.keys()).sort()
>>> lst = list(phonenums.keys()).sort()
>>> lst = list(phonenums.keys())
>>> lst.sort()
>>> lst
['Sue', 'axel', 'fred', 'sally']
>>> phonenums.values()
dict_values([222, 555, 444, 666])
>>> 
>>> phonenums2 = {'fred':7777, 'george':555}
>>> phonenums
{'fred': 222, 'sally': 555, 'Sue': 444, 'axel': 666}
>>> phonenums.update( phonenums2 )
>>> phonenums
{'fred': 7777, 'Sue': 444, 'axel': 666, 'sally': 555, 'george': 555}
>>> 
'''

##### tuple #####
'''
tuple
    like a list, but immutable
    use () instead of []
    otherwise quite similar
    can be used as dict keys

'''

'''
make this work:
>>> frequencies('sentence')
{ 's':1, 'e':3, ....}
'''

def frequencies( iterable ):

    freqs={} # empty dictionary

    # iterate over string/iterable
    for item in iterable:    

        # if item does not have entry
        # in dict, make an entry with count of 1
        if item not in freqs:
            freqs[item]=1
        # if it does
        # increase count by 1
        else:
            freqs[item]+=1
    # give freqs back
    return freqs

'''
>>> frequencies('sentence')
{'t': 1, 'e': 3, 'c': 1, 's': 1, 'n': 2}
>>> 

>>> frequencies('sentence')
{'t': 1, 'e': 3, 'c': 1, 's': 1, 'n': 2}
>>> frequencies(open('dictTupleSet.py').read())
{'D': 6, 'x': 16, ...}
>>> frequencies( [1,2,213,2,3,1,1,1,5])
{1: 4, 2: 2, 3: 1, 213: 1, 5: 1}
>>> frequencies( frequencies( [1,2,213,2,3,1,1,1,5]) )
{1: 1, 2: 1, 3: 1, 213: 1, 5: 1}
>>> 

'''

##### set #####

'''
set - like a list but
    items are UNIQUE!
    i.e., no duplicates
    {item,item,item,...}
    set() - to get empty set
    iterable but not ordered

operators
    in, not in

methods
    add
    remove
    intersection
    union
    
>>> # set
>>> s = {2,3,4,2,2,2,4,5,7,3,9}
>>> s
{2, 3, 4, 5, 7, 9}
>>> 8 in s
False
>>> 3 in s
True
>>> for item in s:
	print( item, end=' ')

	
2 3 4 5 7 9 
>>> len(s)
6
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s[2]
TypeError: 'set' object does not support indexing
>>> s.add(99)
>>> s
{2, 3, 4, 5, 99, 7, 9}
>>> s.add(9)
>>> s
{2, 3, 4, 5, 99, 7, 9}
>>> s = {}  # creates a dict
>>> type(s)
<class 'dict'>
>>> s = set()
>>> s
set()
>>> t = set( range(10))
>>> t
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> t.remove(5)
>>> t.remove(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    t.remove(5)
KeyError: 5

>>> s = range(-3,4)
>>> t
{0, 1, 2, 3, 4, 6, 7, 8, 9}
>>> s = set(range(-3,4))
>>> s
{0, 1, 2, 3, -3, -2, -1}
>>> t = set(range(3,8))
>>> t
{3, 4, 5, 6, 7}
>>> s.intersection(t)
{3}
>>> s.union(t)
{0, 1, 2, 3, 4, 5, 6, 7, -3, -2, -1}

'''

'''
make this work:
>>> hasDuplicates( [2,3,4,5,2,5])
True
>>> hasDuplicates( [2,3,4])
False
>>> hasDuplicates('sentence')
True
'''

def hasDuplicates(lst):

    '''
    if len(lst)!=len(set(lst)):
        return True
    else:
        return False
    '''
    
    # slicker version
    return len(lst)!=len(set(lst))

    


'''
make this work:
>>> notInBoth( {2,3,4},{2,3,5,6})
{4,5,6}
'''

def notInBoth(s,t):

    '''
    u = s.union(t)
    for item in s.intersection(t):
        u.remove(item)
    return u
    '''    
    return s.union(t).difference(s.intersection(t))
    

        
        







