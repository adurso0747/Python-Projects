import copy
import time
from queue import PriorityQueue

class Puzzle():
    """A sliding-block puzzle."""

    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid) # No aliasing!

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print (number, end="")
            print()
        print()

    #Allow priority queue to compare puzzle objects
    def __lt__(self, other):
        return id(self) < id(other)

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN
        moves = []
        puzzle = Puzzle(self.grid)
        locationTuple = puzzle.locate(' ')

        if((locationTuple[0]+1) in range (3)):

            if(self.grid[locationTuple[0] +1][locationTuple[1]] != None):
                {
                    moves.append("S")
                }

        if((locationTuple[0]-1) in range (3)):

            if(self.grid[locationTuple[0] -1][locationTuple[1]] != None):
                {
                    moves.append("N")
                }

        if ((locationTuple[1] + 1) in range (3)):

            if (self.grid[locationTuple[0]][locationTuple[1]+1] != None):

                {
                    moves.append("E")
                }

        if ((locationTuple[1] -1) in range (3)):

            if (self.grid[locationTuple[0]][locationTuple[1] - 1] != None):
                {
                    moves.append("W")
                }

        return moves;


    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        # YOU FILL THIS IN

        puzzle = Puzzle(self.grid)
        locationTuple = puzzle.locate(' ')

        if(move == "N"):
            tempLocation = self.grid[locationTuple[0] -1][locationTuple[1]]
            self.grid[locationTuple[0] - 1][locationTuple[1]] = " "
            self.grid[locationTuple[0]][locationTuple[1]] = tempLocation

        if (move == "S"):
            tempLocation = self.grid[locationTuple[0] + 1][locationTuple[1]]
            self.grid[locationTuple[0] + 1][locationTuple[1]] = " "
            self.grid[locationTuple[0]][locationTuple[1]] = tempLocation

        if (move == "E"):
            tempLocation = self.grid[locationTuple[0]][locationTuple[1] + 1]
            self.grid[locationTuple[0]][locationTuple[1] + 1] = " "
            self.grid[locationTuple[0]][locationTuple[1]] = tempLocation

        if(move == "W"):
            tempLocation = self.grid[locationTuple[0]][locationTuple[1] - 1]
            self.grid[locationTuple[0]][locationTuple[1] - 1] = " "
            self.grid[locationTuple[0]][locationTuple[1]] = tempLocation

        puzzle = Puzzle(self.grid)
        return puzzle

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
        distance = 0

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                number = self.grid[r][c]
                if (number != ' '):
                    (gr,gc) = goal.locate(number)
                    distance += abs(r-gr) + abs(c - gc)
        return distance


    def locate(self, value):
        """Finds location of a number in grid"""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == value:
                    return (r,c)



class Agent():
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN
        # (fscore(g score, h score, maze, path)
        puzzle = Puzzle(puzzle.grid)
        finished = [puzzle]
        frontier = PriorityQueue()
        g_score = 0
        fscore = g_score + puzzle.h(goal)
        thisTuple = (fscore, g_score, puzzle.h(goal), puzzle, list())
        frontier.put(thisTuple)
        while frontier.empty() == False:
            parentTuple = frontier.get()
            parent = parentTuple[3]
            parentPuzzle = Puzzle(parent.grid)
            parentPath = parentTuple[4][:]
            if parent.grid == goal.grid:
                return parentTuple[4]
            else:
                finished.append(parent)

            for i in parentPuzzle.moves():
                childPuzzle = Puzzle(parentPuzzle.grid)
                childPuzzle.neighbor(i)
                child_tuple = parentTuple[:]
                newgscore = child_tuple[1] + 1
                newhscore = childPuzzle.h(goal)
                child_path = child_tuple[4][:]
                child_path.append(i)
                newfscore = child_tuple[1] + child_tuple[2]
                newTuple = (newfscore, newgscore, newhscore, childPuzzle, child_path)
                if newTuple not in frontier.queue and childPuzzle not in finished:
                    frontier.put(newTuple)



def toString():
    """tests"""
    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    print(puzzle.moves())
    puzzle.neighbor("N")
    puzzle.neighbor("W")
    puzzle.neighbor("W")
    print(puzzle.moves())
    puzzle.display()
    print (puzzle.h(goal))


def main():
    """Create a puzzle, solve it with A*, and console-animate."""
    #toString()

    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()

    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)

    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()

if __name__ == '__main__':
 main()