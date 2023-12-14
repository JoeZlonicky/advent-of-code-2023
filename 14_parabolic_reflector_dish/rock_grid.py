from enum import Enum


class SlideDirection(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


class RockGrid:
    EMPTY_CHAR = '.'
    ROUND_ROCK_CHAR = 'O'
    CUBE_ROCK_CHAR = '#'

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(self.rows)
        self.width = len(self.rows[0]) if self.height else 0

    @classmethod
    def from_file(cls, file_name):
        with open(file_name) as f:
            lines = [line.strip() for line in f]
            lines = [list(line) for line in lines if line]
            return cls(lines)

    def slide_round_rocks(self, direction: SlideDirection):
        motion = direction.value
        x_range = range(self.width) if motion[0] <= 0 else reversed(range(self.width))
        y_range = range(self.height) if motion[1] <= 0 else reversed(range(self.height))

        for y in y_range:
            for x in x_range:
                if not self.get_char(x, y) == self.ROUND_ROCK_CHAR:
                    continue

                self.slide_as_far_as_possible(x, y, direction)

    def sum_round_rock_load(self, direction: SlideDirection) -> int:
        load_sum = 0

        for y in range(self.height):
            for x in range(self.width):
                if not self.get_char(x, y) == self.ROUND_ROCK_CHAR:
                    continue

                if direction == SlideDirection.NORTH:
                    load_sum += self.height - y
                elif direction == SlideDirection.EAST:
                    load_sum += x + 1
                elif direction == SlideDirection.SOUTH:
                    load_sum += y + 1
                elif direction == SlideDirection.WEST:
                    load_sum += self.width - x

        return load_sum

    # Will slide everything north, west, south, east. Repeats specified times.
    def cycle(self, times=1):
        for i in range(times):
            print(i)
            self.slide_round_rocks(SlideDirection.NORTH)
            self.slide_round_rocks(SlideDirection.WEST)
            self.slide_round_rocks(SlideDirection.SOUTH)
            self.slide_round_rocks(SlideDirection.EAST)

    def slide_as_far_as_possible(self, x: int, y: int, direction: SlideDirection):
        motion = direction.value

        assert self.rows[y][x] == self.ROUND_ROCK_CHAR
        assert motion != (0, 0)

        current_x, current_y = x, y
        while True:
            next_x = current_x + motion[0]
            next_y = current_y + motion[1]
            if not self.is_free_space(next_x, next_y):
                break

            current_x, current_y = next_x, next_y

        if (x, y) != (current_x, current_y):
            self.set_char(x, y, self.EMPTY_CHAR)
            self.set_char(current_x, current_y, self.ROUND_ROCK_CHAR)

    def is_free_space(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False

        return self.get_char(x, y) == self.EMPTY_CHAR

    def set_char(self, x: int, y: int, char: str):
        self.rows[y][x] = char

    def get_char(self, x: int, y: int) -> str:
        return self.rows[y][x]
