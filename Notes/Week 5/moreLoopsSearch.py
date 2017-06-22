# moreLoopsSearch.py

# hw 

##### review  #####

'''
if,elif,else - multiway switch, choose
exactly one from a bunch of options

accumulation pattern - compute value
using a running value (e.g., running total)

4 step strategy:
0) print version, visit all items of interest
1) initialize accumulator before loop
2) accumulate in the loop
3) return accumulator after the loop

'''

##### example #####

'''
make this work:
>>> signs( [2,-8,99,0,22,-33,-33,55])
['+','-','+','0','+',...]
>>> signs( [] )
[]

print version first:
>>> signs( [2,-8,99,0,22,-33,-33,55])
+
-
+
0
...
'''

# accumulate signs of numbers
def signs( numlist ):

    ans=[]   #init
    # iterate through the numbers
    for num in numlist:

        # determine the sign
        # and accumulate answsers
        if num>0:
            ans.append( '+' )
        elif num==0:
            ans.append( '0' )
        else:
            ans.append( '-' )
    return ans
    
'''
make this work:
>>> biggest( [2,3,-12,99,33])
99
'''

# accumulate, keep track of
# biggest thing that you have seen so far

def biggest( lst ):

    runningMax = lst[0]
    for item in lst:
        if item > runningMax:
            runningMax = item
    return runningMax
    
'''
>>> biggest( [-3,-99,-22])
-3
>>> 
>>> 
>>> biggest(['apple','Pear','orange'])
'orange'
>>> biggest('I am going to buy apples at the store')
'y'
>>> biggest('I am going to buy apples at the store'.split())
'to'
>>> biggest([])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    biggest([])
  File "C:/Users/cdminstructor/Documents/csc241Sedgwick/moreLoopsSearch.py", line 68, in biggest
    runningMax = lst[0]
IndexError: list index out of range
\
>>> biggest( [-3,-99,-22,'apple'])
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    biggest( [-3,-99,-22,'apple'])
  File "C:/Users/cdminstructor/Documents/csc241Sedgwick/moreLoopsSearch.py", line 70, in biggest
    if item > runningMax:
TypeError: unorderable types: str() > int()
>>> 
'''

##### search pattern #####

'''
make this work:
>>> isin(3,[8,9,7,2])
False
>>> isin(3,[8,9,3,7,2])
True
'''

# v1 - written as accumulator
def isin( target, lst ):
    ''' return True if target in lst,
False otherwise '''

    foundYet = False
    for item in lst:
        if item==target:
            #print(item)
            foundYet = True
    return foundYet


# v1 - as a search
def isin( target, lst ):
    ''' return True if target in lst,
False otherwise '''

    for item in lst:
        if item==target:
            #print(item)
            return True
    return False
    
##### try/except #####

'''
Grace Hopper: It's easier to ask forgiveness
than it is to get permission.

try:
    code that may cause
    error
except:
    this code is run if
    an error occurs


ADVICE: be specific about the type of error


>>> 1/0
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> open('blah')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    open('blah')
FileNotFoundError: [Errno 2] No such file or directory: 'blah'
>>> 
>>> 
>>> try:
	open('doesnotexist.txt')
except:
	print('sorry, that file does not exist')

	
sorry, that file does not exist
>>> 
>>> 
>>> a = 5
>>> b = 0
>>> try:
	print(a/b)
except:
	print('division by zero')

	
division by zero
>>> 
>>> try:
	print(a/b)
except ZeroDivisionError:
	print('division by zero')

	
division by zero
>>> try:
	open('blah')
except ZeroDivisionError:
	print('division by zero')

	
Traceback (most recent call last):
  File "<pyshell#85>", line 2, in <module>
    open('blah')
FileNotFoundError: [Errno 2] No such file or directory: 'blah'
>>> 


'''






























 
