

class Game:

    def __init__(self, dim, n_player, board=None):
        if board:
            self.board = board
        else:
            self.board = [[None]*dim for i in range(dim)]
        self.current_player = 0
        self.dimension = dim
        self.n_player = n_player

    def in_bounds(self, row, col):
        """Returns True if row and column are within the board"""
        return 0<=row<self.dimension and 0<=col<self.dimension

    def place_stone_as(self, row, col, player):
        """Places a stone on row and column as a player. Automatically clears
        all groups that are killed by the newly placed stone. If placing the
        stone would be a suicide a ValueError is raised.
        """
        if not self.in_bounds(row, col):
            raise ValueError("Stone is outside of the board")
        if self.board[row][col] is not None:
            raise ValueError("There is already a stone in this location")

        self.board[row][col]=player
        if self.is_group_dead(row, col):
            suicide=True
            for i in self.neighbours(row, col):
                if self.board[i[0]][i[1]] != player and self.is_group_dead(*i):
                    suicide=False
            if suicide:
                self.board[row][col]=None
                raise ValueError("A player can't commit suicide")

        to_clear = []
        for i in self.neighbours(row, col):
            if self.is_group_dead(*i):
                to_clear.append(i)
        for i in to_clear:
            self.clear_group(*i)

    def play_stone(self, row, col):
        """Shortcut for placing a stone as current_player and changing the
        current_player to the player who moves next
        """
        self.place_stone_as(row, col, self.current_player)
        self.current_player=(self.current_player+1)%self.n_player;

    def neighbours(self, row, col):
        """Iterator over all the neighbouring stones to stone at row, col."""
        if not self.in_bounds(row, col):
            raise ValueError("Position is outside of the board")
        dx = (-1, 0, 0, 1)
        dy = (0, -1, 1, 0)
        for i, j in zip(dx, dy):
            if self.in_bounds(row + i, col + j):
                yield (row + i, col + j)


    def group(self, row, col):
        """Iterator over all the stones that belong to the same group as the
        stone at (row, col), yields tuples of coordinates (row, col)
        """
        if not self.in_bounds(row, col):
            raise ValueError("Position is outside of the board")
        visited = set()
        to_visit = [(row, col)]
        while len(to_visit)>0:
            c = to_visit.pop()
            visited.add(c)
            yield c
            for i in self.neighbours(row, col):
                if i not in visited and self.board[i[0]][i[1]]==self.board[row][col]:
                    to_visit.append(i)

    def clear_group(self, row, col):
        """Removes a group from the board replacing it with empty spaces"""
        for i in self.group(row, col):
            self.board[i[0]][i[1]]=None

    def is_group_dead(self, row, col):
        """Returns True if group at row, col is dead i.e. it doesn't have any
        free spaces around itself"""
        if not self.in_bounds(row, col):
            raise ValueError("Position is outside of the board")
        if self.board[row][col] is None:
            return False

        for i in self.group(row, col):
            for j in self.neighbours(*i):
                if self.board[j[0]][j[1]] is None:
                    return False
        return True

    def __str__(self):
        r = "A {0}x{0} game with {1} players. Player {2} plays next \n".format(
                            self.dimension, self.n_player, self.current_player)
        for i in self.board:
            for j in i:
                if j is None:
                    r+='.'
                else:
                    r+=chr(ord('0')+j)
            r+='\n'
        return r
