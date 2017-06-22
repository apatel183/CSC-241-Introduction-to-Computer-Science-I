# interactionsDecisions.py

##### comments #####

x=2+3  # end of line comment is ignored



'''
multiline comment is ignored

>>> x
5
'''

##### def - functions #####
'''
def is a container for python
code that can be asked for later
'''

def f():
    print( 99 )   # indented, in f
print(66) # not part of f() because not indented

'''
>>> f() # function call, invocation, run it!
99
>>> 
'''



##### user interaction #####

'''
i/o - input/output - all input/output
is done via strings

functions

print
    print none or more items
    with spaces inbetween items (can change)
    and one newline for each print

input
    prints message, receives response
    almost always, assign to a variable
    always returns  a str!!!!
    may need to convert to other type

eval
    converts str to number (float, int, bool) if it can
    big hammer
    alternatively use float(), int()
    
'''

def printStuff():

    x = 45.7
    print( 99 )
    print
    print()
    print( 2,3,4,'apple',4*x)

'''
>>> printStuff()
99

2 3 4 apple 182.8
>>> 
'''

# v1 - not quite right, i/o is strings
def getUserNum():

    num = input('please enter a number: ')
    print(num)
    print('twice the num is',2*num)

'''
>>> getUserNum()
please enter a number: 23
23
twice the num is 2323
>>>

converting strings to numbers:

>>> int('23')
23
>>> float('23')
23.0
>>> eval('23')
23
>>> int('23.5')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    int('23.5')
ValueError: invalid literal for int() with base 10: '23.5'
>>> 
'''


# v2 - turns input into a number
def getUserNum():

    num = eval( input('please enter a number: ') )
    print(num)
    print('twice the num is',2*num)
'''
>>> getUserNum()
please enter a number: 23
23
twice the num is 46
>>> getUserNum()
please enter a number: 23.9
23.9
twice the num is 47.8
>>> getUserNum()
please enter a number: 0
0
twice the num is 0
>>>
'''


5.5**.5   # computed but not displayed
print( 5.5**.5 ) # computed and displayed

##### if statements #####

'''
if condition:
    statement
    ...
    statement
statement

one-way if statement - an option
    condition is a bool, either True or False
    if True, execute indented statements
    otherwise (False), don't execute them
    regardless, continue execution with non-indented


if condition:
    statement
    statement
else:
    statement
    statement
statement

two-way if/else is a choice between two things
    if condition True exec if block
    if False exec else block
    EXACTLY ONE of the two blocks executes

if condition:
    statements
elif condition:
    statements
elif condition:
    statements
...
else:
    statements

multiway if/elif/else:
    EXACTLY one of n blocks executes
    the first whose condition is met
    or else block if no condition is met

'''

# v1 - if only
def temp():
    f = eval( input('Please enter a temperature: ') )
    if f < 32:
        print("It's cold")
        print("put a jacket on!")
    print("Bye, see you later")


# v2 - two possibilites - this is BAD!
# poorly written
def temp():
    f = eval( input('Please enter a temperature: ') )
    if f <= 32:
        print("It's cold")
        print("put a jacket on!")
    if f > 32:
        print("It's warm!")
    print("Bye, see you later")


# v3 - same result, GOOD!
# well written
def temp():
    f = eval( input('Please enter a temperature: ') )
    if f < 32:
        print("It's cold")
        print("put a jacket on!")
    else:
        print("It's warm!")
    print("Bye, see you later")


# v4 - same result, GOOD!
# well written
def temp():
    f = eval( input('Please enter a temperature: ') )
    if f < 32:
        print("It's cold")
        print("put a jacket on!")
    elif f<80:
        print("It's warm!")
    else:
        print('Hot!!!!')
    print("Bye, see you later")

















