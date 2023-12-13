from functools import lru_cache
from typing import NamedTuple


class MirrorLineResult(NamedTuple):
    n_rows_above: int = 0
    n_columns_to_left: int = 0


def find_mirror_line(rows, check_columns_if_not_found=True, ignore_result=(0, 0)) -> MirrorLineResult:
    gaps_to_check = tuple(range(len(rows[0]) - 1))
    for row in rows:
        if not gaps_to_check:
            break
        gaps_to_check = find_mirror_lines_for_line(row, gaps_to_check)

    for gap in gaps_to_check:
        result = MirrorLineResult(0, gap + 1)
        if result != ignore_result:
            return result

    if check_columns_if_not_found:
        columns = [''.join(i) for i in zip(*rows)]
        columns_to_left = find_mirror_line(columns[::-1], False, ignore_result[::-1]).n_columns_to_left
        result = MirrorLineResult(columns_to_left, 0)
        if result != ignore_result:
            return result

    return MirrorLineResult(0, 0)


@lru_cache(maxsize=None)
def find_mirror_lines_for_line(line: str, gaps_to_check: tuple) -> tuple:
    mirror_lines = []
    for gap_i in gaps_to_check:
        if is_mirror_line_for_line(gap_i, line):
            mirror_lines.append(gap_i)
    return tuple(mirror_lines)


# gap_i of 0 is the gap between columns 0 and 1; 1 is between 1 and 2; and so on
def is_mirror_line_for_line(gap_i: int, line: str) -> bool:
    left_distance = gap_i + 1
    right_distance = len(line) - left_distance
    distance_check = min(left_distance, right_distance)
    left = line[left_distance - distance_check:left_distance]
    right = line[left_distance:left_distance + distance_check]
    return left == right[::-1]
