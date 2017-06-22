# review.py

# csc 281 in winter?

##### final exam #####

'''
Usual classroom
NOT the usual time
Thurs Nov 19
8:30-10:45
'''

##### pd tourney #####

##### review #####

'''
for any class/type:
    operators
    mutable/immutable
    functions: len(lst)
    methods: lst.append(4.5)

numbers:
    bool < int < float
    ops: +,-,   *,/,//,%,   **  (what is precedence?)
         +=, -=, *=, ...
    bool ops: >,<,<=,>=,==,!=
    funs: sum, abs, max, min

str:
    indexed sequence of characters
    s[i] - indexing
    s[start:stop:step] - slicing
    immutable: s=s.upper()
    ops: +, int*str
         <,>,<=,>=,....   - dictionary comparisons
    in, not in - work on substrs
    functions: len
    methods:  split, upper, lower, find, count, replace

list:
    indexed sequence of items (anything)
    mutable:   lst.sort()
    lst[i] - an item
    lst[start:stop:step] - a sub-list
    ops: +, int*list, list*int
    in, not in - looks for item (not sublist)
    functions: len, sum, max, min
    methods: append, index, count, pop
             sort, reverse, remove

range:
    sequence of ints (arithmetic)
    immutable
    range(n)
    range(start,stop)
    range(start,stop,step)
    used for indexed iteration    

dict:
    container for key:value pairs
    {key:val, key:val, ...}, {}
    mutable, keys are unique and immutable
    not ordered
    d[key]=val
    d[key] retrieves a value
    in, not in - work on keys
    funs:  len
    methods: pop(key)

tuple
    (item,item,,,)
    like a list, but immutable
    can be dict keys
    x,y = 2,3

set:
    {item,item,item,....}
    like a list, BUT items must be unique and immutable
    not ordered
    empty set - s=set() NOT s={}
    mutable
    in, not in
    functions: len
    methods: add, remove

file:
    open(filename) - opens for reading
    open(filename,'w') - for writing
    read() - get back file as a str
    readlines() - get back list of strs
    write( string)
    close()

math
    import math
    math.pi, math.sin()
    other function, constants

random
    import random
    randrange(start,stop)
    choice( iterable )
    seed, sample, shuffle

control structures:
    if
    if,(elif),else - execute EXACTLY one block
    for
    while
    loop mods:  return, break, (pass, continue)

try/except:

    try:
        code may cause error
    except:
        run this if error occurs

print vs. return

loop patterns:

"standard iteration" uses iterators:

    for char in string:
    for item in list:
    for i in range(n)
    for key in dict:
    for item in set:

>>> for word in "hello how are you":
	print( word )

	
h
...
o
u
>>>  

word is a TERRIBLE variable name in this case

>>> for word in "hello how are you".split():
	print( word )

	
hello
how
are
you
>>>

counter/index/range iteration:
use when you need index, location information

>>> for i in range(len(s)):
	print( i,s[i])

	
0 a
1 p
2 p
3 l
4 e
>>> 

nested loops

accmulator:
    0) set up iteration (visit/print items)
    1) init accum before loop
    2) accumulate in the loop
    3) return accum after loop

search pattern:
def
    for
        if
            return
    return

this is NEVER correct:

def 
    for
        if
            return
        else
            return

while loop:
    not clear what you are iterating over in advance
    keep track of state (variables)


loop want body to execute at least once
    1) loop and a half pattern
       part of the body is repeated outside loop
    2) infinite loop pattern, while True
       if ... break inside loop

def
    return vs. print
    arguments/paramters

x is paramter, 3 is the argument
>>> def f(x):
	return x*2
>>> f(3)
6

'''


'''
make this work:
>>> matches( [3,3,5,6], [5,3])
[ (0,1),(1,1),(2,0)]
'''

def matches( lsta, lstb ):

    locs = []
    for i in range(len(lsta)):
        for j in range(len(lstb)):
            if lsta[i]==lstb[j]:
                #print( i,lsta[i],j,lstb[j])
                locs.append( (i,j) )
    return locs
    
    
    































