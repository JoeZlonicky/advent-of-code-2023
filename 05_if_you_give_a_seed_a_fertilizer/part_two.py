from mapping_section import MappingSection
from shared_functions import get_line_sections_from_text_file, create_mapping_sections, perform_mapping_pipeline

INPUT_FILE_NAME = 'inputs/small_input.txt'


def main():
    line_sections = get_line_sections_from_text_file(INPUT_FILE_NAME)
    seed_list = parse_seed_list(line_sections[0][0])

    mapping_sections: dict[str, MappingSection] = create_mapping_sections(line_sections[1:])
    output_values = perform_mapping_pipeline('seed', seed_list, mapping_sections)
    output_values.sort()
    print(output_values[0])


def parse_seed_list(line: str) -> list:
    numbers_string = line.split(':')[1].strip()
    numbers = [int(number_string) for number_string in numbers_string.split()]
    seeds = []
    for i in range(0, len(numbers), 2):
        seeds += [(numbers[i], numbers[i] + numbers[i + 1] - 1)]
    return seeds


if __name__ == '__main__':
    main()
