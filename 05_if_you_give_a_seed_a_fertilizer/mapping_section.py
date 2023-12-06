from mapping import Mapping
from seed_range import SeedRange


class MappingSection:
    def __init__(self, input_name: str, output_name: str):
        self.input_name = input_name
        self.output_name = output_name
        self.mappings: list[Mapping] = []

    def add_mapping(self, mapping: Mapping):
        self.mappings.append(mapping)

    def map_ranges(self, ranges: list[SeedRange]) -> list[SeedRange]:
        mapped_ranges = []
        unmapped_ranges = ranges[:]  # Using a stack for handling leftover ranges from splits
        while True:
            if len(unmapped_ranges) == 0:
                return mapped_ranges

            seed_range = unmapped_ranges.pop()
            for mapping in self.mappings:
                mapped, unmapped = mapping.map(seed_range)
                if mapped:
                    mapped_ranges.extend(mapped)
                    if unmapped:
                        unmapped_ranges.extend(unmapped)  # Throw leftover on stack to be mapped
                    break
            else:
                mapped_ranges.append(seed_range)  # No matching so 1:1 mapping

    @classmethod
    def from_section_lines(cls, lines: list[str]) -> 'MappingSection':
        input_name, output_name = cls.parse_mapping_title(lines[0])
        mapping_list = cls(input_name, output_name)
        for line in lines[1:]:
            mapping = Mapping.from_line(line)
            mapping_list.add_mapping(mapping)
        return mapping_list

    @staticmethod
    def parse_mapping_title(line: str) -> tuple[str, str]:
        title = line.split()[0]
        input_name, _, output_name = title.split('-')
        return input_name, output_name
