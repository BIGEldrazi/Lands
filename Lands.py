import random
from collections import Counter

def main():
    table = Table(['Player1','Player2'])
    table.deal_cards()
    
def print_underline(string, line):
    print('\n{}\n{}'.format(string, line * len(string)))

class Table:

    def __init__(self, players):
        self.players = [Player(name, Hand()) for name in players]
        self.deck = Deck()
        self.rounds = 0

    def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_hands(self.players)
        for player in self.players:
            player.show_hand()

    def count_round(self):
        self.rounds += 1
        print_underline('Starting round {}'.format(self.rounds), '=')

    @property
    def finished(self):
        for player in self.players:                 
            if len(Counter(player.board).keys())==5 :
                return  1
        return 0
                    
class Player:

    board = []
    def __init__(self, name, hand):
        self.name, self.hand = name, hand
    
    def play_card(self,card):
        self.board.append(card)
        
    def show_hand(self):
        print(self.name, 'has', self.hand)
    

class Card:
    card = 'Mountain,Island,Swamp,Plains,Forest'.split(',')
    
    def __init__(self,card):
        self.card = card 
    
    def __str__(self):
        return  '{}'.format(self.card) 
        
class Hand:  
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def add_card(self, card):
        self.cards.append(card)

    def take_top(self):
        return self.cards.pop(0)

    def add_all(self, cards):
        self.cards.extend(cards)

    @property
    def has_cards(self):
        return bool(self.cards)
    
    
class Deck:
    def __init__(self):
        self.cards = [Card(n) for n in  Card.card for m in range(5)]  
    
    def shuffle(self):
       random.shuffle(self.cards)
       
    def setup_hands(self, players):
       hands =   [player.hand for player in players]
       for n in range(4):
           for hand in hands:
               hand.add_card(self.cards.pop())
       print(hands) 
       return hands
       
       
if __name__ == '__main__':
    main()
    