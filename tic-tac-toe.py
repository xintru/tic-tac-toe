import numpy as np
import math


class TicTacToeGame:
    field = []
    game_result = "Game not finished"
    next_turn = "X"

    def __init__(self, side):
        self.field = np.full((side, side), '_').tolist()

    def check_if_game_not_finished(self):
        is_finished = True
        for row in self.field:
            if row.count("_") > 0:
                is_finished = False
        if is_finished:
            self.game_result = "Draw"

    def linear_win(self, matrix):
        for row in matrix:
            if row.count("X") == len(self.field):
                if self.game_result != "Game not finished" and self.game_result != "Draw":
                    self.game_result = "Impossible"
                    break
                self.game_result = "X wins"
            elif row.count("O") == len(self.field):
                if self.game_result != "Game not finished" and self.game_result != "Draw":
                    self.game_result = "Impossible"
                    break
                self.game_result = "O wins"

    def flip_matrix(self):
        columns = []
        for column in range(len(self.field)):
            columns.append(np.array(self.field)[:, column].tolist())
        return columns

    def diagonal_win(self):
        main_diagonal = np.array(self.field).diagonal().tolist()
        alt_diagonal = np.flipud(self.field).diagonal().tolist()
        self.linear_win([main_diagonal, alt_diagonal])

    def row_win(self):
        self.linear_win(self.field)

    def column_win(self):
        self.linear_win(self.flip_matrix())

    def check_turns(self):
        x_count = 0
        o_count = 0
        for row in self.field:
            x_count += row.count("X")
            o_count += row.count("O")
        if abs(x_count - o_count) > 1:
            self.game_result = "Impossible"
        if x_count == o_count:
            self.next_turn = "X"
        elif x_count - o_count == 1:
            self.next_turn = "O"

    def check_result(self):
        self.check_if_game_not_finished()
        self.row_win()
        self.column_win()
        self.diagonal_win()
        self.check_turns()

    def get_result(self):
        return self.game_result

    def print_field(self):
        print("---------")
        for row in self.field:
            print(f"| {' '.join(row)} |")
        print("---------")

    def make_turn(self, x_axis_coord, y_axis_coord):
        if not x_axis_coord.isdigit() or not y_axis_coord.isdigit():
            print("You should enter numbers!")
            return False
        x_axis_coord = int(x_axis_coord)
        y_axis_coord = int(y_axis_coord)
        if x_axis_coord > len(self.field) or y_axis_coord > len(self.field):
            print(f"Coordinates should be from 1 to {str(len(self.field))}!")
            return False
        x_index = len(self.field) - y_axis_coord
        y_index = x_axis_coord - 1
        if self.field[x_index][y_index] == "_":
            self.field[x_index][y_index] = self.next_turn
            self.check_result()
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False


game = TicTacToeGame(3)
while game.game_result == 'Game not finished':
    game.print_field()
    x_axis, y_axis = input("Enter the coordinates: ").split()
    game.make_turn(x_axis, y_axis)
    if game.get_result() != 'Game not finished':
        game.print_field()
        print(game.get_result())
        break
