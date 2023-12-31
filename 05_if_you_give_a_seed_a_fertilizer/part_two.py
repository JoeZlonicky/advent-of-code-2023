from mapping_section import MappingSection
from seed_range import SeedRange
from shared_functions import get_line_sections_from_text_file, create_mapping_sections, perform_mapping_pipeline

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    line_sections = get_line_sections_from_text_file(INPUT_FILE_NAME)
    seed_ranges = parse_seed_list(line_sections[0][0])

    mapping_sections: dict[str, MappingSection] = create_mapping_sections(line_sections[1:])
    output_ranges = perform_mapping_pipeline('seed', seed_ranges, mapping_sections)

    output_ranges.sort(key=lambda x: x[0])
    range_with_smallest_start = output_ranges[0]
    print(range_with_smallest_start[0])


def parse_seed_list(line: str) -> list[SeedRange]:
    numbers_string = line.split(':')[1].strip()
    numbers = [int(number_string) for number_string in numbers_string.split()]
    ranges = []
    for i in range(0, len(numbers), 2):
        ranges += [(numbers[i], numbers[i] + numbers[i + 1] - 1)]
    return ranges


if __name__ == '__main__':
    main()
