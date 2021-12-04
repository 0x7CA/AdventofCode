from py.helper import input_as_list_of_int_grids

""" Advent of Code Day 4
Part 1:
Manage N Bingo Boards and mark drawn values on them until a sheet has bingo, then calculate sum of unmarked values
Part 2:
Same as part 1, but continue game until the last bingo board has won, and calculate score of that last winner

Special considerations: 
    Lookup table is used to find the corresponding grid position to a value quickly
    Bingo is checked by keeping a marked-values tally per row and column
    Sum of unmarked values is retrieved by using marked values as a boolean mask
    Last winner is retrieved by eliminating winning boards from the drawing game
"""


class Board:
    def __init__(self, grid: [[int]]):
        self.grid = grid
        self.last_value = None
        self.lookup_table = {}

        self.n_rows = len(self.grid)
        self.n_columns = len(self.grid[0])
        self.n_checked_row = [0] * self.n_rows
        self.n_checked_col = [0] * self.n_columns
        self.marked = self._init_empty_grid()

        self._populate_lookup()

    def _populate_lookup(self):
        for row_idx, row in enumerate(self.grid):
            for col_idx, val in enumerate(row):
                self.lookup_table[val] = (row_idx, col_idx)

    def _init_empty_grid(self):
        return [[0 for _ in range(self.n_columns)] for _ in range(self.n_rows)]

    def _get_value_pos(self, val: int) -> (int, int):
        if val not in self.lookup_table:
            return None, None
        return self.lookup_table[val]

    def _get_column(self, col_idx: int) -> [int]:
        return [x[col_idx] for x in self.grid]

    def _get_row(self, row_idx: int) -> [int]:
        return self.grid[row_idx]

    def mark_value(self, val: int):
        row, col = self._get_value_pos(val)
        if row is None:
            return
        self.marked[row][col] = 1
        # Keep track of the row and col we marked so we can check for bingo quickly
        self.n_checked_row[row] += 1
        self.n_checked_col[col] += 1
        self.last_value = val
        return self.check_bingo()

    def check_bingo(self) -> bool:
        return (self.n_columns in self.n_checked_row) | (self.n_rows in self.n_checked_col)

    def calculate_unmarked_sum(self) -> int:
        unmarked_values = self._init_empty_grid()
        # Invert marked values and use as mask to get all unmarked values
        for row in range(self.n_rows):
            for col in range(self.n_columns):
                unmarked_values[row][col] += self.grid[row][col] * abs(1 - self.marked[row][col])
        return sum([sum(x) for x in unmarked_values])


def calculate_final_score(boards: [Board], drawings: [int], last=False) -> int:
    if last:
        winning_board = calculate_last_winner(boards, drawings)
    else:
        winning_board = calculate_winner(boards, drawings)
    return winning_board.calculate_unmarked_sum() * winning_board.last_value


def calculate_winner(boards: [Board], drawings: [int]) -> Board:
    for drawing in drawings:
        for board in boards:
            if board.mark_value(drawing):
                return board


def calculate_last_winner(boards: [Board], drawings: [int]) -> Board:
    won_boards = {}
    last_winning_board = None
    for drawing in drawings:
        for board in boards:
            if board in won_boards:
                continue
            if board.mark_value(drawing):
                won_boards[board] = 1
                last_winning_board = board
    return last_winning_board


if __name__ == "__main__":
    boards, drawings = input_as_list_of_int_grids("input.txt", 5)
    boards = [Board(x) for x in boards]
    print(calculate_final_score(boards, drawings))
    # Reset state for part 2
    boards, drawings = input_as_list_of_int_grids("input.txt", 5)
    boards = [Board(x) for x in boards]
    print(calculate_final_score(boards, drawings, last=True))
