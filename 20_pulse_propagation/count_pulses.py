from collections import deque
from functools import reduce
from pulse_module import PulseModule, PulseModuleType


def count_pulses_n_times(modules: dict[str, PulseModule], n: int = 1) -> tuple[int, int]:
    low = 0
    high = 0
    for _ in range(n):
        iteration_low, iteration_high = count_pulses(modules)
        low += iteration_low
        high += iteration_high
    return low, high


def min_presses_until_one_rx_low(modules: dict[str, PulseModule]) -> int:
    # Since the rx input is a conjunction module that occurs very infrequently,
    # we figure out the cycle of each input into the conjunction module and then when we know them all
    # we can just find the product of them for the LCM
    rx_inputs = modules['rx'].input_memory
    rx_conjunction_module = next(iter(rx_inputs))
    conjunction_inputs = modules[rx_conjunction_module].input_memory
    watchers = {input_name: False for input_name in conjunction_inputs}
    presses_for_each_input = {}

    presses = 0
    while True:
        presses += 1
        _, _ = count_pulses(modules, watchers)
        for module_name in watchers:
            got_high_signal = watchers[module_name]
            if got_high_signal and module_name not in presses_for_each_input:
                presses_for_each_input[module_name] = presses
                if len(presses_for_each_input) == len(conjunction_inputs):
                    return reduce(lambda x, y: x * y, presses_for_each_input.values())


# Counts the number of (low, high, low_rx) pulses
def count_pulses(modules: dict[str, PulseModule], high_output_watchers=None) -> tuple[int, int]:
    if high_output_watchers is None:
        high_output_watchers = {}
    low = 0
    high = 0
    out_signals = deque()
    out_signals.append(('button', 'broadcaster', False))
    while out_signals:
        from_name, module_name, is_high_signal = out_signals.popleft()
        if is_high_signal:
            high += 1
            if from_name in high_output_watchers:
                high_output_watchers[from_name] = True
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
