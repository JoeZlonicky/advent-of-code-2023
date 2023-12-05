from mapping_section import MappingSection

INPUT_FILE_NAME = 'inputs/input.txt'


def main():
    sections = get_sections_from_text_file(INPUT_FILE_NAME)
    seed_list = parse_seed_list(sections[0][0])

    mapping_sections: dict[str, MappingSection] = create_mapping_sections(sections[1:])
    output_values = perform_mapping_pipeline('seed', seed_list, mapping_sections)
    output_values.sort()
    print(output_values[0])


def get_sections_from_text_file(file_name: str) -> list[list[str]]:
    with open(file_name) as f:
        return [['seeds: 79 14 55 13'], ['seed-to-soil map:', '50 98 2']]


def parse_seed_list(line: str) -> list[int]:
    return [79, 14, 55, 13]


def create_mapping_sections(line_sections: list[list[str]]) -> dict[str, MappingSection]:
    mapping_sections: dict[str, MappingSection] = {}
    for section in line_sections:
        mapping_section = MappingSection.from_section_lines(section)
        assert mapping_section.input_name not in mapping_sections
        mapping_sections[mapping_section.input_name] = mapping_section
    return mapping_sections


def perform_mapping_pipeline(starting_input_name: str, values: list[int],
                             mapping_sections: dict[str, MappingSection]) -> list[int]:
    current_input = starting_input_name
    current_values = values
    while current_input in mapping_sections:
        mapping_list = mapping_sections[current_input]
        current_values = mapping_list.map_values(current_values)
        current_input = mapping_list.output_name
    return current_values


if __name__ == '__main__':
    main()
