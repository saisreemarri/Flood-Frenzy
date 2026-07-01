import random
import copy

from floodFill import initialize_owned, flood_fill, is_game_won

COLORS = 5


def generate_board(size=11):
    board = []

    for i in range(size):
        row = []

        for j in range(size):
            row.append(random.randint(0, COLORS - 1))

        board.append(row)

    return board


class Game:

    def __init__(self, size=11):

        self.board = generate_board(size)
        self.owned = initialize_owned(self.board)
        self.moves = 0

        # Stacks for Undo
        self.undo_stack = []

    # ----------------------------
    # Save current state
    # ----------------------------
    def save_state(self):

        self.undo_stack.append({

            "board": copy.deepcopy(self.board),

            "owned": copy.deepcopy(self.owned),

            "moves": self.moves

        })

    # ----------------------------
    # Make Move
    # ----------------------------
    def make_move(self, color):

        current_color = self.board[0][0]

        # Ignore same color
        if color == current_color:

            return {
                "board": self.board,
                "moves": self.moves,
                "won": is_game_won(self.board, self.owned),
                "owned": list(self.owned)
            }

        # Save current state before move
        self.save_state()


        self.board, self.owned = flood_fill(
            self.board,
            self.owned,
            color
        )

        self.moves += 1

        return {
            "board": self.board,
            "moves": self.moves,
            "won": is_game_won(self.board, self.owned),
            "owned": list(self.owned)
        }

    # ----------------------------
    # Undo
    # ----------------------------
    def undo(self):

        if not self.undo_stack:

            return {
                "board": self.board,
                "moves": self.moves,
                "won": is_game_won(self.board, self.owned),
                "owned": list(self.owned)
            }

        previous = self.undo_stack.pop()

        self.board = previous["board"]
        self.owned = previous["owned"]
        self.moves = previous["moves"]

        return {
            "board": self.board,
            "moves": self.moves,
            "won": is_game_won(self.board, self.owned),
            "owned": list(self.owned)
        }
