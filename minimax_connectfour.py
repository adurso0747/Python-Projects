import copy
import time
import abc
import random
import math


class Game(object):
    """A connect four game."""

    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        # YOU FILL THIS IN
        moves = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                mark = self.grid[r][c]
                if(mark == '-'):
                    if(c not in moves):
                        moves.append(c)
        return moves



    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        # YOU FILL THIS IN
        row_locations = []
        for r in range(len(self.grid)):
            mark = self.grid[r][col]
            if (mark == '-'):
                if (r not in row_locations):
                    row_locations.append(r)
        bottom_row = max(row_locations)
        self.grid[bottom_row][col] = color;
        game = Game(self.grid)
        return game

    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN
        red_count = 0
        black_count = 0
        game = Game(self.grid)
        if(game.winning_state() == float('inf')):
            return float('inf')
        elif(game.winning_state() == float('-inf')):
            return float('-inf')
        elif(game.winning_state() == 0):
            return 0
        #counts the number of discs in a row and assigns weight
        else:
            return (game.count_discs('R') - game.count_discs('B'))


    def count_discs(self, color):
        one_disc = 0
        two_disc = 0
        three_disc = 0
        #check rows
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if (self.grid[r][c] == color):
                    if(c<7):
                        if(self.grid[r][c+1] == color):
                            if (c<6):
                                if(self.grid[r][c+2] == color):
                                    three_disc += 1
                                else:
                                    two_disc +=1
                            else:
                                two_disc +=1
                        else:
                            one_disc += 1
                    else:
                        one_disc +=1
        #check columns
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if (self.grid[r][c] == color):
                    if(r<7):
                        if(self.grid[r+1][c] == color):
                            if (r<6):
                                if(self.grid[r+2][c] == color):
                                    three_disc += 1
                                else:
                                    two_disc +=1
                            else:
                                two_disc +=1
                        else:
                            one_disc += 1
                    else:
                        one_disc +=1
        #check right diags
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if (self.grid[r][c] == color):
                    if(r<7 and c <7):
                        if(self.grid[r+1][c+1] == color):
                            if (r<6 and c<6):
                                if(self.grid[r+2][c+2] == color):
                                    three_disc += 1
                                else:
                                    two_disc +=1
                            else:
                                two_disc +=1
                        else:
                            one_disc += 1
                    else:
                        one_disc +=1
        # check left diags
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (self.grid[r][c] == color):
                    if (r < 7 and c > 0):
                        if (self.grid[r + 1][c - 1] == color):
                            if (r < 6 and c > 1):
                                if (self.grid[r + 2][c - 2] == color):
                                    three_disc += 1
                                else:
                                    two_disc += 1
                            else:
                                two_disc += 1
                        else:
                            one_disc += 1
                    else:
                        one_disc += 1
        return (one_disc + (two_disc * 4) + (three_disc * 16))


    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        # YOU FILL THIS IN
        game = Game(self.grid)
        possible_moves = game.possible_moves()
        if(len(possible_moves) == 0):
            return 0
        red = "R"
        black = "B"
        # check rows
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if(c < 5):
                    if(self.grid[r][c] == red and self.grid[r][c+1] == red
                    and self.grid[r][c+2] == red and self.grid[r][c+3] == red):
                        return float('inf')
                    if (self.grid[r][c] == black and self.grid[r][c + 1] == black
                            and self.grid[r][c + 2] == black and self.grid[r][c + 3] == black):
                        return float('-inf')

        #check columns
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if(r < 5):
                    if(self.grid[r][c] == red and self.grid[r+1][c] == red
                    and self.grid[r+2][c] == red and self.grid[r+3][c] == red):
                        return float('inf')
                    if (self.grid[r][c] == black and self.grid[r+1][c] == black
                            and self.grid[r+2][c] == black and self.grid[r+3][c] == black):
                        return float('-inf')
        #check right diags
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if(r < 5 and c < 5):
                    if (self.grid[r][c] == red and self.grid[r + 1][c+1] == red
                            and self.grid[r + 2][c+2] == red and self.grid[r + 3][c+3] == red):
                        return float('inf')
                    if (self.grid[r][c] == black and self.grid[r+1][c+1] == black
                            and self.grid[r+2][c+2] == black and self.grid[r+3][c+3] == black):
                        return float('-inf')
        #check left diags
        for r in range (len(self.grid)):
            for c in range(len(self.grid[r])):
                if(r < 5 and c > 2):
                    if (self.grid[r][c] == red and self.grid[r + 1][c-1] == red
                            and self.grid[r + 2][c-2] == red and self.grid[r + 3][c-3] == red):
                        return float('inf')
                    if (self.grid[r][c] == black and self.grid[r+1][c-1] == black
                            and self.grid[r+2][c-2] == black and self.grid[r+3][c-3] == black):
                        return float('-inf')

        return None




class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass

class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # YOU FILL THIS IN
        return random.choice(game.possible_moves())

class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        # YOU FILL THIS IN
        possible_moves = game.possible_moves()
        return possible_moves[0]

class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        # YOU FILL THIS IN
        newGame = copy.deepcopy(game)
        tuple = MinimaxAgent.max_value(Agent, newGame, 4)
        return tuple[0]
    def max_value(self, game, depth):
        max_value = 0
        move = 0
        if(game.winning_state() != None):
            return game.utility()
        elif (depth == 1):
            return game.utility()
        else:
            for i in game.possible_moves():
                newGame = copy.deepcopy(game)
                newGame = newGame.neighbor(i,'R')
                temp_value = MinimaxAgent.min_value(Agent, newGame,depth-1)
                if(isinstance(temp_value,tuple)):
                    temp2 = temp_value[1]
                    if(temp2 >= max_value):
                        max_value = temp2
                        move = i
                elif (temp_value != None):
                    if (temp_value >= max_value):
                        max_value = temp_value
                        move = i

        return (move, max_value)

    def min_value(self, game, depth):
        min_value = 0
        move = 0
        if (game.winning_state() != None):
            return game.utility()
        elif(depth == 1):
            return game.utility()
        else:
            for i in game.possible_moves():
                newGame = copy.deepcopy(game)
                newGame = newGame.neighbor(i, 'B')
                temp_value = MinimaxAgent.max_value(Agent, newGame, depth -1)
                if (isinstance(temp_value, tuple)):
                    temp2 = temp_value[1]
                    if (temp2 <= min_value):
                        min_value = temp2
                        move = i
                elif (temp_value != None):
                    if (temp_value <= min_value):
                        min_value = temp_value
                        move = i

        return (move, min_value)




def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0
    for i in range(simulations):

        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations

def toString():
    """tests"""
    game = Game([['-' for i in range(8)] for j in range(8)])
    print(game.possible_moves())
    game.neighbor(3,'R')
    game.neighbor(4, 'R')
    game.neighbor(5, 'R')



    print(game.winning_state())
    game.display()
    print(game.utility())
    maxplayer = MinimaxAgent('R')
    m = maxplayer.move(game)
    game = game.neighbor(m, maxplayer.color)
    game.display()
    print(game.winning_state())


def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = MinimaxAgent('R')
    minplayer = RandomAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game

if __name__ == '__main__':
    #toString()
    single_game(io=True)
    #tournament(simulations=50)
