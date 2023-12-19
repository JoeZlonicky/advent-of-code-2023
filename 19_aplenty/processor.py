from machine_part import MachinePart, MachinePartRange
from rule import Rule


class Processor:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    @classmethod
    def from_line(cls, line) -> tuple[str, 'Processor']:
        name, rule_list = line.split('{')
        rule_list = rule_list.strip('}').split(',')

        rules = []
        for rule in rule_list:
            rules.append(Rule.from_string(rule))

        return name, cls(rules)

    def process_part(self, part: MachinePart) -> str:
        for rule in self.rules:
            if rule.does_part_match(part):
                return rule.output
        assert False

    def process_part_range(self, part_range: MachinePartRange) -> list[tuple[str, MachinePartRange]]:
        resulting_ranges = []
        current_range = part_range

        for rule in self.rules:
            matching, not_matching = rule.split_range(current_range)
            if matching:
                resulting_ranges.append((rule.output, matching))
            if not not_matching:
                break
            current_range = not_matching

        return resulting_ranges
