def thirdCard(oneCardx, twoCardx):
    oneCardV = int(values.get(oneCardx, oneCardx))
    twoCardV = int(values.get(twoCardx, twoCardx))
    thirdCardx = input('What is your third card').upper()
    thirdCardV = int(values.get(thirdCardx, thirdCardx))
    
    currentHand = [oneCardx, twoCardx, thirdCardx]
    currentHandV = [oneCardV, twoCardV, thirdCardV]
    nextMove = True
    while nextMove == True:
        handValue = sum(currentHandV, 0)
        noOfAces = int(currentHand.count('A'))
        #Taking in to account aces can be high or low, automatically they are assigned high
        if (handValue>21) and (handValue - (noOfAces*10))<22:
            while handValue>21: #The if statement proves this is attainable without breaking the rules of blackjack
                handValue-=10
        elif (handValue - (noOfAces*10))>22:
            print('Unlucky, Better luck next time')
            nextMove = False
            break
        print(f'Your current hand is now {currentHand} with a value of {handValue}')
        
        if handValue>16 or ((handValue == (16 or 15 or 14 or 13)) and (dCardV < 7)) or ((handValue == 12) and (dCardV == (4 or 5 or 6))):
            print('You should stick')
            nextMove = False
            break
        else:
            print('You should hit')
            nextCard = input('What is the next Card').upper()
            nextCardV = int(values.get(nextCard, nextCard))
            currentHand.append(nextCard)
            currentHandV.append(nextCardV)               
                
                
    return handValue    
    
    
#Allows you to double
def hardHands(oneCard1, twoCard1):
    oneCardX = int(values.get(oneCard1, oneCard1))
    twoCardX = int(values.get(twoCard1, twoCard1))
    hardTotal = oneCardX + twoCardX
    #When to double
    if hardTotal == 11 or ((hardTotal == 10) and dCardV<10) or ((hardTotal == 9) and ((dCardV !=2) or (dCardV>6))):
        print('Go for the double!')
    #When to stick
    elif (hardTotal>16) or ((hardTotal == (16 or 15 or 14 or 13)) and (dCardV < 6)) or ((hardTotal == 12) and (dCardV == (4 or 5 or 6))):
        print('You should stick')
    else:
        print('You should hit')
        thirdCard(oneCard1, twoCard1)
    return None


#When one card is an ace
def softTotals(oneCard1, twoCard1):
    oneCardS = int(values.get(oneCard1, oneCard1))
    twoCardS = int(values.get(twoCard1, twoCard1))
    
    soft_total = oneCardS+twoCardS
    #When a person should hold
    if soft_total == (20 or 21) or ((soft_total == 19) and (dCardV != 6)) or ((soft_total == 18) and (dCardV == (7 or 8))):
        print('At this point you should hold! Good Luck!')
            #When a person should double    
    elif ((soft_total == 18) and (dCardV<7)) or \
            ((soft_total == 19) and (dCardV == 6)) or \
            ((soft_total == 17) and (dCardV == (3 or 4 or 5 or 6))) or \
            ((soft_total == (16 or 15)) and (dCardV == (4 or 5 or 6))) or \
            ((soft_total == (14 or 13)) and (dCardV == (5 or 6))):
        print('You should double! Hope it works')
    else:
        print('You should hit')
        thirdCard(oneCard1, twoCard1)        
    return soft_total

#The same as split double except you can no longer split
def runPairs(oneCard1, twoCard1):
    oneCardP = int(values.get(oneCard1, oneCard1))
    twoCardP = int(values.get(twoCard1, twoCard1))       
    #If one of the cards is an ace    
    if (oneCardP == 11 or twoCardP == 11) and (oneCardP != twoCardP):
        softTotals(oneCard1, twoCard1)
    else:
        hardHands(oneCard1, twoCard1)

    

#After splitting allows the user to play 2 seperate hands
def splitpairs():
    pairOneT = input(f'What card is dealt with {oneCard}').upper()
    print('First focus on deck with '+oneCard+' and '+pairOneT)
    runPairs(oneCard, pairOneT)
    print('Now the other deck')
    pairTwoT = input(f'What card is dealt with {twoCard}').upper()    
    runPairs(twoCard, pairTwoT)
    
#Decides if a person with matching cards should split or keep together    
def pairs():
    oneCardV = int(values.get(oneCard, oneCard))
    if oneCardV == 11 or (oneCardV == 9 and (dCardV != (7 or 10 or 11))) or\
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


# can_split_cards = input('Does your site allow you to split your cards? Y or N?').upper()
# can_double_cards = input('Does your site allow you to double? Y or N?').upper()
oneCard = input('What is your first card? 2,3,4,5,6,7,8,9,10,J,Q,K,A?').upper()
twoCard = input('What is your second card?').upper()
dCard = input('What is the dealers card?').upper()

values = {
            'J':'10',
            'Q':'10',
            'K':'10',
            'A':'11'
            }

oneCardV = int(values.get(oneCard, oneCard))
twoCardV = int(values.get(twoCard, twoCard))  
dCardV = int(values.get(dCard, dCard))
# if can_split_cards == 'Y' and can_double_cards == 'Y':
#     splitDouble_cards()
# else:
#     print('go somewhere you can')
splitDouble_cards()
