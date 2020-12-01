import xlsxwriter
from datetime import datetime
from math import ceil

def dealerCard(ownHand, pair):
    global game
    dCard = dealerCards[game]
    dCardV = int(values.get(dCard, dCard))
    if pair != 1:
        game+=1
    dealerHand = [dCard]
    dealerHandV = [dCardV]
    dealerValue = sum(dealerHandV,0)
    while dealerValue < 17:
        if ownHand > 21:
            break
        nextCard = input('What is the dealers next Card').upper()
        nextCardV = int(values.get(nextCard, nextCard))
        dealerHand.append(nextCard)
        dealerHandV.append(nextCardV)
        dealerValue = sum(dealerHandV,0)
        noOfAces = int(dealerHand.count('A'))
        if (dealerValue>21) and (dealerValue - (noOfAces*10))<22:
            dealerValue-=10  
        elif dealerValue>21:
            dealerValue=0
            break      
    return dealerValue


def didYouWin(ownHand, pair, dealerValue):
    print('Lets see if you Won')
    if pair != 1:
        dealerValue = dealerCard(ownHand, pair)
    betValue = betTracker[-1]
    if pair == 2:
        betValue = betValue*2
        betTracker[-1] == betValue
    balance = budgetChange[-1]
        
    if (ownHand<22) and (ownHand>dealerValue):
        print('Congrats on the Win')
        newBalance = balance+betValue
        budgetChange.append(newBalance)
        gameResult = 'Win'
        results.append(gameResult)
    elif (ownHand<22) and (ownHand==dealerValue):
        print('A draw, we can take that')
        budgetChange.append(balance)
        gameResult = 'Draw'
        results.append(gameResult)
    else:
        print('Unlucky, we lost that one')
        newBalance = balance-betValue
        budgetChange.append(newBalance)
        gameResult = 'Lose'
        results.append(gameResult)
    if pair != 1:
        newGame()
    return gameResult
        

def thirdCard(oneCardx, twoCardx, pair):
    oneCardV = int(values.get(oneCardx, oneCardx))
    twoCardV = int(values.get(twoCardx, twoCardx))
    thirdCardx = input('What is your third card').upper()
    thirdCardV = int(values.get(thirdCardx, thirdCardx))
    dCard = dealerCards[game]
    dCardV = int(values.get(dCard,dCard))
    
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
        elif (handValue - (noOfAces*10))>21:
#             print('Unlucky, Better luck next time')
            nextMove = False
            if pair == 1:
                break
            else:
                didYouWin(handValue ,pair, 0)
                break
        print(f'Your current hand is now {currentHand} with a value of {handValue}')
        
        if handValue>16 or ((handValue == (16 or 15 or 14 or 13)) and (dCardV < 7)) or ((handValue == 12) and (dCardV == (4 or 5 or 6))):
            print('You should stick')
            if pair == 1:
                break
            else:
                didYouWin(handValue ,pair, 0)
        else:
            print('You should hit')
            nextCard = input('What is the next Card').upper()
            nextCardV = int(values.get(nextCard, nextCard))
            currentHand.append(nextCard)
            currentHandV.append(nextCardV)               
                
                
    return handValue    
    
    
#Allows you to double
def hardHands(oneCard1, twoCard1, pair):
    oneCardX = int(values.get(oneCard1, oneCard1))
    twoCardX = int(values.get(twoCard1, twoCard1))
    hardTotal = oneCardX + twoCardX
    dCard = dealerCards[game]
    dCardV = int(values.get(dCard,dCard))
    #When to double        
    if hardTotal == 11 or ((hardTotal == 10) and dCardV<10) or ((hardTotal == 9) and ((dCardV !=2) or (dCardV>6))):
        if pair == 1:
            print('You should hit')
            thirdCard(oneCard1, twoCard1, pair)
        else:
            print('Go for the double!')
            doubleCard = input('What is your final card').upper()
            doubleCardV = int(values.get(doubleCard, doubleCard))
            hardTotal+=doubleCardV
            if ((hardTotal>21) and (doubleCardV == 11)):
                hardTotal-=10
            didYouWin(hardTotal, 2, 0)
    #When to stick
    elif (hardTotal>16) or ((hardTotal == (16 or 15 or 14 or 13)) and (dCardV < 6)) or ((hardTotal == 12) and (dCardV == (4 or 5 or 6))):
        print('You should stick')
        if pair != 1:            
            didYouWin(hardTotal, pair, 0)
    else:
        print('You should hit')
        hardTotal = thirdCard(oneCard1, twoCard1, pair)
    return hardTotal


#When one card is an ace
def softTotals(oneCard1, twoCard1, pair):
    oneCardS = int(values.get(oneCard1, oneCard1))
    twoCardS = int(values.get(twoCard1, twoCard1))
    soft_total = oneCardS+twoCardS
    global game
    dCard = dealerCards[game]
    dCardV = int(values.get(dCard,dCard))
    print(soft_total)
    
    #When a person should hold
    if (soft_total == 20 or 21) or ((soft_total == 19) and (dCardV != 6)) or ((soft_total == 18) and (dCardV == (7 or 8))):
        print('At this point you should hold! Good Luck!')
        if pair != 1:
            didYouWin(soft_total, pair, 0)
            #When a person should double    
    elif ((soft_total == 18) and (dCardV<7)) or \
            ((soft_total == 19) and (dCardV == 6)) or \
            ((soft_total == 17) and (dCardV == (3 or 4 or 5 or 6))) or \
            ((soft_total == (16 or 15)) and (dCardV == (4 or 5 or 6))) or \
            ((soft_total == (14 or 13)) and (dCardV == (5 or 6))):
        if pair == 1:
            print('You should stick')
        else:
            print('You should double! Hope it works')
            doubleCard = input('What is your final card').upper()
            doubleCardV = int(values.get(doubleCard, doubleCard))
            soft_Total+=doubleCardV
            if (soft_total > 21):
                soft_total-=10
            
            didYouWin(soft_total, 2, 0)
    else:
        print('You should hit')
        soft_total = thirdCard(oneCard1, twoCard1, pair)        
    return soft_total

#The same as split double except you can no longer split
def runPairs(oneCard1, twoCard1):
    oneCardP = int(values.get(oneCard1, oneCard1))
    twoCardP = int(values.get(twoCard1, twoCard1))       
    #If one of the cards is an ace    
    if (oneCardP == 11 or twoCardP == 11):
        handTotal = softTotals(oneCard1, twoCard1, 1)
    else:
        handTotal = hardHands(oneCard1, twoCard1, 1)
    
    return handTotal
    

#After splitting allows the user to play 2 seperate hands
def splitpairs(oneCard, twoCard):
    
    pairOneT = input(f'What card is dealt with {oneCard}').upper()
    print('First focus on hand with '+oneCard+' and '+pairOneT)
    pair1 = runPairs(oneCard, pairOneT)    
    print('Now the other deck')
    pairTwoT = input(f'What card is dealt with {twoCard}').upper()    
    betValue = betTracker[-1]
    betTracker.append(betValue)
    pair2 = runPairs(twoCard, pairTwoT)
    
    if (pair1 or pair2) <= 21:
        if pair1 <=21:
            dealerHand = dealerCard(pair1, 1)
        else:
            dealerHand = dealerCard(pair2, 1)
    else:
        dealerHand = 22
    
    gameResult = didYouWin(pair1, 1, dealerHand)
    print('Now looking at your second hand')    
    gameResult1 = didYouWin(pair2, 1, dealerHand)
    
    global game
    game+=1
    newGame()
#Decides if a person with matching cards should split or keep together    
def pairs(oneCard, twoCard):
    global game
    dCard = dealerCards[game]
    dCardV = int(values.get(dCard,dCard))
    oneCardV = int(values.get(oneCard, oneCard))
    if oneCardV == 11 or (oneCardV == 9 and (dCardV != (7 or 10 or 11))) or\
                    (oneCardV == 8) or \
                    (oneCardV == 7 and dCardV >7):
        print('You should split')
        splitpairs(oneCard, twoCard)
    else:
        print("Don't Split")
        hardHands(oneCard, twoCard, 0)
    return None


def startGame():
    firstBet = input('What is your bet value')
    firstBetV = float(firstBet)
    betTracker.append(firstBetV)
    oneCard = input('What is your first card? 2,3,4,5,6,7,8,9,10,J,Q,K,A?').upper()
    twoCard = input('What is your second card?').upper()
    dCard = input('What is the dealers card?').upper()
    dealerCards.append(dCard)    
    oneCardV = int(values.get(oneCard, oneCard))
    twoCardV = int(values.get(twoCard, twoCard))  
    dCardV = int(values.get(dCard, dCard))
    if (oneCardV == 11 or twoCardV == 11) and (oneCardV != twoCardV):
        softTotals(oneCard, twoCard, 0)
    elif oneCardV == twoCardV:
        pairs(oneCard, twoCard)
    else:
        hardHands(oneCard, twoCard, 0)
    

def newGame():
            
    start = input('Do you want a new Game? Enter Y for yes and N for no').upper()
    if start == 'Y':
        startGame()
    elif start == 'N':
        print('An excel document has been created to show your winnings')
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y %H_%M_%S")
        workbook = xlsxwriter.Workbook(f'blackjackResults{dt_string}.xlsx')
        worksheet = workbook.add_worksheet('Results')
        worksheet.write(0,0,'Result')
        worksheet.write(0,1,'Bet Value')
        worksheet.write(0,2,'Balance')
        
        row = 2
        column = 0
        rowB = 1
        columnB = 2
        rowT = 2
        columnT = 1
        for balance in budgetChange:
            worksheet.write(rowB,columnB,balance)
            rowB+=1
        for result in results:
            worksheet.write(row, column, result) 
            row+=1
        for bet in betTracker:
            worksheet.write(rowT,columnT,bet)
            rowT+=1
        worksheet.write(0,4,'Win Percentage')
        worksheet.write(1,4,'=COUNTIF(A2:A99999,"Win")/COUNTA(A2:A99999)')
        workbook.close()
        
    else:
        print('Please enter a valid input')
        newGame()
            

values = {
            'J':'10',
            'Q':'10',
            'K':'10',
            'A':'11'
            }




inputV = input('What is your starting budget')
initialBudget = float(inputV)
budgetChange = []
betTracker = []
budgetChange.append(initialBudget)
dealerCards = []
results = [] 
game = 0
startGame() 



