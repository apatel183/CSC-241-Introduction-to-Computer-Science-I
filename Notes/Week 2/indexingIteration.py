# indexingIteration.py

'''
hw question

make this work:
>>> square()
Enter a number: 16
16 is 4 squared.
>>> square()
Enter a number: 23
23 is not a perfect square.
'''

##### review #####
'''

review:
    input, print, eval
    if, if/else, if/elif/else
    bool - and, or, not
    
'''

##### str(ing) #####
'''
str:
    0-based
    indexed []
    sequence of characters
    immutable - can't be changed

functions:
    len

operators:
    in, not in

indexing:
    s[i] - character at index i
    s[start:stop] - slice, substring
       starting at start, stopping and
       not including stop
    omit start - start at beginning
    omit stop - go to end
    s[start:stop:step]
    omit step - defaults to 1

>>> s='apple'
>>> s[1]
'p'
>>> s[0]
'a'
>>> c=s[3]
>>> 10*c
'llllllllll'
>>> len(s)
5
>>> # last character
>>> s[4]
'e'
>>> s = 'this is a sentence!'
>>> # last character
>>> 
>>> 
>>> s[len(s)-1]
'!'
>>> # python shorthand
>>> s[-1]
'!'
>>> s[-2]
'e'
>>> # first char using negative
>>> s[-len(s)]
't'
>>> 'apple'[2]
'p'
>>> 'apple'[10]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'apple'[10]
IndexError: string index out of range
>>> 'apple
SyntaxError: EOL while scanning string literal
>>> 'apple'[-6]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'apple'[-6]
IndexError: string index out of range
>>> 
>>> 
>>> # slices
>>> # s[start:stop]
>>> s
'this is a sentence!'
>>> # grab the word 'this'
>>> s[0:4]
'this'
>>> # everything but 'this'
>>> s[4:len(s)]
' is a sentence!'
>>> s[4:100]
' is a sentence!'
>>> s[4:]  # omit stop, go to end
' is a sentence!'
>>> s[:4] # up to index 4
'this'
>>> s[0:10:2]
'ti sa'
>>> s[:]
'this is a sentence!'
>>> s[::-1]
'!ecnetnes a si siht'
>>> 
>>> # change 'apple' to 'Apple'
>>> c
'l'
>>> s='apple'
>>> # immutable - must build new string
>>> 'A'+s[1:]
'Apple'
>>> s='A'+s[1:]
>>> s
'Apple'
>>> 
>>> # in, not in are for substrings
>>> s
'Apple'
>>> 'p' in s
True
>>> 'ap' in s
False
>>> 'Ap' in s
True
>>> 'pl' not in s
False
>>>
'''

##### list #####

'''
list:
    0-based
    sequence
    of items (of any type, can be mixed, can include lists)
    [item, item, item, ..., item]
    [] - empty list
    mutable - can be changed/edited

operations:
    + concatenation
    list*int, int*list
    in, not in - look for ITEMS! not sublists

functions:
    len
    max, min, sum

methods:
    append - add item to end
    remove(item)
    pop() - removes last item, returns it

>>> 
>>> #### list ####
>>> 
>>> lst = [2,3,4,'apple',2<3]
>>> lst[3]
'apple'
>>> lst[3:]
['apple', True]
>>> fruit = ['apple','orange','kiwi','durian']
>>> fruit[3][1]
'u'
>>> fruit[-2][-3]
'i'
>>> 
>>> # lists are mutable
>>> # this wouldnt work with string
>>> fruit[0] = 'Apple'
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> 
>>> s
'Apple'
>>> fruit+'banana'
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    fruit+'banana'
TypeError: can only concatenate list (not "str") to list
>>> fruit+['banana']
['Apple', 'orange', 'kiwi', 'durian', 'banana']
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> 2*fruit
['Apple', 'orange', 'kiwi', 'durian', 'Apple', 'orange', 'kiwi', 'durian']
>>> len(fruit)
4
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> [ item.capitalize() for item in fruit]
['Apple', 'Orange', 'Kiwi', 'Durian']
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> 'apple' in fruit
False
>>> 'Apple' in fruit
True
>>> ['Apple','orange'] in fruit
False
>>> nested = [ [2,3,4], [4,5], [5,7,8]]
>>> nested[1]
[4, 5]
>>> nested[1][1]
5
>>> [4,5] in nested
True
>>> [[2,3,4], [4,5]] in nested
False
>>> 
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> fruit.append('banana')
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana']
>>> fruit.append('banana')
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana', 'banana']
>>> len(fruit)
6
>>> fruit.remove('banana')
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana']
>>> fruit.count('banana')
1
>>> x = len( fruit )
>>> x
5
>>> x = fruit.append('lemon')
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana', 'lemon']
>>> x
>>> type(x)
<class 'NoneType'>
>>> vars()
{'lst': [2, 3, 4, 'apple', True], 'fruit': ['Apple', 'orange', 'kiwi', 'durian', 'banana', 'lemon'], '__builtins__': <module 'builtins' (built-in)>, '__doc__': '\nhw question\n\nmake this work:\n>>> square()\nEnter a number: 16\n16 is 4 squared.\n>>> square()\nEnter a number: 23\n23 is not a perfect square.\n', 'nested': [[2, 3, 4], [4, 5], [5, 7, 8]], '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__name__': '__main__', '__spec__': None, '__package__': None, '__file__': 'C:\\Users\\cdminstructor\\Documents\\csc241Sedgwick\\indexingIteration.py', 'c': 'l', 's': 'Apple', 'x': None}
>>> 
>>> 
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana', 'lemon']
>>> fruit.pop()
'lemon'
>>> fruit
['Apple', 'orange', 'kiwi', 'durian', 'banana']
>>> tobuy = fruit.pop()
>>> fruit
['Apple', 'orange', 'kiwi', 'durian']
>>> tobuy
'banana'
>>> len(fruit)
4
>>> lst = []
>>> lst.append(3)
>>> lst.append(99)
>>> lst.append(77)
>>> lst
[3, 99, 77]
>>> max(lst)
99
>>> min(lst)
3
>>> max(fruit)
'orange'
>>> min(fruit)
'Apple'
>>> max([2,3,'apple'])
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    max([2,3,'apple'])
TypeError: unorderable types: str() > int()
>>> 
>>> 
>>> # important coding tip
>>> # is n one of 2, 3, 4
>>> n=7
>>> n==2 or 3 or 4
3
\
>>> n==2 or n==3 or n==4
False
>>> False or 3
3
>>> n in [2,3,4]
False
>>> s
'Apple'
>>> # s[1] a vowel
>>> s[1] in 'aeiouAEIOU'
False
>>>    
    
'''

##### range #####

'''
range:
    behaves like a list of numbers
    not quite, but can think of that way

3 forms:
    range(n) - 0,1,2,...,n-1
    range(start,stop) - start, start+1, ...., stop-1
    range(start,stop,step)

functions
    len

operators
    in, not in

indexing
    [] - index 
    [::] - slice

>>> range(10)
range(0, 10)
>>> 4 in range(10)
True
>>> 11 in range(10)
False
>>> 10 in range(10)
False

>>> list( range(10) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list( range(4,10) )
[4, 5, 6, 7, 8, 9]
>>> list( range(-4,3) )
[-4, -3, -2, -1, 0, 1, 2]
>>> list( range(-4,3,2) )
[-4, -2, 0, 2]
>>> list( range(4,-33,-7) )
[4, -3, -10, -17, -24, -31]
>>> len( range(-4,3,2) )
4
>>> range(-4,3,2)[0]
-4
>>> range(99999999)
range(0, 99999999)
>>> range(3,100,2)
range(3, 100, 2)
>>> range(3,100,2)[0]
3
>>> range(3,100,2)[2]
7
>>> range(3,100,2)[12]
27
>>> range(3,100,1000)
range(3, 100, 1000)
>>> len( range(3,100,1000) )
1
>>> len( range(3,-99,1000) )
0
>>> range(3,100,2)[0:2]
range(3, 7, 2)
>>> 

'''


##### iteration - for #####

'''
for variable in sequence:
    statement
    ...
    statement
statement

body - indented statements

variable "visits" each item in the sequence
this is a variable declaration/assignment
even if you dont see the variable=

variable is assigned to each item
in the sequence, one at a time, and
the indented block is executed for each



>>> 
>>> s = 'apple'
>>> for char in s:
	print( char )

	
a
p
p
l
e
>>> # shorthand for the following
>>> char = s[0]
>>> print( char )
a
>>> char = s[1]
>>> print( char )
p
>>> char = s[2]
>>> print( char )
p
>>> char = s[3]
>>> print( char )
l
>>> char = s[4]
>>> print( char )
e
>>> char
'e'
>>> 
>>> 
>>> for item in [2,3,'apple']:
	print(item)

	
2
3
apple
>>> for i in range(3,10,2):
	print(i)

	
3
5
7
9
>>> vars()
{'l': [10, 20, 30, 40], '__name__': '__main__', 'char': 'e', 'i': 9, 's': 'apple', 'item': 'apple', '__package__': None, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
>>> 
>>> 
>>> sentence = 'hello how are you?"
SyntaxError: EOL while scanning string literal
>>> sentence = 'hello how are you?'
>>> for word in sentence:
	print( word )

	
h
e
l
l
o
 
h
o
w
 
a
r
e
 
y
o
u
?
>>> # word is a TERRIBLE choice for a variable
>>> # if you iterate over a str, you get
>>> # characters, because a str is a sequencde
>>> # of characters
>>> 
>>> # print 'hello' ten times
>>> # count - iterate over range
>>> for i in range(10):
	print('hello',i)

	
hello 0
hello 1
hello 2
hello 3
hello 4
hello 5
hello 6
hello 7
hello 8
hello 9
>>> i
9
>>> for i in range(0):
	print('hello',i)

	
>>> 
>>> 
>>> s
'apple'
>>> sentence
'hello how are you?'
>>> # print vowels in sentence
>>> # one per line
>>> for c in sentence:
	print(c)

	
h
e
l
l
o
 
h
o
w
 
a
r
e
 
y
o
u
?
>>> for c in sentence:
	if :print(c)
	
SyntaxError: invalid syntax
>>> for c in sentence:
	if :print(c)
	
SyntaxError: invalid syntax
>>> for c in sentence:
	if :  print(c)
	
SyntaxError: invalid syntax
>>> for c in sentence:
	if c in 'aeiouAEIOU':
		print( c )

		
e
o
o
a
e
o
u
>>> # print negative numbers in lst
>>> lst = [2,3,-5,-99,8,77,-22]
>>> for num is lst:
	
SyntaxError: invalid syntax
>>> for num in lst:
	if num<0:
		print(num)

		
-5
-99
-22
>>> # print whether each is odd/even
>>> for num in lst:
	if num%2!=0:  # != not equals
		print(num,'is odd')
	else:
		print(num,'is even')

		
2 is even
3 is odd
-5 is odd
-99 is odd
8 is even
77 is odd
-22 is even
>>> for num in lst:
	if num%2:  # != not equals
		print(num,'is odd')
	else:
		print(num,'is even')

		
2 is even
3 is odd
-5 is odd
-99 is odd
8 is even
77 is odd
-22 is even
>>> True+True
2
>>> 
'''





