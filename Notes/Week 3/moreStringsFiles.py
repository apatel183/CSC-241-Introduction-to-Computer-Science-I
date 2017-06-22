# moreStringsFiles.py

##### str #####

'''
str(ings) are IMMUTABLE, they cannot
be changed, you can however, produce
new strings based on old ones

slices
    s[start:stop]
    s[start:stop:step]

function
    len

methods:
    upper, lower, capitalize
    strip
    split - splits on space (by default)
    find(target) - returns index of target, -1 if not found
    count(target)
    

>>> 
>>> s = 'apple'
>>> s.upper()
'APPLE'
>>> s
'apple'
>>> 'Fred'.lower()
'fred'
>>> 'Fred'.lower().upper()
'FRED'
>>> s.upper()
'APPLE'
>>> s
'apple'
>>> s = s.upper()
>>> s
'APPLE'
>>> s
'APPLE'
>>> 'hello'.capitalize()
'Hello'
>>> 
>>> ans = input('Continue?')
Continue?y
>>> if ans=='y' or ans ='Y' or ans='yes' or ans='YES':
	
SyntaxError: invalid syntax
>>> if ans=='y' or ans =='Y' or ans=='yes' or ans=='YES':
	print('ok, continue then')

	
ok, continue then
>>> if ans[0].upper()=='Y':
	print('ok, continue then')

	
ok, continue then
>>> ans = input('Continue?')
Continue?yowza
>>> if ans[0].upper()=='Y':
	print('ok, continue then')

	
ok, continue then
>>> 
>>> 
>>> '   string    with   blanks    '.strip()
'string    with   blanks'
>>> 
>>> 
>>> s = 'Hello,  how are you?'
>>> for word in s:
	print( word )

	
H
e
l
l
o
,
 
 
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
>>> s
'Hello,  how are you?'
>>> s.split()
['Hello,', 'how', 'are', 'you?']
>>> for word in s.split():
	print( word )

	
Hello,
how
are
you?
>>> 
>>> s
'Hello,  how are you?'
>>> s.find('how')
8
>>> s.find('How')
-1
>>> s.index('how')
8
>>> s.index('How')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.index('How')
ValueError: substring not found
>>> s
'Hello,  how are you?'
>>> s.count(' ')
4
>>> s.replace('how','HOW')
'Hello,  HOW are you?'
>>> s.replace(' ','-')
'Hello,--how-are-you?'
>>> 
>>> letter='''
'''
Dear {},
Would you like to buy {} for {}?
thanks,
{}'''
'''
>>> letter.format('so and so','ducks','$100','fred')
'\nDear so and so,\nWould you like to buy ducks for $100?\nthanks,\nfred'
>>> print(letter.format('so and so','ducks','$100','fred'))

Dear so and so,
Would you like to buy ducks for $100?
thanks,
fred
>>> s
'Hello,  how are you?'
>>> for word in s.split():
	print( word )

	
Hello,
how
are
you?
>>> for word in s.split().upper():
	print( word )

	
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    for word in s.split().upper():
AttributeError: 'list' object has no attribute 'upper'
>>> for word in s.upper().split():
	print( word )

	
HELLO,
HOW
ARE
YOU?
>>> for word in s.replace(',','').replace('?','').upper().split():
	print( word )

	
HELLO
HOW
ARE
YOU
>>> 
    
'''

# fancier palindrome

'''
make this work:
>>> palindrome('otto')
True
>>> palindrome('Otto')
True
>>> palindrome('RaceCar')
True
>>> palindrome('Able was I, ere I saw Elba.')
True
>>> palindrome('A dog! A panic in a pagoda!')
True
'''

# v1 - good, but a bit cumbersome
def palindrome( s ):

    # get rid of spaces, assign to same variable
    s = s.replace(' ','')
    # get rid  of punctuation
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace('!','')
    s = s.replace('?','')
    # convert to upper case
    s = s.upper()
    # check whether equal to reverse
    #print( s )
    if s==s[::-1]:  # equal to reverse
        return True
    else:
        return False
    #return s==s[::-1]
    

# v2 - slicker, uses ACCUMULATION
def palindrome( s ):

    # get rid of spaces, assign to same variable
    # get rid  of punctuation
    for c in ' .,!?;:\"\'':
        s=s.replace(c,'')
    # convert to upper case
    s = s.upper()
    # check whether equal to reverse
    print( s )
    if s==s[::-1]:  # equal to reverse
        return True
    else:
        return False
    #return s==s[::-1]


##### more on print #####

'''
print - by default
    prints spaces between items
    end of line after all items
    these can be changed

print( ...items..., end=s, sep=t) # s and t strings

s will be instead of end of line
t instead of spaces

>>> print(2,3,'apple')
2 3 apple
>>> print(2,3,'apple',sep='----')
2----3----apple
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> for i in range(4):
	print(i,end='')

	
0123
>>> 
'''


##### file #####

'''
we will open and manipulate (read/write)
text files

text file should be in your working directory/folder

be careful to distinguish between
    - name of the file, a string
    - file itself, file object
    - contents of the file, which is a string

general procedure:
0) open the file
1) read/write the file
2) close the file

open(filename,mode)
    returns a file object
    mode is one of 'r'ead, 'w'rite, 'a'ppend
    defaults to read

can read in (at least) 2 ways:
    read() - returns contens as a str
    readlines() - returns contents as a list of strs
close()


>>> open('in.txt')
<_io.TextIOWrapper name='in.txt' mode='r' encoding='cp1252'>
>>> infile = open('in.txt')
>>> infile.read()
'This is a text file\nwith\n4\nlines in it.\n'
>>> contents = infile.read()
>>> contents
''
>>> infile = open('in.txt')
>>> contents = infile.read()
>>> contents
'This is a text file\nwith\n4\nlines in it.\n'
>>> infile.close()
>>> 
>>> infile = open('in.txt')
>>> lines = infile.readlines()
>>> infile.close()
>>> lines
['This is a text file\n', 'with\n', '4\n', 'lines in it.\n']
>>> 
>>> outfile = open('out.txt','w')
>>> outfile.write('here is some stuff
	      
SyntaxError: EOL while scanning string literal
>>> outfile.write('here is some stuff')
18
>>> outfile.write('here is some more stuff')
23
>>> outfile.write('that is it')
10
>>> outfile.close()
>>> open('out.txt').read()
'here is some stuffhere is some more stuffthat is it'
>>> 

'''
'''
make this work:
>>> numChars('out.txt')
50 ?
'''

# v1 - proper version, closes file
def numChars(filename):

    # open
    infile = open(filename)
    # read
    contents = infile.read()
    # close
    infile.close()
    # give answer back
    n = len(contents)
    return n
  
# v2 - slicker, but doesnt close file
def numChars(filename):
    return len( open(filename).read() )
    1/0  # never get here, return terminates
    

def numLines(filename):
    return len( open(filename).readlines() )
 

'''
make this work:
>>> getCell('numbers.csv',3,2)
66
'''

def getCell( filename, col, row):  # 1-based counting

    return eval( open(filename).readlines()[row-1].split(',')[col-1] )











