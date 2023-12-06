class Mapping:
    def __init__(self, src_range_start: int, dest_range_start: int,
                 range_length: int):
        self.dest_range_start = dest_range_start
        self.src_range_start = src_range_start
        self.range_length = range_length

    def is_in_range(self, value: int) -> bool:
        return 0 <= value - self.src_range_start < self.range_length

    # value can either be an int or a tuple representing an inclusive range
    # Will either return an int, a tuple range, or a list of tuple ranges if a tuple needs to be split
    def map(self, value):
        if self.is_in_range(value):
            return self.dest_range_start + value - self.src_range_start
        return value

    @classmethod
    def from_line(cls, line: str) -> 'Mapping':
        dest, src, range_length = line.split()
        return cls(int(src), int(dest), int(range_length))
