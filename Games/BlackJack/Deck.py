import random

class Deck():
    
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
                result = input(" (H)it or (S)tay :").upper()
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