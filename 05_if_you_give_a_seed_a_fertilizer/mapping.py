from seed_range import SeedRange


class Mapping:
    def __init__(self, src_range_start: int, dest_range_start: int,
                 range_length: int):
        self.dest_range_start = dest_range_start
        self.dest_range_end = dest_range_start + range_length - 1

        self.src_range_start = src_range_start
        self.src_range_end = src_range_start + range_length - 1

        self.range_length = range_length
        self.offset = self.dest_range_start - self.src_range_start

    # Returns ([mapped_seed_ranges, ...], [unmapped_seed_ranges, ...])
    def map(self, seed_range: SeedRange) -> tuple[list[SeedRange], list[SeedRange]]:
        # Unmapped completely
        if seed_range[0] > self.src_range_end:
            return [], [seed_range]

        # Unmapped completely
        if seed_range[1] < self.src_range_start:
            return [], [seed_range]

        # Right portion is mapped and left portion is unmapped
        if seed_range[0] < self.src_range_start and seed_range[1] <= self.src_range_end:
            mapped = (self.src_range_start + self.offset, seed_range[1] + self.offset)
            unmapped = (seed_range[0], self.src_range_start - 1)
            return [mapped], [unmapped]

        # Left portion is mapped and right portion is unmapped
        if seed_range[0] >= self.src_range_start and seed_range[1] > self.src_range_end:
            mapped = (seed_range[0] + self.offset, self.dest_range_end)
            unmapped = (self.src_range_end + 1, seed_range[1])
            return [mapped], [unmapped]

        # Inner section is mapped and outer is unmapped
        if seed_range[0] < self.src_range_start and seed_range[1] > self.src_range_end:
            mapped = (self.dest_range_start, self.dest_range_end)
            unmapped_left = (seed_range[0], self.src_range_start - 1)
            unmapped_right = (self.src_range_end + 1, seed_range[1])
            return [mapped], [unmapped_left, unmapped_right]

        # Entirely within mapping range
        return [(seed_range[0] + self.offset, seed_range[1] + self.offset)], []

    @classmethod
    def from_line(cls, line: str) -> 'Mapping':
        dest, src, range_length = line.split()
        return cls(int(src), int(dest), int(range_length))
