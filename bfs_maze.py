import time
import queue

class Maze():
    """A pathfinding problem."""
    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('*', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        moves = []
        (r,c) = self.location
        if self.grid[r][c - 1] != 'X':
            moves.append('N')
        if self.grid[r][c + 1] != 'X':
            moves.append('S')
        if self.grid[r+1][c] != 'X':
            moves.append('E')
        if self.grid[r][c - 1] != 'X':
            moves.append('W')

        return moves


    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        (r,c) = self.location
        if move == "N":
            maze = Maze(self.grid, (r, c-1))
            return maze
        elif move == "S":
            maze = Maze(self.grid, (r, c+1))
            return
        elif move == "E":
            maze = Maze(self.grid, (r+1, c))
            return maze
        else:
            maze = Maze(self.grid, (r-1, c))
            return maze



class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        frontier = queue.Queue()
        frontier.put(maze.location)
        movesList = []
        reverseMovesList = []

        while frontier.empty() == False:
            parent = frontier.get(0)
            child_maze = Maze(maze.grid, parent)
            for i in child_maze.moves():
                child = child_maze.neighbor(i)
                frontier.put(child_maze.neighbor(i).location)
                movesList.append(i)
                if child_maze.location == goal.location:
                    for j in movesList[::-1]:
                        reverseMovesList.append(j)
                    return reverseMovesList



def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()