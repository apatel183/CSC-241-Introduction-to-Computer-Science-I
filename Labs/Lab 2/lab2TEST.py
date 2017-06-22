Jane
Jones
george
orwell
k
i
y
apple
pear
book
owl



>>> from lab2 import *
>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('lab2TEST.py')



##### initials #####

>>> initials()
Please enter your first name: Please enter your last name: Jane Jones your initials are JJ
>>> initials()
Please enter your first name: Please enter your last name: george orwell your initials are go

##### corv ######

>>> corv()
Please enter a lower case letter: k is a consonant
>>> corv()
Please enter a lower case letter: i is a vowel
>>> corv()
Please enter a lower case letter: y is a consonant


##### pigLatin ######

>>> pigLatin()
English to Pig Latin Translator
Please enter a lower case English word: apple translates to appleay
>>> pigLatin()
English to Pig Latin Translator
Please enter a lower case English word: pear translates to earpay
>>> pigLatin()
English to Pig Latin Translator
Please enter a lower case English word: book translates to ookbay
>>> pigLatin()
English to Pig Latin Translator
Please enter a lower case English word: owl translates to owlay

>>> sys.stdin = si  # return stdin

