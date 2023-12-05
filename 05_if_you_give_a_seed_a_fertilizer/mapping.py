class Mapping:
    def __init__(self, dest_range_start: int, src_range_start: int,
                 range_length: int):
        self.dest_range_start = dest_range_start
        self.src_range_start = src_range_start
        self.range_length = range_length

    def is_in_range(self, value: int) -> bool:
        return True

    def map(self, value: int) -> int:
        return value

    @classmethod
    def from_line(cls, line: str) -> 'Mapping':
        pass
