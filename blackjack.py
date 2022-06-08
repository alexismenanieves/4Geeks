import random

class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
    
    def __repr__(self):
        return f'({self.suit},{self.value})'

suits = ['Spades','Hearts','Clubs','Diamonds']
suits_values = {'Spades': '\u2664', 'Hearts':'\u2661', 
               'Clubs': '\u2667', 'Diamonds':'\u2662'}
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards_values = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, 
                '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# Let's generetate a deck
deck = []
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, cards_values[card]))

def blackjack_game(deck):
    global cards_values

    player_cards = []
    player_score = 0 
    while len(player_cards) < 2:
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        player_score += player_card.card_value

        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
        
        print('Player cards: ')
        print(repr(player_cards))
        print(f'Player score: {player_score}')

        # And if you have a natural 21
        if player_score == 21:
            print('You have a Blackjack!')
            print('You win!')
            quit()

def blackjack_game_rep():
    global cards_values

    deck = [] 
    for suit in suits:
        for card in cards:
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    player_cards = []
    player_score = 0 
    while len(player_cards) < 2:
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        player_score += player_card.card_value

        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

    if player_score == 21:
        result = 1
    else:
        result = 0

    return result

acum = 0
n = 10000

for i in range(n): 
    acum += blackjack_game_rep()

print(f'The average of Natural 21 is: {acum/n}')