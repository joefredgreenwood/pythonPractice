import random

def eighthCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard, sixthCard, seventhCard):
    eighthCard = input('What is your eighth Card').upper()
    eightCardV = int(valuesAce.get(eighthCard, eighthCard))
    seventhCardV = int(valuesAce.get(seventhCard, seventhCard))
    sixthCardV = int(valuesAce.get(sixthCard, sixthCard))    
    fifthCardV = int(valuesAce.get(fifthCard, fifthCard))
    thirdCardV = int(valuesAce.get(thirdCard, thirdCard))
    forthCardV = int(valuesAce.get(forthCard, forthCard))
    oneCardF = int(valuesAce.get(oneCard1, oneCard1))
    twoCardF = int(valuesAce.get(twoCard1, twoCard1))
    finalTotal = oneCardF + twoCardF + thirdCardV + forthCardV +fifthCardV + sixthCardV + seventhCardV + eightCardV
    if finalTotal <22:
        print('Hold it, hope you win')
    else:
        print('Sorry you lost')    
    return eightCardV


def seventhCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard, sixthCard):
    seventhCard = input('What is your 7th Card').upper()
    seventhCardV = int(valuesAce.get(seventhCard, seventhCard))
    sixthCardV = int(valuesAce.get(sixthCard, sixthCard))    
    fifthCardV = int(valuesAce.get(fifthCard, fifthCard))
    thirdCardV = int(valuesAce.get(thirdCard, thirdCard))
    forthCardV = int(valuesAce.get(forthCard, forthCard))
    oneCardF = int(valuesAce.get(oneCard1, oneCard1))
    twoCardF = int(valuesAce.get(twoCard1, twoCard1))
    finalTotal = oneCardF + twoCardF + thirdCardV + forthCardV +fifthCardV + sixthCardV + seventhCardV
    if finalTotal <22:
        if finalTotal <12 and (oneCard1 or twoCard1 or thirdCard or forthCard or fifthCard or sixthCard or seventhCard) == 'A':
            finalTotal+=10
        if finalTotal>16 or ((finalTotal == 16 or 15 or 14 or 13) and dCardV < 7) or (finalTotal == 12 and (dCardV == 4 or 5 or 6)):
            print('You should stick')
        else:
            print('You should hit')
            EighthCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard, sixthCard, seventhCard)  
    else:
        print('Sorry you lost')    

    return seventhCardV


def sixthCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard):
    sixthCard = input('What is your 6th Card').upper()
    sixthCardV = int(valuesAce.get(sixthCard, sixthCard))    
    fifthCardV = int(valuesAce.get(fifthCard, fifthCard))
    thirdCardV = int(valuesAce.get(thirdCard, thirdCard))
    forthCardV = int(valuesAce.get(forthCard, forthCard))
    oneCardF = int(valuesAce.get(oneCard1, oneCard1))
    twoCardF = int(valuesAce.get(twoCard1, twoCard1))
    finalTotal = oneCardF + twoCardF + thirdCardV + forthCardV +fifthCardV + sixthCardV
    if finalTotal <22:
        if finalTotal <12 and (oneCard1 or twoCard1 or thirdCard or forthCard or fifthCard or sixthCard) == 'A':
            finalTotal+=10
        if finalTotal>16 or ((finalTotal == 16 or 15 or 14 or 13) and dCardV < 7) or (finalTotal == 12 and (dCardV == 4 or 5 or 6)):
            print('You should stick')
        else:
            print('You should hit')
            SixthCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard, sixthCard)  
    else:
        print('Sorry you lost')    
    return sixthCardV


def fifthCard(oneCard1, twoCard1, thirdCard, forthCard):
    fifthCard = input('What is your fifth Card').upper()
    fifthCardV = int(valuesAce.get(fifthCard, fifthCard))
    thirdCardV = int(valuesAce.get(thirdCard, thirdCard))
    forthCardV = int(valuesAce.get(forthCard, forthCard))
    oneCardF = int(valuesAce.get(oneCard1, oneCard1))
    twoCardF = int(valuesAce.get(twoCard1, twoCard1))
    finalTotal = oneCardF + twoCardF + thirdCardV + forthCardV +fifthCardV
    if finalTotal <22:
        if finalTotal <12 and (oneCard1 or twoCard1 or thirdCard or forthCard or fifthCard) == 'A':
            finalTotal+=10
        if finalTotal>16 or ((finalTotal == 16 or 15 or 14 or 13) and dCardV < 7) or (finalTotal == 12 and (dCardV == 4 or 5 or 6)):
            print('You should stick')
        else:
            print('You should hit')
            sixthCard(oneCard1, twoCard1, thirdCard, forthCard, fifthCard)  
    else:
        print('Sorry you lost')    
    return fifthCardV
    


def forthCard(oneCard1, twoCard1, thirdCard1):
    oneCardX = int(values.get(oneCard1, oneCard1))
    twoCardX = int(values.get(twoCard1, twoCard1))
    thirdCard1 = thirdCard1
    thirdCardV = int(values.get(thirdCard1, thirdCard1))
    forthCard = input('What is the value of the forth card').upper()
    forthCardV = int(values.get(forthCard, forthCard))
    hardTotal = oneCardX + twoCardX + thirdCardV + forthCardV
    if hardTotal > 21 and (thirdCard1 or forthCard or oneCard1 or twoCard1) == 'A':
        if (hardTotal - 10)<21:
            hardTotal -=10
        elif (hardTotal -20)<21 and ((oneCard1 and thirdCard1) or (oneCard1 and forthCard) or (twoCard1 and thirdCard1) or (twoCard1 and forthCard) or (thirdCard1 and forthCard)) == 'A':
            hardTotal -=20
        elif (hardTotal-30)<21 and ((oneCard1 and twoCard1 and thirdCard1) or (oneCard1 and twoCard1 and forthCard) or (twoCard1 and thirdCard1 and forthCard)) == 'A':
            hardtotal-=30
 

    if hardTotal < 22:
    #When to stick
        if hardTotal>16 or ((hardTotal == (16 or 15 or 14 or 13)) and (dCardV < 7)) or ((hardTotal == 12) and (dCardV == (4 or 5 or 6))):
            print('You should stick')
        else:
            print('You should hit')
            fifthCard(oneCard1, twoCard1, thirdCard1, forthCard)  
    else:
        print('Sorry you lost')         
    
    return forthCardV


def thirdCard(oneCard1, twoCard1):
    oneCardZ = int(values.get(oneCard1, oneCard1))
    twoCardZ = int(values.get(twoCard1, twoCard1))    
    thirdCard = input('What is your third card?').upper()
    thirdCardX = int(values.get(thirdCard, thirdCard))
    hardTotal = oneCardZ + twoCardZ + thirdCardX
    
    if hardTotal > 21 and thirdCard == 'A':
        hardTotal = oneCardZ + twoCardZ + 1
    elif hardTotal > 21 and thirdCard != 'A' and (oneCard or twoCard) == 'A':
        oneCardA = valuesAce.get(oneCard, oneCard)
        twoCardA = valuesAce.get(twoCard, twoCard)
        hardTotal = oneCardA + twoCardA + thirdCardX
    else:
        hardTotal = oneCardZ + twoCardZ + thirdCardX
    
    if hardTotal<22:
    #When to stick
        if (hardTotal>16) or ((hardTotal == (16 or 15 or 14 or 13)) and (dCardV < 7)) or ((hardTotal == 12) and (dCardV == (4 or 5 or 6))):
            print('You should stick')
        else:
            print('You should hit')
            forthCard(oneCard1, twoCard1, thirdCard)    
    else:
        print('Better luck next time')
    
    return thirdCard


def hardHands(oneCard1, twoCard1):
    oneCardX = int(values.get(oneCard1, oneCard1))
    twoCardX = int(values.get(twoCard1, twoCard1))
    hardTotal = oneCardX + twoCardX
    #When to double
    if hardTotal == 11 or (hardTotal == 10 and dCardV<10) or (hardTotal == 9 and (dCardV !=2 or dCardV>6)):
        print('Go for the double!')
    #When to stick
    elif hardTotal>16 or ((hardTotal == 16 or 15 or 14 or 13) and dCardV < 6) or (hardTotal == 12 and (dCardV == 4 or 5 or 6)):
        print('You should stick')
    else:
        print('You should hit')
        thirdCard(oneCard1, twoCard1)
    return None





def softTotals(oneCard1, twoCard1):
    oneCardS = int(values.get(oneCard1, oneCard1))
    twoCardS = int(values.get(twoCard1, twoCard1))
    
    soft_total = oneCardS+twoCardS
           #When a person should hold
    if soft_total == 20 or 21 or (soft_total == 19 and dCardV != 6) or (soft_total == 18 and (dCardV == 7 or 8)):
        print('At this point you should hold! Good Luck!')
            #When a person should double    
    elif (soft_total == 18 and dCardV<7) or \
            (soft_total == 19 and dCardV == 6) or \
            (soft_total == 17 and (dCardV == 3 or 4 or 5 or 6)) or \
            ((soft_total == 16 or 15) and (dCardV == 4 or 5 or 6)) or \
            ((soft_total == 14 or 13) and (dCardV == 5 or 6)):
        print('You should double! Hope it works')
    else:
        print('You should hit')
        thirdCard(oneCard1, twoCard1)        
    return soft_total

def runPairs(oneCard1, twoCard1):
    oneCardP = int(values.get(oneCard1, oneCard1))
    twoCardP = int(values.get(twoCard1, twoCard1))       
    #If one of the cards is an ace    
    if (oneCardP == 11 or twoCardP == 11) and (oneCardP != twoCardP):
        softTotals(oneCard1, twoCard1)
    else:
        hardHands(oneCard1, twoCard1)

    


def splitpairs():
    pairOneT = input('Next Card Dealt?')
    print('First focus on deck with '+oneCard+' and '+pairOneT)
    runPairs(oneCard, pairOneT)
    print('Now the other deck')
    pairTwoT = input('And the remaining Card?')
    
    runPairs(twoCard, pairTwoT)
    
def pairs():
    oneCardV = int(values.get(oneCard, oneCard))
    if oneCardV == 11 or (oneCardV == 9 and (dCardV != 7 or 10 or 11)) or\
                    (oneCardV == 8) or \
                    (oneCardV == 7 and dCardV >7):
        print('You should split')
        splitpairs()
    else:
        print("Don't Split")
        hardHands(oneCard, twoCard)
    return None


def splitDouble_cards():         
    #If one of the cards is an ace    
    if (oneCardV == 11 or twoCardV == 11) and (oneCardV != twoCardV):
        softTotals(oneCard, twoCard)
    elif oneCardV == twoCardV:
        pairs()
    else:
        hardHands(oneCard, twoCard)


can_split_cards = input('Does your site allow you to split your cards? Y or N?').upper()
can_double_cards = input('Does your site allow you to double? Y or N?').upper()
oneCard = input('What is your first card? 2,3,4,5,6,7,8,9,10,J,Q,K,A?').upper()
twoCard = input('What is your second card?').upper()
dCard = input('What is the dealers card?').upper()

values = {
            'J':'10',
            'Q':'10',
            'K':'10',
            'A':'11'
            }
valuesAce = {
    'J':10,
    'Q':10,
    'K':10,
    'A':1
    }
oneCardV = int(values.get(oneCard, oneCard))
twoCardV = int(values.get(twoCard, twoCard))  
dCardV = int(values.get(dCard, dCard))
if can_split_cards == 'Y' and can_double_cards == 'Y':
    splitDouble_cards()
else: 
    no_split()
    












   
    
    def no_split():
        return none
        
