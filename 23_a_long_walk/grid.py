class Grid:
    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0]) if self.height > 0 else 0

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            lines = [line.strip() for line in f]
            rows = [list(line) for line in lines if line]
            return cls(rows)

    def get_cell(self, x, y):
        return self.rows[y][x]

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_adjacent_positions(self, x, y):
        positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        positions = [position for position in positions if self.is_in_bounds(position[0], position[1])]
        return positions
