from Account import Account
from Deck import Deck

# from IPython.display import clear_output
# BLACK JACK GAME
newDeck = Deck()
newDeck.build_deck()
newDeck.shuffle_deck()

playerAcc = Account('Player',20)
dealerAcc = Account('Dealer',20)


def statusMessage(message):
    filler = 18 - len(message)
    print('---------------------')
    print('---- ' +message.center(filler)+ ' ----')
    print('---------------------')


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
    statusMessage('DEALING')
    player = []
    dealer = []
    
    player = newDeck.draw_hand(player)
    dealer = newDeck.draw_hand(dealer)
    
    print('DEALER', dealer[0])

    drawOn = True
    pHit = ''
    dHit = ''
    while drawOn:
        
        pHand = newDeck.hand_value(player)
        dHand = newDeck.hand_value(dealer)

        # PLAYER TURN
        if pHit != 'Stay':
            print('-------------------')
            print('PLAYER', *player, '('+str(pHand)+')', sep=' ')
            print('-------------------')
            #print(player)
            pHit = newDeck.hit_stay(pHand,player)
            pHand = newDeck.hand_value(player)
            if newDeck.bust(pHand) == 'BUST':
                print(player)
                playerAcc.withdraw(playerBet)
                dealerAcc.deposit(playerBet)
                statusMessage('PLAYER BUST')
                drawOn = False

        # DEALER TURN        
        elif dHit != 'Stay':
            print('--------------------')
            print('DEALER', *dealer, '('+str(dHand)+')', sep=' ')
            print('--------------------')
            dHit = newDeck.hit_stay(dHand,dealer)
            dHand = newDeck.hand_value(dealer)
            if newDeck.bust(dHand) == 'BUST':
                print(dealer)
                dealerAcc.withdraw(dealerBet)
                playerAcc.deposit(dealerBet)
                statusMessage('DEALER BUST')
                drawOn = False
        else:
        # WINNER CHECK
            check = newDeck.winner(pHand,dHand)
            if check == 'Player WINS':
                dealerAcc.withdraw(dealerBet)
                playerAcc.deposit(dealerBet)
                statusMessage('PLAYER WINS')
                drawOn = False
            elif check == 'Dealer WINS':
                playerAcc.withdraw(playerBet)
                dealerAcc.deposit(playerBet)
                statusMessage('DEALER WINS')
                drawOn = False
            else:
                statusMessage('DRAW')
                drawOn = False 
				
