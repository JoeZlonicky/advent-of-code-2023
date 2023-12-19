from machine_part import MachinePart
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
