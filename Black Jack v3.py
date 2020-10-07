"""
This is a simple Black Jack Game I hope you enjoy Playing
"""

# noinspection PyUnresolvedReferences
import random

# Initializing some variable
suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': (11, 1)}


# Now we're gonna define some classes
# First we define Card so we can give each 52 cards of the game a certain attribute
class Card:

    def __init__(self, card, suit):
        self.suit = suit
        self.card = card
        self.value = card_value[card]

    def __str__(self):
        return f'{self.card} of {self.suit}'


# Second we need to define Deck for shuffling and dealing method to be carried out also holding 52 cards
class Deck:

    def __init__(self):
        self.aDeck = []
        for rank in ranks:
            for suit in suits:
                self.aDeck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.aDeck)

    def deal(self):
        return self.aDeck.pop()


class Player:

    def __init__(self, name='NoOne', balance=0):
        self.balance = balance
        self.name = name

    def bet(self, amount):
        self.balance -= amount

    def winbet(self, amount):
        self.balance += 2 * amount


def scores(P_hand, D_hand):
    global sump
    sump=0
    global  sumd
    sumd = 0
    for card in P_hand:
        try:
            sump += card.value
        except:
            sump11 = sump + card.value[0]
            sump1 = sump + card.value[1]
            sump = sump11
            if sump11 > 21:
                sump = sump1
    for card in D_hand:
        try:
            sumd += card.value
        except:
            sumd11 = sumd + card.value[0]
            sumd1 = sumd + card.value[1]
            sumd = sumd11
            if sumd11 > 21:
                sumd = sumd1


def check_winner(sump, sumd):
    if sump > sumd:
        print(f'Congratulation {player.name}, you have won')
        player.winbet(bet)
    elif sump < sumd:
        print('Dealer nailed your ass')


def bust(bet,sumd,sump):
    if sumd > 21 and sump > 21:
        print('Both busted')
        return False
    elif sumd > 21:
        print('Dealer got Busted')
        print(f'Congratulation {player.name}, you have won')
        player.winbet(bet)
        return False
    elif sump > 21:
        print(f'Sorry {player.name} you are busted')
        return False


game_on = True
name = input('Enter your Name: ')
balance = int(input('Enter you Current Balance: '))

while game_on:
    player = Player(name, balance)
    adeck = Deck()
    adeck.shuffle()
    D_hand = []
    P_hand = []
    bet = int(input('How much bet? '))
    player.bet(bet)
    for counter in range(2):
        D_hand.append(adeck.deal())
        P_hand.append(adeck.deal())
    showd = f'D: ?,{D_hand[1]}'
    showp = f'{player.name}: {P_hand[0]},{P_hand[1]}'
    print(showd, '\n', showp)
    stage = 2
    repeat = True
    while repeat:
        response = input('Hit or Stand? ')
        if response.lower() == 'hit':
            D_hand.append(adeck.deal())
            P_hand.append(adeck.deal())
            showd += (', ' + str(D_hand[stage]))
            showp += (', ' + str(P_hand[stage]))
            print(showd, '\n', showp)
            repeat = bust()
        elif response.lower() == 'stand':
            check_winner(P_hand, D_hand)
            repeat = False
        print(showd.replace('?', str(D_hand[0])))
        print(showp)
        print(f'Your Balance: {player.balance}')

    result = input('Another Time? (y/n)')
    if result == 'n':
        game_on = False
