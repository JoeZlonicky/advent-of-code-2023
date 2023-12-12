from functools import lru_cache


class ConditionRecord:
    OPERATIONAL_CHAR = '.'
    DAMAGED_CHAR = '#'
    UNKNOWN_CHAR = '?'

    def __init__(self, spring_row: str, damaged_contiguous_groups: list[int]):
        self.spring_row = spring_row
        self.damaged_contiguous_groups = damaged_contiguous_groups

    @lru_cache(maxsize=None)
    def calc_n_arrangements(self, start_spring_i=0, group_i=0):
        if start_spring_i >= len(self.spring_row) or group_i >= len(self.damaged_contiguous_groups):
            return 0

        # First figure out if there is even enough space to fit the current situation
        remaining_damaged_springs = sum(self.damaged_contiguous_groups[group_i:])
        n_groups_left_to_fit = len(self.damaged_contiguous_groups) - group_i

        remaining_space_required = remaining_damaged_springs + (n_groups_left_to_fit - 1)
        remaining_space = len(self.spring_row) - start_spring_i

        if remaining_space_required > remaining_space:
            return 0

        # Now to figure out if the current group matches
        current_group_length = self.damaged_contiguous_groups[group_i]
        end_spring_i = start_spring_i + current_group_length

        fits = self.OPERATIONAL_CHAR not in self.spring_row[start_spring_i:end_spring_i]
        fits = fits and (end_spring_i == len(self.spring_row) or self.spring_row[end_spring_i] != self.DAMAGED_CHAR)
        fits = fits and (start_spring_i == 0 or self.spring_row[start_spring_i - 1] != self.DAMAGED_CHAR)

        # If not restricted by knowing the leftmost is for sure a damaged spring, we calculate all the variations
        # that start further to the right
        n_with_starting_more_right = 0
        if self.spring_row[start_spring_i] != self.DAMAGED_CHAR:
            n_with_starting_more_right = self.calc_n_arrangements(start_spring_i + 1, group_i)

        # Invalid, discard this version and only go with other variations
        if not fits:
            return n_with_starting_more_right

        # Check if we have a valid arrangement we can count
        valid_solution = fits and n_groups_left_to_fit == 1 and self.DAMAGED_CHAR not in self.spring_row[end_spring_i:]
        if valid_solution:
            return 1 + n_with_starting_more_right

        # This group fits, but now we need to calculate how many arrangements with the remaining
        n_with_this_one_fitting = self.calc_n_arrangements(end_spring_i + 1, group_i + 1)
        return n_with_starting_more_right + n_with_this_one_fitting

    @classmethod
    def from_line(cls, line: str, n_copies=1) -> 'ConditionRecord':
        spring_row, damaged_contiguous_groups = line.split()
        damaged_contiguous_groups = [int(n) for n in damaged_contiguous_groups.split(',')]
        if n_copies == 1:
            return cls(spring_row, damaged_contiguous_groups)

        expanded_row = spring_row
        expanded_damaged_contiguous_groups = damaged_contiguous_groups[:]
        for _ in range(n_copies - 1):
            expanded_row += '?' + spring_row
            expanded_damaged_contiguous_groups += damaged_contiguous_groups[:]

        return cls(expanded_row, expanded_damaged_contiguous_groups)
