#####lab4.py####
###Arpan Patel####

def lineLengths(filename):
    total=0
    infile=open(filename)
    lines=infile.readlines()
    infile.close()
    for line in lines:
        total+=len(line)
        print(len(line), end='+')
    print('0='+str(total))
#test
'''
>>> corv()
Please enter a lower case letter: k
k is a consonant
>>> corv()
Please enter a lower case letter: i
i is a vowel
>>> corv()
Please enter a lower case letter: y
y is a consonant
>>>
'''

def monogram(word):
    output=''
    for letters in word.upper().split():
        output+=letters[0]
    return output
#Test
'''
>>> monogram('cher')
'C'
>>> monogram('George Washington')
'GW'
>>> monogram('george herbert walker bush')
'GHWB'
>>>
'''

def pay(rate,hours):
    pay=rate*hours
    if hours <=40:
        return(pay)
    elif hours >40 and hours <60:
        return(rate*40)  +  ((hours-40)*(rate)*1.5)
    else:
        hours > 60
        return(rate*40)  +  ((hours-40)*(rate)*2)
#test
'''
>>> monogram('cher')
'C'
>>> monogram('George Washington')
'GW'
>>> monogram('george herbert walker bush')
'GHWB'
>>>
''' 
def average(filename):

' Ran out of time so I could not finish the lab '


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab4TEST.py') )
