from machine_part import MachinePart, MachinePartRange
from processor import Processor

ACCEPT_PROCESSOR_NAME = 'A'
REJECT_PROCESSOR_NAME = 'R'


def sum_accepted(processors: dict[str, Processor], parts: list[MachinePart]) -> int:
    current_sum = 0
    for part in parts:
        is_accepted = accept_or_reject(part, processors)
        if is_accepted:
            current_sum += part.calculate_rating()
    return current_sum


def accept_or_reject(part: MachinePart, processors: dict[str, Processor]):
    current_processor = processors['in']
    while True:
        next_processor_name = current_processor.process_part(part)

        if next_processor_name == ACCEPT_PROCESSOR_NAME:
            return True
        if next_processor_name == REJECT_PROCESSOR_NAME:
            return False

        current_processor = processors[next_processor_name]


def count_distinct_combinations_of_accepted(processors: dict[str, Processor], min_category_rating: int,
                                            max_category_rating: int) -> int:
    category_range = (min_category_rating, max_category_rating)
    start_range = MachinePartRange(category_range, category_range, category_range, category_range)
    accepted_ranges = []

    range_stack = [('in', start_range)]
    while range_stack:
        current_processor_name, current_range = range_stack.pop()
        current_processor = processors[current_processor_name]

        outputs = current_processor.process_part_range(current_range)
        for output in outputs:
            next_processor_name, output_range = output
            if next_processor_name == ACCEPT_PROCESSOR_NAME:
                accepted_ranges.append(output_range)
                continue
            elif next_processor_name == REJECT_PROCESSOR_NAME:
                continue

            range_stack.append(output)

    n_combinations = 0
    for part_range in accepted_ranges:
        x_range_length = part_range.x[1] - part_range.x[0] + 1
        m_range_length = part_range.m[1] - part_range.m[0] + 1
        a_range_length = part_range.a[1] - part_range.a[0] + 1
        s_range_length = part_range.s[1] - part_range.s[0] + 1
        n_combinations += x_range_length * m_range_length * a_range_length * s_range_length

    return n_combinations
