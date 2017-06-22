
import random
def sFrank (myhistory=None, vshistory=None):
    return random.choice ('CD')

def sFranco (myhistory=None, vshistory=None):
    if len(myhistory) == 0:
        return 'D'
    else:
        return vshistory[-1]

import random
def sKat1Strategy (myHistory=None,vsHistory=None):
    return random.choice ('CD')

def sKat2Strategy (myHistory=None, vsHistory=None):
    return 'D'

def sKat3Strategy (myHistory=None, vsHistory=None):
    return random.choice ('CD')
        
    

def sTitforTat (myHistory=None, vsHistory=None):
        if len (vsHistory)== 0:
                return 'D'
        else:
            return vsHistory [-1]

import random
def sJessica(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    elif 'DDDDD' in (vsHistory):
        return 'D'
    elif 'CCCCC' in (vsHistory):
        return 'C'
    elif random.randint(0,9)==4:
        return 'D'
    
    else:
        return random.choice(vsHistory)
    
def sLaurenBrookins1(myHistory=None, vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    else:
        return vsHistory[-1]

def sLaurenBrookins2(myHistory=None, vsHistory=None):
    if len(myHistory)==0:
        return 'D'
    elif myHistory[-1]=='D':
        return 'C'
    else:
        return 'D'

import random
def sLaurenBrookins3(myHistory=None, vsHistory=None):
    if len(myHistory)==0:
        return random.choice('CD')
    else:
        return random.choice(vsHistory)


    
##Tomasz Wegrzyn

def sCounterPlay(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return random.choice('CD')
    else:
        count1 = 0
        count2 = 0
        for item in vsHistory:
            if item is ("C"):
                   count1 += 1
            elif item is "D":
                   count2 += 1
        if count2 > count1:
            return "C"
        else:
            return random.choice('CD')


















    
    
    
import random
def sIsabellaTam(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'D'
    elif vsHistory[0]=='C':
        return 'C'
    else:
        return vsHistory[-1]
def sAaron(myHistory=None, vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    if myHistory[-1]== "C":
        return 'D'
    return "C"

def sAaron21(myHistory=None, vsHistory=None):
    if len(vsHistory)==0:
        return 'D'
    if vsHistory[-1]== "C":
        return 'D'
    if vsHistory[-1]== "D":
        return 'C'

#Kyle Surowiec

def sKyle(myHistory = None, vsHistory = None):
    import random
    num = random.randint(0,10)

    if num%2 == 0:
        return random.choice('CD')
    if len(myHistory) == 0:
        return 'D'
    if len(myHistory) != 2:
        return vsHistory[-1]
    if vsHistory[-1] == vsHistory[-2]:
        return 'C'
    else:
        return 'D'
import random
def sSam1(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'D'
    elif myHistory[-1]=='D':
        return 'C'
    else:
        return 'D'

def sSam2(myHistory=None,vsHistory=None):
    if len(myHistory)==0:
        return 'C'
    elif myHistory[-1]=='C':
        return 'D'
    else:
        return 'C'

def sSam3(myHistory=None,vsHistory=None):
    if len(myHistory)==0:
        return 'C'
    elif 'D' in vsHistory:
        return 'D'
    else:
        return 'C'

def sSam4(myHistory=None,vsHistory=None):
    if len(myHistory)==0:
        return 'C'
    else:
        return random.choice(vsHistory)
def sHunter1(mmyHistory=None,vsHistory=None):
    if len(vsHistory)<=5:
        return 'D'
    else:
        if vsHistory[-1] == 'C':
            return('D')
        elif vsHistory[-2] == 'C':
            return('D')
        elif vsHistory[-1] == 'C' and vsHistory[-2] == 'C' and vsHistory[-1] == 'C':
            return('D')
        elif vsHistory[-1] == 'D' and vsHistory[-2] == 'D':
            return('D')
        else:
            return(random.choice('CD'))
import random
def sKevin1(myHistory=None, vsHistory=None):
    if len(vsHistory) == 0:
        return random.choice('CD')
    let = 'C'
    n = -1
    if let in vsHistory[n]:
        return 'D'
        n -= 1
    else:
        return 'C'
        n += 1

def sKevin2(myHistory=None, vsHistory=None):
    if len(vsHistory) == 0:
        return 'D'
    let = 'C'
    n = -1
    if let in vsHistory[n]:
        return vsHistory[-1]
        n -= 1
    else:
        return vsHistory[-1]
        n += 1
    


import random
def sZac(myHistory=None,vsHistory=None):
    if len(vsHistory)==0 or len(vsHistory)%3==0:
        return 'C'
    elif len(vsHistory)%7 ==0:
        return vsHistory[random.randrange(0,len(vsHistory))]
    else:
        return vsHistory[-1]

















    
    
    
#Prisoner Game

'''-If opponent playing coop play with them
    -
    '''
import random
def sMichaelLarson(myHistory=None,vsHistory=None):
    if len(vsHistory)<=20:
        return 'C'
    else:
        return 'D'
    
    
import random
def sJoeFossing1(myHistory=None,vsHistory=None):
    if vsHistory=='C':
        return 'C'
    else:
        return 'D'

def sJoeFossing2(myHistory=None,vsHistory=None):
    if random.randrange(2)==0:
        return 'D'
    else:
        return 'C'

def sJoeFossing3(myHistory=None,vsHistory=None):
    if random.randrange(5)==0:
        return 'D'
    else:
        return 'C'

def sJoeFossing4(myHistory=None,vsHistory=None):
    if random.randrange(10)==0:
        return 'D'
    else:
        return 'C'

def sJoeFossing5(myHistory=None,vsHistory=None):
    if random.randrange(5)==0:
        return 'D'
    else:
        return 'C'
def sJoeFossing6(myHistory=None,vsHistory=None):
    if random.randrange(5)==0:
        return 'C'
    else:
        return 'D'
##### Gaurav Patel #####

import random
def sGaurav(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'D'
    elif myHistory[-1]=='D':
        return 'C'
    else:
        return 'D'


def sGaurav1(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    elif myHistory[-1]=='C':
        return 'D'
    else:
        return 'C'


import random
def sArpan(myHistory=None,vsHistory=None):
    if len(myHistory)==0:
          return 'C'
    else:
          return random.choice(myHistory)
def sYT1(myHistory=None,vsHistory=None):
    if len(vsHistory)<2:
        return 'C'
    else:
        return vsHistory[-2]
    
def sYT2(myHistory=None,vsHistory=None):
    result=[]
    if len(vsHistory)==0:
        return 'C'
    elif len(vsHistory)%10==0:
        for i in range(-10,0):
            result.append(vsHistory[i])
        Max=max(result)
        if Max=='D':
            return 'C'
        else:
            return vsHistory[-1]
    elif len(vsHistory)>0:
        return vsHistory[-1]

import random
def sYT3(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    elif len(vsHistory)%10==0:
        return random.choice('CD')
    else:
        return vsHistory[-1]

def sCooperate(myHistory=None,vsHistory=None ):
    return 'C'

def sDefect(myHistory=None,vsHistory=None):
    return 'D'

import random
def sRandom(myHistory=None,vsHistory=None):
    return random.choice( 'CD' )

# starts by cooperateing, otherwise returns opponnents last move
def sTitForTat(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    else:
        return vsHistory[-1]

def sTitForTat2(myHistory=None,vsHistory=None):
    if len(vsHistory)==0:
        return 'C'
    else:
        return vsHistory[-1]



def sSuckerES(myHistory=None,vsHistory=None):

    if len(myHistory)<5:
        return 'CDCDD'[len(myHistory)]
    elif list(myHistory[:5])==list('CDCDD') and list(vsHistory[:5]) == list('CCDCC'):
        return 'C'
    else:
        return 'D'

def sWinnerES(myHistory=None,vsHistory=None):

    if len(myHistory)<5:
        return 'CCDCC'[len(myHistory)]
    elif list(myHistory[:5])== list('CCDCC') and list(vsHistory[:5]) == list('CDCDD'):
        return 'D'
    else:
        return vsHistory[-1]
