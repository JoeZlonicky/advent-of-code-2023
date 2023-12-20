from collections import deque
from pulse_module import PulseModule, PulseModuleType


def count_pulses_n_times(modules: dict[str, PulseModule], n: int = 1) -> tuple[int, int]:
    low = 0
    high = 0
    for _ in range(n):
        iteration_low, iteration_high = count_pulses(modules)
        low += iteration_low
        high += iteration_high
    return low, high


# Counts the number of (low, high) pulses
def count_pulses(modules: dict[str, PulseModule]) -> tuple[int, int]:
    low = 0
    high = 0
    out_signals = deque()
    out_signals.append(('button', 'broadcaster', False))
    while out_signals:
        from_name, module_name, is_high_signal = out_signals.popleft()
        if is_high_signal:
            high += 1
        else:
            low += 1

        if module_name not in modules:
            continue

        module = modules[module_name]
        if module.module_type == PulseModuleType.BROADCASTER:
            for output in module.outputs:
                out_signals.append((module_name, output, is_high_signal))
        elif module.module_type == PulseModuleType.FLIP_FLOP:
            if is_high_signal:
                continue
            is_turned_on = not module.input_memory['inputs']
            module.input_memory['inputs'] = is_turned_on
            for output in module.outputs:
                out_signals.append((module_name, output, is_turned_on))
        elif module.module_type == PulseModuleType.CONJUNCTION:
            module.input_memory[from_name] = is_high_signal
            all_high = all(module.input_memory.values())
            for output in module.outputs:
                out_signals.append((module_name, output, not all_high))

    return low, high
