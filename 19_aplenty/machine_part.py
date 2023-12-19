from dataclasses import dataclass


@dataclass
class MachinePart:
    x: int
    m: int
    a: int
    s: int

    @classmethod
    def from_line(cls, line) -> 'MachinePart':
        line = line.strip('{}')
        expressions = line.split(',')
        categories = {}

        for expression in expressions:
            category, value = expression.split('=')
            categories[category] = int(value)

        return cls(categories.get('x', 0), categories.get('m', 0), categories.get('a', 0), categories.get('s', 0))

    def calculate_rating(self):
        return self.x + self.m + self.a + self.s


@dataclass
class MachinePartRange:
    x: tuple[int, int]
    m: tuple[int, int]
    a: tuple[int, int]
    s: tuple[int, int]
