# counterLoops.py

# search pattern

'''
def search():

    for
       if
           return
    return

'''

##### counter/index/range loops #####

'''
1+2+3+...+1000=?
>>> add(3) # 1 + 2 + 3
6
>>> add(5)
15
>>> add(1000)
??
'''

def add(n):

    total = 0
    for i in range(1,n+1):
        total += i
    return total


'''
make this work:
>>> vowelIndices('hello how are you?')
[1,4,...]
'''



def vowelIndices( s ):

    indices = []
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            indices.append(i)
            #indices += [i]
            #print(i,s[i])
    return indices


'''
make this work:
>>> find( 7, [6,7,2,3,4,7,99])
1
>>> find( 8, [6,7,2,3,4,99])
-1
'''

def find( target,lst ):

    for i in range(len(lst)):
        if lst[i]==target:
            return i
    return -1
    

'''
make this work:
>>> findall( 7, [6,7,2,3,4,7,99])
[1,5]
>>> findall( 8, [6,7,2,3,4,7,99])
[]
'''

def findall( target,lst ):

    indices = []
    for i in range(len(lst)):
        if lst[i]==target:
            indices.append(i)
    return indices


##### review #####

'''
2 ways of iterating:

1) standard (using an iterator)
2) counter/index/range - iterate over indices

which to use: use 1) if you can, but if you need
location or indices, you have to go with 2)

>>> s = 'apple'
>>> #1)
>>> for c in s:
	print( c, end=' ')

	
a p p l e 
>>> #2)
>>> for i in range(len(s)):
	print( i,s[i] )

	
0 a
1 p
2 p
3 l
4 e
>>> 

'''

'''
make this work:
>>> count( 4, [6,3,4,4,8,9,10])
2

use 1) dont need to know where things are found
only that they are found

'''

# or we do sneaky implementation
def count( target, lst ):
    return len( findall( target, lst ) )


'''
make this work
>>> isSorted( [3,4,5,5,9,10,99] )
True
>>> isSorted( [3,4,5,5,3,9,10,99] )
False
'''

# search for a bad (decreasing pair)

def isSorted( lst ):

    # iterate over successive pairs
    # for num in lst: #no, need location
    for i in range(len(lst)-1):
        # if any pair decreases, return False
        if lst[i+1]<lst[i]:  # step down
            return False
            #print( i, lst[i], lst[i+1] )
    # no decreasing pair, return True
    return True

'''
>>> isSorted( [3,4,5,5,3,9,10,99] )
False
>>> isSorted( [3,4,5,5,9,10,99] )
True
>>> isSorted( [3,4,5,5,9,10,99,1] )
False
>>> 
'''

##### 2d/nested iteration #####
'''
make this work:
>>> vowelCount( ['apple','pear','kiwi'])
6
'''


def vowelCount( lstOfStrings ):

    count = 0
    for string in lstOfStrings:
        for char in string:
            if char in 'aeiouAEIOU':
                #print( char )
                count+=1
    return count


table =[
[2,3,-4],
[3,2,-1],
[-1,-1]
]

'''
make this work:
count the number of rows with positive numbers
>>> rowsWPos( table )
2
'''

def rowsWPos( table ):

    count=0
    for row in table:
        for num in row:
            if num>0:
                #print( num,end=' ' )
                count+=1
                break # out of the loop, not the function
        #print()
    return count
    

##### loop modifiers #####
'''
can affect execution of loops with:

1) return - kills function, hence all loops within
2) break - terminates innermost loop, not others
3) continue - terminates current iteration,
              continues with next
    
'''

'''
make this work:
>>> printTri(4)
1
12
123
1234
>>> printTri(3)
1
12
123
'''

def printTri( n ):

    # outer loop 1...n
    for i in range(1,n+1):
        # print 12...i
        for j in range(1,i+1):
            print(j,end='')
        print()




tmap='''
___________________________
______X______________X_______
___________________________
___________________________
___________________________
___________________________
~~~~~~~~~~~~~~~~~__________
~~~~X~~~~~~~~~~~~~____X______
~~~~~~~~~~~~~~~~~__________
~~~~~~~~~~~~~~~~~_____X_____
~~~~~~~~~~~~~~~~~__________
~~~~~~~~~~~~~~~~~__________
~~~~~~~~~~~~~~~~~__________'''

'''
make this work:
>>> findTreasure(tmap)
[ (2,6), (2,17), ...]
'''

# 2d indexed accumulator

def findTreasure(tmap):

    lines = tmap.split()
    #print( lines )

    treasure = []
    # 2d indexed iteration
    # not good enough: for line in lines:
    for i in range(len(lines)):
        #print(i,lines[i])
        for j in range(len(lines[i])):
            if lines[i][j]=='X':
                #print( i,j, lines[i][j])
                # accumulate locations
                treasure.append( (i,j) )
    return treasure
'''
>>> findTreasure(tmap)
[(1, 6), (1, 21), (7, 4), (7, 22), (9, 22)]
>>>
'''
        


    




















