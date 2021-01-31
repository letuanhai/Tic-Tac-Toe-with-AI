import random


def find_position(coordinate):
    return 3 * (coordinate[0] - 1) + coordinate[1] - 1


class Board:
    def __init__(self, player_x, player_o):
        self.current_pos = "_" * 9
        self.current_player = "X"
        self.player_x = self.user_move if player_x == "user" else self.auto_move
        self.player_o = self.user_move if player_o == "user" else self.auto_move
        self.print_board()

    def print_board(self):
        print("---------")
        print("|", " ".join(self.current_pos[:3]), "|", sep=" ")
        print("|", " ".join(self.current_pos[3:6]), "|", sep=" ")
        print("|", " ".join(self.current_pos[6:]), "|", sep=" ")
        print("---------")

    def winning_pos(self):
        cells = [
            self.current_pos[0] + self.current_pos[1] + self.current_pos[2],
            self.current_pos[0] + self.current_pos[3] + self.current_pos[6],
            self.current_pos[0] + self.current_pos[4] + self.current_pos[8],
            self.current_pos[2] + self.current_pos[4] + self.current_pos[6],
            self.current_pos[2] + self.current_pos[4] + self.current_pos[6],
            self.current_pos[2] + self.current_pos[5] + self.current_pos[8],
            self.current_pos[6] + self.current_pos[7] + self.current_pos[8],
            self.current_pos[1] + self.current_pos[4] + self.current_pos[7],
            self.current_pos[3] + self.current_pos[4] + self.current_pos[5],
        ]
        return cells

    def game_result(self):
        """If the game is finished, return the result, else return Game not finished"""

        # Make an array of possible winning positions
        winning_pos = self.winning_pos()

        empty_cell = "_" in self.current_pos
        # count_x = self.current_board.count("X")
        # count_o = self.current_board.count("O")

        if "XXX" in winning_pos and "OOO" in winning_pos:
            # or abs(count_x - count_o) > 1:
            return "Impossible"
        elif "OOO" in winning_pos:
            return "O wins"
        elif "XXX" in winning_pos:
            return "X wins"
        elif empty_cell:
            return "Game not finished"
        else:
            return "Draw"

    def is_valid_move(self, move):
        coordinate = move.split()
        if not move.replace(" ", "").isnumeric():
            print("You should enter numbers!")
            return False
        n = [int(i) for i in coordinate]
        for i in n:
            if i < 1 or i > 3:
                print("Coordinates should be from 1 to 3!")
                return False
        if self.current_pos[find_position(n)] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def random_move(self):
        empty_cells = [i for i, cell in enumerate(self.current_pos) if cell == "_"]
        move = random.choice(empty_cells)
        cells = list(self.current_pos)
        cells[move] = self.current_player
        self.current_pos = "".join(cells)
        self.print_board()

    def winning_move(self):
        winning_pos = self.winning_pos()
        possible_win = [s.replace('X', self.current_player) for s in ['XX_','_XX','X_X']]
        pass

    def auto_move(self):
        print('Making move level "easy"')
        self.random_move()

    def user_move(self):
        while True:
            next_move = input("Enter the coordinates: ")
            if self.is_valid_move(next_move):
                break
        moves = [int(i) for i in next_move.split()]
        cells = list(self.current_pos)
        cells[find_position(moves)] = self.current_player
        self.current_pos = "".join(cells)
        self.print_board()

    def make_move(self):
        if self.current_player == "X":
            self.player_x()
        else:
            self.player_o()
        self.current_player = "X" if self.current_player == "O" else "O"


def start(x_player, o_player):
    new_game = Board(x_player, o_player)
    while new_game.game_result() == "Game not finished":
        new_game.make_move()
    print(new_game.game_result())


while True:
    commands = input("Input command: ").split()
    if commands[0] == "exit" and len(commands) == 1:
        break
    elif (
        commands[0] == "start"
        and len(commands) == 3
        and set(commands[1:]).issubset({"user", "easy"})
    ):
        start(*commands[1:])
    else:
        print("Bad parameters!")
