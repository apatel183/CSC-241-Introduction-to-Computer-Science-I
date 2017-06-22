#######hw2.py######
#######Arpan Patel#######

#######returnThree######
def returnThree(letters):
    if len(letters)>=3:
        return letters[0:3]
    else:
        return ''

####returnN#####

def returnN(a,b):
    if len(a)>=b:
        return(a[0:b])
    else:
        return ''

####firstchars#####
def firstChars(itemlist):
    if itemlist==([]):
        print('The list provided as a parameter was empty.')
    else:
        for char in itemlist:
            if len(char) !=0:
                print(char[:1])


####printerGreater######

def printGreater(lstNum,number):
    for num in lstNum:
        if num>number:
            print(num,end= " ")
    else:
        return 

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw2TEST.py') )


