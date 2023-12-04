class Card:
    def __init__(self, number: int, winning_numbers: list[int], numbers_in_possession: list[int]):
        self.number = number
        self.winning_numbers = winning_numbers
        self.numbers_in_possession = numbers_in_possession

    def get_matching_numbers(self) -> list[int]:
        return [number for number in self.numbers_in_possession if number in self.winning_numbers]

    def calculate_points(self) -> int:
        n_matching = len(self.get_matching_numbers())
        if n_matching == 0:
            return 0

        return pow(2, n_matching - 1)

    @classmethod
    def from_line(cls, line: str):
        line = " ".join(line.split())
        label, number_sections = line.split(':')

        number = int(label.split()[1])

        winning_numbers, numbers_in_possession = number_sections.split('|')
        winning_numbers = [int(number) for number in winning_numbers.split()]
        numbers_in_possession = [int(number) for number in numbers_in_possession.split()]

        return cls(number, winning_numbers, numbers_in_possession)
