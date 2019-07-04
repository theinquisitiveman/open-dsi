class Board():
    """
    This class defines elements of the board during the Tic Tac Toe game.

    Args:
        board_size:integer
        board:list
    """

    def __init__(self, board_size = 9, board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]):
        self.board_size = board_size
        self.board = board

    def coordinate_check(self, position):
        """
        Docstring: This function will check to see if the coordinate provided is free.

        Args:
        position:integer
        """
        self.position = position
        for position in board:
            if [position] == "_":
                return True
            else:
                return False

    def mark_square(self):
        if coordinate_check(board) == True:
            [i] == 'X'
        else:
            pass

#    def check_winner(self, player):
#        for range in range(len(board))

    def display_board(self, board):
        for row in range(board):
            print(row)

#    display_board(board)


class Player():
    """
    This class will build the players of the game and give them the right attributes.

    Args:
        name: string
        indicator: string
    """

    def __init(self, name, indicator):
        self.name = user_input("What's your name?: ")
        self.indicator = indicator

class Game():
    """
    This class defines the rules of the game that will be played.

    Args:

    """
    def __init__(self, board, player):
        player_1 = 'X'
        player_2 = 'O'
        self.board = Board
        self.players = (player_1, player_2)
        pass

"""
Test Data

Test Players >>
Samuel = Player('Samuel', 'X')
Nicky = Player('Nicky', 'O')
Robert = Player('Robert', 'X')
Monir = Player('Monir', 'O')

Test Game >>


Test Board >>

"""
