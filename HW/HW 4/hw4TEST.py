# hw4TEST.py

>>> from hw4 import *

##### partition #####

>>> partition( ['apple','pear','','Orange','Kiwi','','banana'],'g' )
pear
Orange
Kiwi
>>> partition( ['apple','pear','','Orange','Kiwi','','banana'],'G' )
pear
Orange
Kiwi
>>> partition( ['apple','pear','','Orange','Kiwi','','banana'],'w' )
>>> partition( ['apple','pear','','Orange','Kiwi','','banana'],'b' )
pear
Orange
Kiwi
banana
>>> 

##### points #####

>>> points(0,0,1,1)
The slope is 1.0 and the distance is 1.4142135623730951
>>> points(0,0,0,1)
The slope is infinity and the distance is 1.0
>>> points(3,4,5,6)
The slope is 1.0 and the distance is 2.8284271247461903
>>> points(-12.3,55,99.4,-3.6)
The slope is -0.5246195165622203 and the distance is 126.13821784058946
>>> 

##### numVowels #####

>>> numVowels('vowels.txt')
21
>>> numVowels('poppins.txt')
418
>>> numVowels('empty.txt')
0
>>> 

##### numLen #####

>>> numLen('This is a test',4)
2
>>> numLen('This is a test',2)
1
>>> numLen('This is a test',3)
0
>>> numLen('The quick red fox jumped over the lazy brown dog',2)
0
>>> numLen('The quick red fox jumped over the lazy brown dog',5)
2
>>> [numLen('The quick red fox jumped over the lazy brown dog',i) for i in range(10)]
[0, 0, 0, 5, 2, 2, 1, 0, 0, 0]
>>> 
