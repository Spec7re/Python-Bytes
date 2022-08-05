from Account import Account
from Deck import Deck

from IPython.display import clear_output
# BLACK JACK GAME
newDeck = Deck()
newDeck.build_deck()
newDeck.shuffle_deck()

playerAcc = Account('Player',20)
dealerAcc = Account('Dealer',20)

while True:
    try:
        bet = int(input("Enter your bet: "))
    except ValueError:
        print("Integer, please.")
    else:
        if bet > playerAcc.balance:
            print("Sorry, your bet can't exceed",playerAcc.balance)
        else:
            break
        
playerBet = dealerBet = bet

player = []
dealer = []

gameOn = True
while gameOn:
    
    if player != []:
        newDeck.deck.extend(player)
        newDeck.deck.extend(dealer)
    
    if playerAcc.balance == 0:
        print('NO CA$H')
        break
    elif dealerAcc.balance == 0:
        print("NO CA$H")
        break
        
    print(playerAcc)
    print('-------------------')
    print('----  DEALING  ----')
    print('-------------------')
    player = []
    dealer = []
    
    player = newDeck.draw_hand(player)
    dealer = newDeck.draw_hand(dealer)
    
    print(dealer[0])
    clear_output()
    drawOn = True
    pHit = ''
    dHit = ''
    while drawOn:
        
        pHand = newDeck.hand_value(player)
        dHand = newDeck.hand_value(dealer)

        # PLAYER TURN
        if pHit != 'Stay':
            print('PLAYER')
            print('------')
            print(*player, sep=' ')
            #print(player)
            print(pHand)
            pHit =newDeck.hit_stay(pHand,player)
            pHand = newDeck.hand_value(player)
            if newDeck.bust(pHand) == 'BUST':
                print(player)
                playerAcc.withdraw(playerBet)
                dealerAcc.deposit(playerBet)
                print ('-------------------')
                print ('--- PLAYER BUST ---')
                print ('-------------------')
                drawOn = False

        # DEALER TURN        
        elif dHit != 'Stay':
            print('DEALER')
            print('------')
            print(*dealer, sep=' ')
            print(dHand)
            dHit = newDeck.hit_stay(dHand,dealer)
            dHand = newDeck.hand_value(dealer)
            if newDeck.bust(dHand) == 'BUST':
                print(dealer)
                dealerAcc.withdraw(dealerBet)
                playerAcc.deposit(dealerBet)
                print ('-------------------')
                print ('--- DEALER BUST ---')
                print ('-------------------')
                drawOn = False
        else:
        # WINNER CHECK
            check = newDeck.winner(pHand,dHand)
            if check == 'Player WINS':
                dealerAcc.withdraw(dealerBet)
                playerAcc.deposit(dealerBet)
                print ('-------------------')
                print ('--- PLAYER WINS ---')
                print ('-------------------')
                drawOn = False
            elif check == 'Dealer WINS':
                playerAcc.withdraw(playerBet)
                dealerAcc.deposit(playerBet)
                print ('-------------------')
                print ('--- DEALER WINS ---')
                print ('-------------------')
                drawOn = False
            else:
                print('--DRAW--')
                print('--------')
                drawOn = False 
				
