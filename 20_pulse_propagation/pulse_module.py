from collections import defaultdict
from enum import Enum

BROADCASTER_NAME = 'broadcaster'
FLIP_FLOP_PREFIX = '%'
CONJUNCTION_PREFIX = '&'


class PulseModuleType(Enum):
    BROADCASTER = 1
    CONJUNCTION = 2
    FLIP_FLOP = 3


class PulseModule:
    def __init__(self, module_type: PulseModuleType, outputs: list[str]):
        self.module_type = module_type
        self.outputs = outputs
        self.input_memory = defaultdict(lambda: False)

    @classmethod
    def from_line(cls, line: str) -> tuple[str, 'PulseModule']:
        left, right = [side.strip() for side in line.split('->')]
        outputs = [output.strip() for output in right.split(',')]
        if left == 'broadcaster':
            return left, cls(PulseModuleType.BROADCASTER, outputs)
        elif left.startswith(FLIP_FLOP_PREFIX):
            return left.removeprefix(FLIP_FLOP_PREFIX), cls(PulseModuleType.FLIP_FLOP, outputs)
        elif left.startswith(CONJUNCTION_PREFIX):
            return left.removeprefix(CONJUNCTION_PREFIX), cls(PulseModuleType.CONJUNCTION, outputs)

        assert False

    def add_input_connection(self, input_module_name: str):
        if self.module_type != PulseModuleType.CONJUNCTION:
            return

        self.input_memory[input_module_name] = False
