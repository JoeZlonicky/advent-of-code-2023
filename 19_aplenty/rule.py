from dataclasses import dataclass
from machine_part import MachinePart


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

    def get_accepted_in_range(self, range_min, range_max) -> tuple[int, int]:
        if self.category == '':
            return range_min, range_max

        if self.comparison_operator == '>':
            return max(range_max - self.comparison_value, 0)

        return max(self.comparison_value - range_min, 0)

    def does_value_match(self, value):
        return value > self.comparison_value if self.comparison_operator == '>' else value < self.comparison_value
