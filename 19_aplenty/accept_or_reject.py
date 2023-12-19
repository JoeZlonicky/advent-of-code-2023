from machine_part import MachinePart
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
