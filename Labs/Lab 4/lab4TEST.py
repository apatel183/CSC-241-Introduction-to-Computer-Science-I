# lab4TEST.py

>>> from lab4 import *


##### lineLengths #####

>>> lineLengths('test1.txt')
15+20+23+24+0=82
>>> lineLengths('test2.txt')
16+21+49+24+0=110
>>> 

##### monogram #####

>>> monogram('cher')
'C'
>>> monogram('George Washington')
'GW'
>>> monogram('george herbert walker bush')
'GHWB'
>>> monogram('george herbert walker bush')=='GHWB'
True
>>>


##### pay #####
>>> pay(10,35)
350
>>> pay(10,45)
475.0
>>> pay(10,61)
720.0
>>> pay(10,61)==720.0
True

##### average #####

>>> average("example1.txt")
4.352941176470588
>>> average("example2.txt")
4.523809523809524
>>> average("example2.txt")==4.523809523809524
True
>>> average("empty.txt")
0.0
