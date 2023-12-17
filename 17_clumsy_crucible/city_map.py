class CityMap:
    def __init__(self, rows: list[list[int]]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0]) if self.height > 0 else 0

    @classmethod
    def from_file(cls, file_path: str) -> 'CityMap':
        with open(file_path) as f:
            lines = [line.strip() for line in f]
            rows = [[int(x) for x in row] for row in lines if row]
            return cls(rows)

    def get_value(self, x: int, y: int) -> int:
        return self.rows[y][x]

    def is_in_map(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get_surrounding_positions(self, x: int, y: int) -> list[tuple[int, int]]:
        positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [position for position in positions if self.is_in_map(position[0], position[1])]
