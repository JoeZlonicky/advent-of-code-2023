from functools import lru_cache


class Grid:
    EMPTY_CHAR = '.'
    RIGHTWARD_MIRROR_CHAR = '/'
    LEFTWARD_MIRROR_CHAR = '\\'
    MIRROR_CHARS = [LEFTWARD_MIRROR_CHAR, RIGHTWARD_MIRROR_CHAR]
    H_SPLITTER_CHAR = '-'
    V_SPLITTER_CHAR = '|'
    SPLITTER_CHARS = [H_SPLITTER_CHAR, V_SPLITTER_CHAR]

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(self.rows)
        self.width = len(self.rows[0]) if self.height else 0

    def highest_energized_from_entering_edge(self):
        highest = 0
        for x in range(1, self.width - 1):
            highest = max(highest, self.count_energized((x, 0), (0, 1)))
            highest = max(highest, self.count_energized((x, self.height - 1), (0, -1)))
        for y in range(self.height):
            highest = max(highest, self.count_energized((0, y), (1, 0)))
            highest = max(highest, self.count_energized((self.width - 1, y), (-1, 0)))
        return highest

    def count_energized(self, start_pos: tuple[int, int], start_direction: tuple[int, int]):
        history: dict[tuple, int] = {}
        stack = [(start_pos, start_direction)]

        while stack:
            current = stack.pop()

            history[current] = history.get(current, 0) + 1
            pos, direction = current
            next_beams = self.get_next_beams(pos, direction)

            for beam in next_beams:
                if beam in history:
                    continue
                stack.append(beam)

        positions = set([beam[0] for beam in history.keys()])

        return len(positions)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            lines = [line.strip() for line in f]
            rows = [list(line) for line in lines if line]
            return cls(rows)

    @lru_cache(maxsize=None)
    def get_next_beams(self, pos, direction):
        next_directions = []

        char = self.get_char(pos[0], pos[1])
        if char == self.EMPTY_CHAR or (char == self.H_SPLITTER_CHAR and direction[1] == 0) or (
                char == self.V_SPLITTER_CHAR and direction[0] == 0):
            next_directions = [direction]

        elif char == self.H_SPLITTER_CHAR:
            next_directions = [(-1, 0), (1, 0)]

        elif char == self.V_SPLITTER_CHAR:
            next_directions = [(0, -1), (0, 1)]

        elif char == self.RIGHTWARD_MIRROR_CHAR:
            next_directions = [(-1 * direction[1], -1 * direction[0])]

        elif char == self.LEFTWARD_MIRROR_CHAR:
            next_directions = [(direction[1], direction[0])]

        next_beams = [((pos[0] + d[0], pos[1] + d[1]), d) for d in next_directions]
        return [beam for beam in next_beams if self.is_valid_position(beam[0][0], beam[0][1])]

    @lru_cache(maxsize=None)
    def get_char(self, x: int, y: int) -> str:
        return self.rows[y][x]

    @lru_cache(maxsize=None)
    def is_valid_position(self, x, y) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
