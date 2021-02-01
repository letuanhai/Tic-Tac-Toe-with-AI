import random


def find_position(coordinate):
    return 3 * (coordinate[0] - 1) + coordinate[1] - 1


class Board:
    # A list of possible winning cases
    winning_cases = (
        (0, 1, 2),
        (0, 3, 6),
        (0, 4, 8),
        (2, 4, 6),
        (2, 5, 8),
        (6, 7, 8),
        (1, 4, 7),
        (3, 4, 5),
    )

    def __init__(self, player_x, player_o):
        self.current_pos = ["_"] * 9
        self.current_player = "X"
        self.player_x = player_x
        self.player_o = player_o
        self.print_board()

    def print_board(self):
        print("---------")
        print("|", " ".join(self.current_pos[:3]), "|", sep=" ")
        print("|", " ".join(self.current_pos[3:6]), "|", sep=" ")
        print("|", " ".join(self.current_pos[6:]), "|", sep=" ")
        print("---------")

    def winning_pos(self):
        cases = dict()
        for case in Board.winning_cases:
            positions = "".join(self.current_pos[i] for i in case)
            cases[positions] = case
        return cases

    def game_result(self):
        """If the game is finished, return the result, else return Game not finished"""

        winning_pos = self.winning_pos()
        empty_cell = "_" in self.current_pos

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
        self.current_pos[move] = self.current_player

    def winning_move(self):
        winning_pos = self.winning_pos()
        possible_win = [
            s.replace("A", self.current_player) for s in ["AA_", "_AA", "A_A"]
        ]
        for case in possible_win:
            if case in winning_pos:
                positions = winning_pos[case]
                move = positions[case.index("_")]
                self.current_pos[move] = self.current_player
                return True
        return False

    def blocking_move(self):
        winning_pos = self.winning_pos()
        opponent = "X" if self.current_player == "O" else "X"
        possible_win = [s.replace("A", opponent) for s in ["AA_", "_AA", "A_A"]]
        for case in possible_win:
            if case in winning_pos:
                positions = winning_pos[case]
                move = positions[case.index("_")]
                self.current_pos[move] = self.current_player
                return True
        return False

    def auto_move(self, difficulty):
        level = difficulty.strip().lower()
        if level == "easy":
            print('Making move level "easy"')
            self.random_move()
        elif level == "medium":
            print('Making move level "medium"')
            if not self.winning_move():
                if not self.blocking_move():
                    self.random_move()

        self.print_board()

    def user_move(self):
        while True:
            next_move = input("Enter the coordinates: ")
            if self.is_valid_move(next_move):
                break
        moves = [int(i) for i in next_move.split()]
        self.current_pos[find_position(moves)] = self.current_player
        self.print_board()

    def make_move(self):
        if self.current_player == "X":
            if self.player_x == "user":
                self.user_move()
            else:
                self.auto_move(self.player_x)
        else:
            if self.player_o == "user":
                self.user_move()
            else:
                self.auto_move(self.player_o)
        self.current_player = "X" if self.current_player == "O" else "O"


def start(x_player, o_player):
    new_game = Board(x_player, o_player)
    while new_game.game_result() == "Game not finished":
        new_game.make_move()
    print(new_game.game_result())
    print()


while True:
    commands = input("Input command: ").split()
    if commands[0] == "exit" and len(commands) == 1:
        break
    elif (
        commands[0] == "start"
        and len(commands) == 3
        and set(commands[1:]).issubset({"user", "easy", "medium"})
    ):
        start(*commands[1:])
    else:
        print("Bad parameters!")
