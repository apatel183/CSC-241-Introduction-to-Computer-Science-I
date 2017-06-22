# lab8TEST.py

>>> from lab8 import *

##### findMinRow #####

>>> findMinRow([])
-1
>>> findMinRow( [ [1,2,5],[2,2],[1,3],[7] ] )
1
>>> findMinRow( [ [1,2,5],[2,2],[1,3],[7],[99,99,-200] ] )
4
>>> 


##### anagrams #####

>>> anagram('otto','toto')
True
>>> anagram('to','otto')
False
>>> anagram('dormitory','dirtyroom')
True
>>>


##### mirror #####

>>> mirror('vow')
'wov'
>>> mirror('wood')
'boow'
>>> mirror('bed')
'INVALID'
>>> mirror('pout')
'tuoq'
>>> mirror( mirror('pout') )
'pout'
>>> [(c,mirror(c)) for c in 'abcdefghijklmnopqrstuvwxyz']
[('a', 'INVALID'), ('b', 'd'), ('c', 'INVALID'), ('d', 'b'), ('e', 'INVALID'), ('f', 'INVALID'), ('g', 'INVALID'), ('h', 'INVALID'), ('i', 'i'), ('j', 'INVALID'), ('k', 'INVALID'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'q'), ('q', 'p'), ('r', 'INVALID'), ('s', 'INVALID'), ('t', 't'), ('u', 'u'), ('v', 'v'), ('w', 'w'), ('x', 'x'), ('y', 'INVALID'), ('z', 'INVALID')]
>>> 

##### numPicks #####

>>> random.seed(15)   
>>> numPicks()  # simulation: 3 0 8 0
4
>>> random.seed(11)
>>> numPicks()  # simulation: 7 8 7
3
>>> random.seed(0)
>>> numPicks()  # simulation: 6 6
2
>>> [ (random.seed(i),numPicks()) for i in range(10)]
[(None, 2), (None, 5), (None, 3), (None, 6), (None, 7), (None, 8), (None, 6), (None, 7), (None, 5), (None, 6)]
>>> 
