from mapping_section import MappingSection


def get_line_sections_from_text_file(file_name: str) -> list[list[str]]:
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        sections = [[]]
        for line in lines:
            if line == '' and len(sections[-1]) > 0:
                sections.append([])
            else:
                sections[-1].append(line)
        return sections


def create_mapping_sections(line_sections: list[list[str]]) -> dict[str, MappingSection]:
    mapping_sections: dict[str, MappingSection] = {}
    for section in line_sections:
        mapping_section = MappingSection.from_section_lines(section)
        assert mapping_section.input_name not in mapping_sections
        mapping_sections[mapping_section.input_name] = mapping_section
    return mapping_sections


# values can contain integers and/or tuples representing inclusive ranges
# Returned list is a list of integers and/or tuples representing inclusive ranges
def perform_mapping_pipeline(starting_input_name: str, values: list,
                             mapping_sections: dict[str, MappingSection]) -> list:
    current_input = starting_input_name
    current_values = values
    while current_input in mapping_sections:
        mapping_list = mapping_sections[current_input]
        current_values = mapping_list.map_values(current_values)
        current_input = mapping_list.output_name
    return current_values
