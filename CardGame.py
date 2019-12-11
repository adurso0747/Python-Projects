#Coding excersise for Maxeta Technologies written in python. Author Alexander Durso
#Python Version 3.7.4, created with PyCharm

import random
class Player(object):
    """Creates a player instance"""

    def __init__(self, name, score, number, current_card):
        """Instances differ by name, score, number, and current card"""
        self.name = name
        self.score = score
        self.number = number
        self.current_card = current_card

    def change_score(self, result):
        """Changes a player's score"""
        if (result == 2):
            self.score += result
        if(result == 1):
            if(self.score > 0):
                self.score -= result

    def change_card(self, card):
        """Changes a player's current card"""
        self.current_card = card

class Card(object):
    """Creates a card instance"""
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face


def deck():
    """Returns an list that represents a standard deck of
    52 cards plus four penalty cards"""
    list = []
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    faces = [2, 3, 4, 5,
             6, 7, 8, 9, 10,
             'Jack', 'Queen', 'King', 'Ace']

    for x in faces:
        for i in suits:
            list.append(Card(i, x))

    for x in range(4):
        list.append(Card(x, 'Penalty'))

    return list


def compare(players_list):
    """Returns the player who is currently holding the
    highest rated card"""
    max_suit = 0
    max_face = 0
    max_player = None
    for i in players_list:
        if (i.current_card.face != 'Penalty'):
            if i.current_card.face == 'Jack':
                card_face = 11

            elif i.current_card.face == 'Queen':
                card_face = 12

            elif i.current_card.face == 'King':
                card_face = 13

            elif i.current_card.face == 'Ace':
                card_face = 14
            else:
                card_face = i.current_card.face

            if i.current_card.suit == 'Spades':
                card_suit = 4

            elif i.current_card.suit == 'Hearts':
                card_suit = 3

            elif i.current_card.suit == 'Diamonds':
                card_suit = 2

            elif i.current_card.suit == 'Clubs':
                card_suit = 1

            if (card_face == max_face):
                if (card_suit > max_suit):
                    max_face = card_face
                    max_suit = card_suit
                    max_player = i
            else:
                if (card_face > max_face):
                    max_face = card_face
                    max_suit = card_suit
                    max_player = i

    return max_player


def game():
    """Plays the card game"""
    game_finished_flag = 0
    print("Welcome to the card game. Please enter the number of players.")
    while True:
        try:
            num = int(input())
            if (num >= 2 and num <= 4):
                break
            else:
                print("Please enter a number between two and four.")
        except:
            print("Please enter an integer")

    players = [0] * (num)

    for i in range(num):
        print("Please enter a name for player " + str(i + 1))
        name = str(input())
        players[i] = Player(name, 0, i, None)

    while(game_finished_flag == 0):
        deck_list = deck()
        #Shuffle deck
        random.shuffle(deck_list)
        for i in players:
            print('Player ' + i.name + ", it is"
                  " currently your turn. Please press enter to draw card.")
            input()

            card = deck_list.pop()

            if card.face == 'Penalty':
                print("You have selected a penalty card\n")
                i.change_card(Card('Penalty', 'Penalty'))
                i.change_score(1)
            else:
                print('You have selected the ' + str(card.face) +
                      ' of ' + card.suit + '.\n')
                i.change_card(card)

        max_player = compare(players)
        print(max_player.name + " wins this round with a " +
              str(max_player.current_card.face) + " of " + max_player.current_card.suit + ".\n")

        for i in players:
            if i == max_player:
                i.change_score(2)

        for i in players:
            print(i.name + "'s current score = " + str(i.score) + ".")

        print('\n')
        max_score = 0
        for i in players:
            if i.score > max_score:
                max_score = i.score

        #Check that there are no duplicate max scores over 21 and that
        #scores over 21 exceed all other scores by at least 2
        scores = []
        if(max_score >= 21):
            game_finished_flag = 1
            for i in players:
                if i.score >= 21:
                    if i.score in scores:
                        if i.score == max_score:
                            game_finished_flag = 0
                    else:
                        scores.append(i.score)
                if i.score == (max_score - 1):
                    game_finished_flag = 0


    for i in players:
        if i.score == max_score:
            print(i.name + " wins with a score of " +
                  str(i.score) + "!")

if __name__ == '__main__':
    game()
