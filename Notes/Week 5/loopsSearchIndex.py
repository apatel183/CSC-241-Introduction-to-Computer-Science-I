# loopsSearchIndex.py

'''
reminder:

    Tues - lab
    Thurs - midterm 9:15-11:40
'''


##### review #####

'''
if, elif,else:
    multiway switch, exactly ONE of
    a bunch of blocks executes

accumulation: compute a value
using a running value (e.g. running total)

4 steps
0) print version, visit all items of interest
1) initialize accumulator before loop
2) accumulate in loop
3) return accumulator after loop

'''

'''
make this work:
>>> countEvens( [2,3,4,5,6,7] )
3
'''


def countEvens( numberlst):

    count=0
    for num in numberlst:
        if num%2==0:
            count+=1  # count++
            #print( num )
    return count

    
'''
make this work:
>>> signs( [ 2, -8, 99, 0, 22, -33])
['+','-','+','0','+','-']
'''

# v1 - as one function
def signs( lst ):

    ans = []
    for item in lst:
        if item>0:
            ans.append('+' )
            # ans+= ['+']
        elif item==0:
            ans.append('0')
        else:
            ans.append('-')
    return ans


def sign( num ):
    if num>0:
        return '+'
    elif num==0:
        return '0'
    else:
        return '-'


def signs(lst):

    ans = []
    for num in lst:
        ans.append( sign(num) )
    return ans

'''
make this work
>>> biggest( [-3,-99,-22,11] )
11
>>> biggest( [-3,-99,-22] )
-3
'''

def biggest( lst ):

    runningMax = lst[0]
    for item in lst:
        #print( item )
        if item > runningMax:
            runningMax = item
    return runningMax


'''
>>> biggest( [-3,-99,-22] )
-3
>>> biggest( ['a','b','c'])
'c'
>>> biggest( 'apple' )
'p'
>>> 
'''

##### search ####

'''
make this work:
>>> isIn( 3,[8,9,7,2] )
False
>>> isIn( 7,[8,9,7,2] )
True
'''

# v1 - as an accumulator - wasteful

def isIn( target, lst ):

    foundYet = False
    for item in lst:
        if item==target:
            foundYet = True
    return foundYet
        

# v2 - as a search, much better

def isIn( target, lst ):

    for item in lst:
        if item==target:
            return True
    return False

##### try/except #####

'''
Grace Hopper: "It's easier to ask forgiveness
than it is to get permission."

try:
    code that may cause
    an error
except:
    this code executes
    if an error occurs

ADVICE: be specific about the type of error
you are expecting

>>> 2+'apple'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    2+'apple'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> y
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> open('doesnotexist')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    open('doesnotexist')
FileNotFoundError: [Errno 2] No such file or directory: 'doesnotexist'
>>> raise Exception('this is an error')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    raise Exception('this is an error')
Exception: this is an error
>>> 
>>> 
>>> 
>>> try:
	open('doesnotexist.txt')
except:
	print('could not find the file')

	
could not find the file
>>> a = 5
>>> b = 0
>>> try:
	print(a/b)
except:
	print('div by zero')

	
div by zero
>>> try:
	print(a/b)
except ZeroDivisionError:
	print('div by zero')

	
div by zero
>>> try:
	print(a/b)
except FileNotFoundError:
	print('div by zero')

	
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    print(a/b)
ZeroDivisionError: division by zero
>>> 
'''

'''
make this work:
>>> numLines( 'input.txt' )
23
>>> numLines('doesnotexist.txt')
-1
'''

def numLines( filename):

    try:
        return len( open(filename).readlines() )
    except:  # except FileNotFoundError: better probably
        return -1
        
'''
>>> numLines( 'in.txt')
4
>>> numLines( 'inn.txt')
-1
>>> 
'''
    










