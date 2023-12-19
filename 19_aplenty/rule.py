from dataclasses import dataclass
from machine_part import MachinePart, MachinePartRange


@dataclass
class Rule:
    category: str
    comparison_operator: str
    comparison_value: int
    output: str

    @classmethod
    def from_string(cls, s) -> 'Rule':
        if ':' not in s:
            return cls('', '', 0, s)

        comparison, output = s.split(':')
        if '>' in comparison:
            left, right = comparison.split('>')
            return cls(left, '>', int(right), output)

        left, right = comparison.split('<')
        return cls(left, '<', int(right), output)

    def does_part_match(self, part: MachinePart):
        if self.category == '':
            return True

        if self.category == 'x':
            return self.does_value_match(part.x)
        elif self.category == 'm':
            return self.does_value_match(part.m)
        elif self.category == 'a':
            return self.does_value_match(part.a)
        elif self.category == 's':
            return self.does_value_match(part.s)

        return False

    def split_range(self, part_range: MachinePartRange) -> tuple[MachinePartRange | None, MachinePartRange | None]:
        if self.category == '':
            return part_range, None

        if self.category == 'x':
            matching, not_matching = self.split_range_on_value(part_range.x)
            matching_part_range = MachinePartRange(matching, part_range.m, part_range.a,
                                                   part_range.s) if matching else None
            not_matching_part_range = MachinePartRange(not_matching, part_range.m, part_range.a,
                                                       part_range.s) if not_matching else None
            return matching_part_range, not_matching_part_range

        elif self.category == 'm':
            matching, not_matching = self.split_range_on_value(part_range.m)
            matching_part_range = MachinePartRange(part_range.x, matching, part_range.a,
                                                   part_range.s) if matching else None
            not_matching_part_range = MachinePartRange(part_range.x, not_matching, part_range.a,
                                                       part_range.s) if not_matching else None
            return matching_part_range, not_matching_part_range

        elif self.category == 'a':
            matching, not_matching = self.split_range_on_value(part_range.a)
            matching_part_range = MachinePartRange(part_range.x, part_range.m, matching,
                                                   part_range.s) if matching else None
            not_matching_part_range = MachinePartRange(part_range.x, part_range.m, not_matching,
                                                       part_range.s) if not_matching else None
            return matching_part_range, not_matching_part_range

        elif self.category == 's':
            matching, not_matching = self.split_range_on_value(part_range.s)
            matching_part_range = MachinePartRange(part_range.x, part_range.m, part_range.a,
                                                   matching) if matching else None
            not_matching_part_range = MachinePartRange(part_range.x, part_range.m, part_range.a,
                                                       not_matching) if not_matching else None
            return matching_part_range, not_matching_part_range

        return None, part_range

    def does_value_match(self, value):
        return value > self.comparison_value if self.comparison_operator == '>' else value < self.comparison_value

    def split_range_on_value(self, r: tuple[int, int]) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
        if self.comparison_operator == '>':
            if self.comparison_value >= r[1]:
                return None, r
            if self.comparison_value < r[0]:
                return r, None

            match_upper = r[1]
            match_lower = self.comparison_value + 1
            not_matching_upper = self.comparison_value
            not_matching_lower = r[0]
            return (match_lower, match_upper), (not_matching_lower, not_matching_upper)

        # self.comparison_operator == '>'

        if self.comparison_value <= r[0]:
            return None, r
        if self.comparison_value > r[1]:
            return r, None

        match_upper = self.comparison_value - 1
        match_lower = r[0]
        not_matching_upper = r[1]
        not_matching_lower = self.comparison_value
        return (match_lower, match_upper), (not_matching_lower, not_matching_upper)
