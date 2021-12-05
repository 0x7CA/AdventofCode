class Grid:
    def __init__(self, rows: int, cols: int):
        self.n_rows = rows
        self.n_columns = cols
        self.grid = self._init_empty_grid()

        self.lookup_table = {}
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