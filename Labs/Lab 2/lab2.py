#########lab2.py########
#########Arpan Patel####

def initials():
    firstname = input('Please enter your first name: ')
    lastname= input('Please enter your last name: ')
    print ( firstname,lastname,'your initials are',firstname[0:1]+lastname[0:1])

#Test
'''
>>> initials()
Please enter your first name: Jane
Please enter your last name: Jones
Jane Jones your initials are JJ
>>> initials()
Please enter your first name: george
Please enter your last name: orwell
george orwell your initials are go
>>>

'''

def corv():
    letters =input('Please enter a lower case letter: ')
    vowel=('aeiou')
    if letters in vowel:
        print(letters,'is a vowel')
    else:
        print(letters, 'is a consonant')

#Test
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

def pigLatin():
    print('English to Pig Latin Translator')
    lowercase= input('Please enter a lower case English word: ')
    vowel=('aeiou')
    if lowercase[0:1] in vowel:
        print( lowercase, 'translates to', lowercase + 'ay')
    else:
        print(lowercase, 'translates to', lowercase[1:] + lowercase[0] + 'ay')

#Test
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
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab2TEST.py') )   

    

        
    
    
    
    
                     
    
