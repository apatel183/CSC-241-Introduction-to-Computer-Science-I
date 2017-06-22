# functions.py

##### def - more on functions #####

'''
generally, three types of functions/methods
    1) functions that DO something:
       print, list.append, often verbs
    2) functions with answer (returns value)
       max, abs, len, eval  often nouns
    3) functions that does both
       input, list.pop


1) function definition - does NOT execute function

def functionName(par0,par1,...,parn):  # 0 or more paramters
    statement
    statement
    ...
    statement
    # may or may not have one or more of these
    return
    return something

2) function call/invocation - actually EXECUTES function

>>> functionName(arg0,arg1,...,argn)
like saying: par0=arg0, par1=arg1, ....
and then execute statements

3) return - means "the answer is"
   return something - stops function, gives something
      back as answer
   return - stops function, does not give answer
'''

'''
make this work:
>>> max(2,3)
3
>>> max(2,3)*10
30
'''

#v1 - print version doesnt work
# calculation cant be used in
# subsequent expressions
def max(a,b):
    if a>b:
        print( a )
    else:
        print( b )

'''
>>> max(2,3)
3
>>> max(2,3)*10
3
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    max(2,3)*10
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> 
'''

#v2 - return version
# answer can be used in subsequent calculations
def max(a,b):
    if a>b:
        return a  # the answer is: a
    else:
        return b  # the answer is: b

'''
>>> max(2,3)
3
>>> max(2,3)*10
30
>>> 
'''

'''
make this work:
>>> odds( [2,4,12,99,22,333])
99
333
'''

def odds(lstNums):
    for num in lstNums:
        # if odd
        # print(num)
        if num%2==1:
            # return num   # not good, will terminate after 1
            print( num )


'''
>>> odds( [2,4,12,99,22,333])
99
333
>>> 
>>> 
>>> odds ( range(20) )
1
3
5
7
9
11
13
15
17
19
>>>
'''

'''
make this work:
>>> palindrome('otto')
True
>>> palindrome('Otto')
False
'''

#v1 - absolutely correct
def palindrome( s ):
    if s==s[::-1]:
        return True
    else:
        return False
    
'''
>>> palindrome('otto')
True
>>> palindrome('ottO')
False
>>> if palindrome('otto'):
	print( 'yes' )

	
yes
>>> 
'''
#v2 - slicker
# functions of form v1 can always be rewritten
def palindrome( s ):
    return s==s[::-1]






