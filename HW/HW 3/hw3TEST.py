# hw3TEST.py

>>> from hw3 import *



##### printMultiples ######

>>> printMultiples(10,2)
10 20 
>>> printMultiples(10,10)
10 20 30 40 50 60 70 80 90 100 
>>> printMultiples(2,12)
2 4 6 8 10 12 14 16 18 20 22 24 
>>> printMultiples(3,5)
3 6 9 12 15 
>>> printMultiples(7,5)
7 14 21 28 35 
>>> 

##### customSpam ######

>>> customSpam('Ambrose Bierce','one thousand','iamgreat@xyz.com')
Dear Ambrose Bierce,
We would like to let you know about a great opportunity.
You can make O N E   T H O U S A N D dollars in just a few short weeks!
This is a limited-time offer.
Please contact us at iamgreat@xyz.com for more information.
>>> customSpam('haruki murakami','two million','callnow@gmail.com')
Dear Haruki Murakami,
We would like to let you know about a great opportunity.
You can make T W O   M I L L I O N dollars in just a few short weeks!
This is a limited-time offer.
Please contact us at callnow@gmail.com for more information.
>>> customSpam('ORANGE juice','four hundred','notimeleft@aol.com')
Dear Orange Juice,
We would like to let you know about a great opportunity.
You can make F O U R   H U N D R E D dollars in just a few short weeks!
This is a limited-time offer.
Please contact us at notimeleft@aol.com for more information.
>>> 

##### ion2e ######


>>> ion2e('congratulation')
'congratulate'
>>> ion2e('marathon')
'marathon'
>>> ion2e('accordionist')
'accordionist'
>>> ion2e('ionization')
'ionizate'
>>> ion2e('congratulation')=='congratulate'  # returns?
True
>>> x = ion2e('congratulate') # return
>>> x
'congratulate'


##### startsWith ######

>>> startsWith('a',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
apricot
>>> startsWith('A',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
apricot
>>> startsWith('App',['apple','ApPle','orange','Apple','kiwi','apricot'])
apple
ApPle
Apple
>>> startsWith('orang',['apple','ApPle','orange','Apple','kiwi','apricot'])
orange
>>> startsWith('ORANG',['apple','ApPle','orange','Apple','kiwi','apricot'])
orange
>>> startsWith('an',['apple','ApPle','orange','Apple','kiwi','apricot'])
>>> startsWith('ppl',['apple','ApPle','orange','Apple','kiwi','apricot'])
>>> 
