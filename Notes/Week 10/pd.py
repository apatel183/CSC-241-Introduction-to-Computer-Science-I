# pd.py

# Final Exam
# Thurs, November 19, 2015, from 8:30 AM to 10:45 AM
# same rules as before
# 4 single sided OR 2 double sided pages of notes
# cumulative - we will review

# hw/lab - make sure you that are solving the
# problems yourself

'''
>>> pd( 'C','D')
(0,5)
'''

def pd(p0,p1):
    ''' p0 and p1, are each one of 'C' or 'D'
returns (v0,v1) outcome of playing one round of
Prisoner's Dilemma'''
    t = { 'CC':(3,3), 'CD':(0,5), 'DC':(5,0), 'DD':(1,1)}
    return t[p0+p1]

'''
>>> pdIterated( sCooperate, sDefect, 10)
(0,50)

note that the strategies are not being called here
they are passed as arguments

'''


def pdIterated( s0, s1, n):
    ''' strategy s0 plays strategy s1 for n rounds of
prisoner's dilemma, returns (total points0, total points1)'''

    points0=0
    points1=0
    history0=[]
    history1=[]
    for i in range(n):
        # note that [:] copies history
        # so that it cant be changed by the strategy
        p0 = s0(string(history0),string(history1))
        p1 = s1(string(history1),string(history0))
        result=pd(p0,p1)
        points0 += result[0]
        points1 += result[1]
        history0.append(p0)
        history1.append(p1)
    return (points0,points1)

'''
>>> pdRoundRobin( [sCooperate, sDefect, sRandom], 100)
... prints total results ...
'''
 
def pdRoundRobin( strategies, n ):
    ''' strategies is a list  of strategies, this function
plays each pair, keeps track of, and then prints scores'''

   
    strategies = list(set(strategies)) # removes duplicates
    scores = dict(zip(strategies,len(strategies)*[0]))
    for i in range(len(strategies)-1):
        for j in range(i+1,len(strategies)):
            s0 = strategies[i]
            s1 = strategies[j]
            print( s0,s1)
            results = pdIterated( s0,s1, n)
            scores[s0] += results[0]
            scores[s1] += results[1]
    # print results
    lst = [ (scores[s],scores[s]/n/(len(strategies)-1),s.__name__) for s in strategies]
    lst.sort()
    for tup in reversed(lst):
        print( tup[0],tup[1],tup[2],sep='\t')
    #print( scores )
    

def string( lst ):
    s = ''
    for item in lst:
        s+=str(item)
    return s
##### strategies #####

'''
every strategy is given its own history (myHistory)
and the opponents history (vsHistory)
and returns the next play, either 'C' or 'D'
'''

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


from allStrategies import *
strats = [sTitforTat,
sJoeFossing4,
sAaron21,
sJoeFossing1,
sJessica,
sLaurenBrookins1,
sKat3Strategy,
sSuckerES,
sCooperate,
sJoeFossing5,
sKyle,
sJoeFossing2,
sLaurenBrookins2,
sKevin2,
sTitForTat2,
sSam2,
sRandom,
sMichaelLarson,
sDefect,
sLaurenBrookins3,
sGaurav,
sYT3,
sHunter1,
sIsabellaTam,
sArpan,
sKat1Strategy,
sCounterPlay,
sWinnerES,
sYT1,
sJoeFossing3,
sZac,
sYT2,
sSam4,
sSam3,
sFrank,
sKat2Strategy,
sKevin1,
sJoeFossing6,
sFranco,
sGaurav1,
sTitForTat,
sAaron,
sSam1
    ]

'''

for s in strats:
    
    print(s)
    print( pdIterated(s,sRandom,100) )
'''

pdRoundRobin( strats, 100 )




           













    
    
    
