from mapping import Mapping


class MappingSection:
    def __init__(self, input_name: str, output_name: str):
        self.input_name = input_name
        self.output_name = output_name
        self.mappings: list[Mapping] = []

    def add_mapping(self, mapping: Mapping):
        self.mappings.append(mapping)

    def map_values(self, values: list[int]):
        mapped_values = []
        for value in values:
            for mapping in self.mappings:
                if mapping.is_in_range(value):
                    mapped_values.append(mapping.map(value))
                    break
            else:
                mapped_values.append(value)
        return mapped_values

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
        return 'hello', 'world'
