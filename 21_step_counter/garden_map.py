type Pos = tuple[int, int]


class GardenMap:
    START_CHAR = 'S'
    PASSABLE_CHAR = '.'
    IMPASSABLE_CHAR = '#'

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(self.rows)
        self.width = len(self.rows[0]) if self.height > 0 else 0
        self.start_pos = self.find_start_pos()

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            lines = [line.strip() for line in f]
            rows = [list(line) for line in lines if line]
            return cls(rows)

    def find_start_pos(self) -> Pos:
        for y in range(self.height):
            for x in range(self.width):
                if self.get_char(x, y) == self.START_CHAR:
                    return x, y
        assert False

    def get_char(self, x, y):
        return self.rows[y][x]

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_pos_passable(self, x, y):
        return self.is_in_bounds(x, y) and self.get_char(x, y) != self.IMPASSABLE_CHAR
