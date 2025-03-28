class ChessPiece:
    """Represents a chess piece, and serves as a parent class for Bishop, Knight, Rook and King, all of which are used
    to initialize the RacingKings class. Each ChessPiece object has a color, square and set of controlled squares."""

    def __init__(self, color, square, controlled_squares):
        self._color = color    # can be either 'WHITE' or 'BLACK'
        self._square = square
        self._controlled_squares = controlled_squares

    def get_color(self):
        """Returns the color of a chess piece."""
        return self._color

    def get_controlled_squares(self):
        """Returns all squares currently controlled by the chess piece."""
        return self._controlled_squares

    def set_square(self, new_square):
        """Takes as an argument a square and sets it as the current square for a piece."""
        self._square = new_square

    def algebraic_to_tup(self, algebraic_square):
        """Takes as an argument a square in algebraic notation and returns a tuple of two integers: the ASCII value
        of the file and the rank number."""
        file = ord(algebraic_square[0]) - 96  # ord() converts a letter into an integer per the ASCII table
        rank = int(algebraic_square[1])
        return (file, rank)

    def tup_to_algebraic(self, square_tup):
        """Takes as an argument a tuple representing a square on a chess board and returns the corresponding algebraic
        notation."""
        file, rank = square_tup
        return chr(file + 96) + str(rank)
    
    def _check_direction(self, square_tup, direction, board):
        """Receives a tuple representing the current square of a long-range piece, a direction the piece can travel,
        and the current state of the board. Adds squares to the set of controlled squares until a friendly piece or
        edge of board is reached."""
        file, rank = square_tup
        delta_file, delta_rank = direction
        clear_path = True
        while clear_path:
            square = self.tup_to_algebraic((file + delta_file, rank + delta_rank))
            if square not in board:
                clear_path = False
            elif board[square] is None:
                self._controlled_squares.add(square)
                file += delta_file
                rank += delta_rank
            elif board[square].get_color() != self._color:
                self._controlled_squares.add(square)
                clear_path = False
            else:
                clear_path = False

class Bishop(ChessPiece):
    """Represents a bishop in a game of chess and used to create all Bishop objects when initializing RacingKings.
    Inherits from ChessPiece."""

    def set_controlled_squares(self, board):
        """Takes as an argument the current layout of the board and determines the set of controlled squares by a
        bishop."""
        self._controlled_squares.clear()
        square_tup = self.algebraic_to_tup(self._square)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            self._check_direction(square_tup, direction, board)


class Knight(ChessPiece):
    """Represents a knight in a game of chess and used to create all Knight objects when initializing RacingKings.
    Inherits from ChessPiece."""

    def set_controlled_squares(self, board):
        """Takes as an argument the current layout of the board and determines the set of controlled squares by a
        knight."""
        self._controlled_squares.clear()

        # Extract integer values of column and rank from the algebraic notation.
        square_tup = self.algebraic_to_tup(self._square)
        file, rank = square_tup

        # Generate tuples representing the squares that need to be checked, then convert each into algebraic notation.
        tup_to_check = [(file + 2, rank + 1), (file + 2, rank - 1), (file - 2, rank + 1),
                        (file - 2, rank - 1), (file + 1, rank + 2), (file + 1, rank - 2),
                        (file - 1, rank + 2), (file - 1, rank - 2)]
        square_to_check = [self.tup_to_algebraic(tup) for tup in tup_to_check]

        for square in square_to_check:
            if square not in board:
                pass
            elif board[square] is not None and self._color == board[square].get_color():
                pass
            else:
                self._controlled_squares.add(square)


class Rook(ChessPiece):
    """Represents a rook in a game of chess and used to create all Rook objects when initializing RacingKings. Inherits
     from ChessPiece."""

    def set_controlled_squares(self, board):
        """Takes as an argument the current layout of the board and determines the set of controlled squares by a rook.
        """
        self._controlled_squares.clear()
        square_tup = self.algebraic_to_tup(self._square)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for direction in directions:
            self._check_direction(square_tup, direction, board)


class King(ChessPiece):
    """Represents a king in a game of chess and used to create all King objects when initializing RacingKings. Inherits
     from ChessPiece."""

    def set_controlled_squares(self, board):
        """Takes as an argument the current layout of the board and determines the set of controlled squares by a king.
        """
        self._controlled_squares.clear()

        # Extract integer values of column and rank from the algebraic notation.
        square_tup = self.algebraic_to_tup(self._square)
        file, rank = square_tup

        # Generate tuples representing the squares that need to be checked, then convert each into algebraic notation.
        tup_to_check = [(file + 1, rank + 1), (file + 1, rank), (file + 1, rank - 1), (file, rank - 1),
                        (file - 1, rank - 1), (file - 1, rank), (file - 1, rank + 1), (file, rank + 1)]
        square_to_check = [self.tup_to_algebraic(tup) for tup in tup_to_check]

        for square in square_to_check:
            if square not in board:
                pass
            elif board[square] is not None and self._color == board[square].get_color():
                pass
            else:
                self._controlled_squares.add(square)


class RacingKings:
    """Represents a game of Racing Kings, a variant of chess."""

    def __init__(self):
        self._theme = self.select_theme()
        self._game_state = 'UNFINISHED'
        self._turn = 'WHITE'

        # Initialize white's pieces.
        a1_king = King('WHITE', 'a1', set())
        a2_rook = Rook('WHITE', 'a2', {'a3', 'a4', 'a5', 'a6', 'a7', 'a8'})
        b1_bishop = Bishop('WHITE', 'b1', set())
        b2_bishop = Bishop('WHITE', 'b2', {'a3', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'})
        c1_knight = Knight('WHITE', 'c1', {'b3', 'd3', 'e2'})
        c2_knight = Knight('WHITE', 'c2', {'a3', 'b4', 'd4', 'e3', 'e1'})

        # Initialize black's pieces.
        h1_king = King('BLACK', 'h1', set())
        h2_rook = Rook('BLACK', 'h2', {'h3', 'h4', 'h5', 'h6', 'h7', 'h8'})
        g1_bishop = Bishop('BLACK', 'g1', set())
        g2_bishop = Bishop('BLACK', 'g2', {'h3', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8'})
        f1_knight = Knight('BLACK', 'f1', {'g3', 'e3', 'd2'})
        f2_knight = Knight('BLACK', 'f2', {'h3', 'g4', 'e4', 'd3', 'd1'})

        self._board = {
            'a8': None, 'b8': None, 'c8': None, 'd8': None, 'e8': None, 'f8': None, 'g8': None, 'h8': None,
            'a7': None, 'b7': None, 'c7': None, 'd7': None, 'e7': None, 'f7': None, 'g7': None, 'h7': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            # 2nd rank
            'a2': a2_rook, 'b2': b2_bishop, 'c2': c2_knight, 'd2': None,
            'e2': None, 'f2': f2_knight, 'g2': g2_bishop, 'h2': h2_rook,
            # 1st rank
            'a1': a1_king, 'b1': b1_bishop, 'c1': c1_knight, 'd1': None,
            'e1': None, 'f1': f1_knight, 'g1': g1_bishop, 'h1': h1_king
        }

        self._remaining_pieces = [a1_king, a2_rook, b1_bishop, b2_bishop, c1_knight, c2_knight, f1_knight, f2_knight,
                                  g1_bishop, g2_bishop, h1_king, h2_rook]
        self._white_king_position = 'a1'
        self._black_king_position = 'h1'

    def select_theme(self):
        """Prompts the user for the theme of their terminal, dark or light, to ensure pieces display with the correct
        colors."""
        theme = input('Select your terminal theme (dark/light): ').lower()
        while theme not in ['dark', 'light']:
            theme = input('Select your terminal theme (dark/light): ').lower()

        return theme

    def set_white_king_position(self, new_square):
        """Takes as an argument a new_square for the white king and sets it as the king's current position."""
        self._white_king_position = new_square

    def set_black_king_position(self, new_square):
        """Takes as an argument a new_square for the black king and sets it as the king's current position."""
        self._black_king_position = new_square

    def update_king_position(self, piece, new_square):
        """Takes as an argument a piece and square and, if the piece is of the King class, updates the corresponding
        king_position data member."""
        if isinstance(piece, King):
            if piece.get_color() == "WHITE":
                self.set_white_king_position(new_square)
            else:
                self.set_black_king_position(new_square)

    def update_controlled_squares(self):
        """Updates the controlled squares for all remaining pieces on the board."""
        for piece in self._remaining_pieces:
            piece.set_controlled_squares(self._board)

    def is_check(self):
        """Returns True if either king is within the controlled squares of a piece, but returns False otherwise."""
        for piece in self._remaining_pieces:
            controlled_squares = piece.get_controlled_squares()
            if self._white_king_position in controlled_squares or self._black_king_position in controlled_squares:
                return True
        return False

    def change_turn(self):
        """Switches the player to move by providing an argument for set_turn."""
        if self._turn == 'WHITE':
            self._turn = ('BLACK')
        else:
            self._turn = ('WHITE')

    def update_game_state(self):
        """Checks the current position of the kings and the turn to determine if the game is over."""
        # If both kings are on the 8th rank, the game is a tie.
        if self._white_king_position[1] == '8' and self._black_king_position[1] == '8':
            self._game_state = ('TIE')
        # If black's king is on the 8th rank but white's is not, black has won the game.
        elif self._black_king_position[1] == '8' and not self._white_king_position[1] == '8':
            self._game_state = ('BLACK_WON')
        # If white's king is on the 8th rank and white is to move again, white has won the game.
        elif self._white_king_position[1] == '8' and self._turn == 'WHITE':
            self._game_state = ('WHITE_WON')
        else:
            self._game_state = ('UNFINISHED')

    def print_board(self):
        """Prints the current position of the game."""
        list_of_ranks = []
        single_rank = []
        square_count = 0

        # Generates a list of lists of the contents (either None or a ChessPiece subclass object) of each square. Each
        # of the 8 inner lists will have 8 elements, corresponding to the 8 squares in a rank.
        for square in self._board:
            if square_count == 0:
                single_rank.append(self._board[square])
                square_count += 1
            elif square_count % 8 != 0:
                single_rank.append(self._board[square])
                square_count += 1
                if square_count == 64:
                    list_copy = list(single_rank)
                    list_of_ranks.append(list_copy)
            elif square_count % 8 == 0:
                list_copy = list(single_rank)
                list_of_ranks.append(list_copy)
                single_rank.clear()
                single_rank.append(self._board[square])
                square_count += 1

        for num, rank in enumerate(list_of_ranks, -8):  # Starts at -8 to print the rank numbers in descending order.
            print(abs(num), end="")
            print(' ', end="")
            for square in rank:
                if square is None:
                    print('\u2610', end=" ")
                else:
                    print(self._get_unicode(square), end=" ")
            print('\n')
        print('  a b c d e f g h')  # Prints the file names at the bottom of the board.

    def _get_unicode(self, piece):
        """Receives a piece and returns the unicode representation based on piece color and terminal theme."""            
        matched = (piece.get_color() == "WHITE" and self._theme == 'light') or (piece.get_color() == "BLACK" and self._theme == 'dark')
        if isinstance(piece, Bishop):
            unicode = '\u2657' if matched else '\u265D'
        if isinstance(piece, Knight):
            unicode = '\u2658' if matched else '\u265E'
        if isinstance(piece, Rook):
            unicode = '\u2656' if matched else '\u265C'
        if isinstance(piece, King):
            unicode = '\u2654' if matched else '\u265A'
        return unicode

    def make_move(self, start_square, end_square):
        """Takes as arguments the starting and ending squares of a move, and, assuming the move is legal, makes the
        indicated move and returns True. If the move is illegal or the game has already concluded, return False."""
        # If the starting or ending squares do not exist, return False.
        if start_square not in self._board or end_square not in self._board:
            return False

        # If there is no piece on the start_square or the piece is the wrong color, return False.
        if self._board[start_square] is None or self._turn != self._board[start_square].get_color():
            return False

        # If the piece on start_square cannot move to end_square, return False.
        if end_square not in self._board[start_square].get_controlled_squares():
            return False

        # If the game is already over, return False.
        if self._game_state != 'UNFINISHED':
            return False

        # Move the piece from start_square to end_square, remove any captured piece, update the controlled squares for
        # all pieces, and update the king positions as needed.
        piece_to_move = self._board[start_square]
        end_square_contents = self._board[end_square]
        self._board[start_square] = None
        self._board[end_square] = piece_to_move
        if end_square_contents is not None:
            self._remaining_pieces.remove(end_square_contents)
        piece_to_move.set_square(end_square)
        self.update_controlled_squares()
        self.update_king_position(piece_to_move, end_square)

        # If the move puts either of the kings in check, put the piece back on start_square, return any captured piece,
        # re-update the controlled squares for all pieces, update king positions as needed, and return False.
        if self.is_check():
            piece_to_return = self._board[end_square]
            self._board[end_square] = end_square_contents
            if end_square_contents is not None:
                self._remaining_pieces.append(end_square_contents)
            self._board[start_square] = piece_to_return
            piece_to_return.set_square(start_square)
            self.update_controlled_squares()
            self.update_king_position(piece_to_return, start_square)
            return False

        # If the move does not place either king in check, switch the side to move, make necessary updates to the game
        # state, print the current position, and return True.
        self.change_turn()
        self.update_game_state()
        self.print_board()
        return True
        
    def _new_game(self):
        """After the conclusion of a game, prompts the user if they'd like to play another."""
        new_game = input('Would you like to play another game? (y/n) ').lower()

        while new_game not in ['y', 'n']:
            new_game = input('Would you like to play another game? (y/n) ')

        if new_game == 'y':
            main()
        else:
            print('Thanks for playing!')
        
    def run(self):
        """Starts the Racing Kings game."""
        print("Welcome to Racing Kings!\n")
        self.print_board()
        while self._game_state == 'UNFINISHED':
            print('\nWhite to move.') if self._turn == 'WHITE' else print('\nBlack to move.')
            legal = self.make_move(input('Enter start square of move: '), input('Enter end square of move: '))
            if not legal:
                print('\nIllegal move! Please make a different move.')
        print(self._game_state)
        self._new_game()


def main():
    game = RacingKings()
    game.run()


if __name__ == "__main__":
    main()
