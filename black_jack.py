import random
class Cards():
    
    from random import shuffle
    deck = []
    def __init__(self):
        
        self.ranks = [ "Ace", "Jack", "Queen", "King", "2", "3", "4", "5", "6", "7","8", "9", "10" ]
        self.suits = [ "♠", "♢", "♡", "♣" ]
        self.values= {"A":11, "J":10, "Q":10, "K":10, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "1":10}
        
    def build_deck(self):
        self.deck = []
        for i in self.ranks:
            for j in self.suits:
                self.deck.append(i+j)
        return self.deck
    
    def shuffle_deck(self):
        return random.shuffle(self.deck)
    
    def draw_hand(self,hand):
        for card in self.deck:
            hand.append(self.deck.pop(0))
            if len(hand) == 2:
                return hand
        
    def hand_value(self,hand):
        total = 0
        x=' '
        for x in hand:
            val = self.values[x[:1]]
            total += val
        return total
    
    def hit_stay(self,handValue,hand):
        if handValue <= 21:
            result = ' '
            while not (result == 'H' or result == 'S'):
                result = input(" H for hit or S for stay :").upper()
            if result == 'H':
                hand.append(self.deck.pop(0))
            elif result == 'S':
                return 'Stay'
    
    def bust(self,pHand):
        if pHand > 21:
            return 'BUST'
        
    def winner(self,pHand=0,dHand=0):
        if pHand == dHand == 21:
            return 'DRAW'
        elif pHand > dHand:
            return 'Player WINS'
        elif pHand == dHand:
            return 'DRAW'
        else:
            return 'Dealer WINS'
    
    def replay(self):
        result = ' '
        while not (result == 'Y' or result == 'N'):
            result = input(" Y for yes or N for no ").upper()
        if result == 'Y':
            return True
        elif result == 'N':
            return False
             
    def __len__(self):
        return len(self.deck)


class Account:
    
    def __init__(self,owner,balance=0):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Account {self.owner}: Balance: {self.balance}."
    
    def deposit(self,val):
        self.balance += val
        #print(f"Deposit Accepted! {val} add to account!")
        
    def withdraw(self,val):
        if self.balance >= val : 
            self.balance -= val
            #print("Withdraw processed!")
        else:
            print("Insufficient funds!")


from IPython.display import clear_output
# BLACK JACK GAME
newDeck = Cards()
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