type GridPos = tuple[int, int]


class PipeGrid:
    START_CHAR = 'S'

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.width = len(rows[0])
        self.height = len(rows)
        self.start_pos = self.find_char(self.START_CHAR)

    def find_char(self, search_char: str) -> GridPos:
        for y in range(self.height):
            for x in range(self.width):
                if self.get_char((x, y)) == search_char:
                    return x, y
        return -1, -1

    def get_char(self, pos: GridPos) -> str:
        return self.rows[pos[1]][pos[0]]

    def is_pos_in_grid(self, pos: GridPos) -> bool:
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    @classmethod
    def from_file(cls, file_name):
        with open(file_name) as f:
            rows = [list(line.strip()) for line in f]
            rows = [row for row in rows if len(row) > 0]
            return cls(rows)
