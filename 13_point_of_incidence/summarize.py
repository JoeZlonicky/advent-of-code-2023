from mirror_lines import find_mirror_line, MirrorLineResult
from parse_input_file import parse_input_file


def summarize(input_file) -> int:
    sections = parse_input_file(input_file)

    sum_columns_to_left = 0
    sum_rows_above = 0

    for section in sections:
        result: MirrorLineResult = find_mirror_line(section)
        sum_columns_to_left += result.n_columns_to_left
        sum_rows_above += result.n_rows_above

    return sum_columns_to_left + sum_rows_above * 100


def summarize_with_smudges(input_file) -> int:
    sections = parse_input_file(input_file)

    sum_columns_to_left = 0
    sum_rows_above = 0

    for section in sections:
        without_smudges = find_mirror_line(section)

        for line_idx, line in enumerate(section):
            line_as_list = list(line)
            match_found = False
            
            for idx, char in enumerate(line):
                line_as_list[idx] = '#' if char == '.' else '.'
                section[line_idx] = ''.join(line_as_list)

                result: MirrorLineResult = find_mirror_line(section, True, without_smudges)
                if result != (0, 0):
                    sum_columns_to_left += result.n_columns_to_left
                    sum_rows_above += result.n_rows_above
                    match_found = True
                    break

                line_as_list[idx] = char
                section[line_idx] = line

            if match_found:
                break

    return sum_columns_to_left + sum_rows_above * 100
