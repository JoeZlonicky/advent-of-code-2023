def parse_ints_from_file(file_name) -> list[list[int]]:
    with open(file_name) as f:
        return [[int(x) for x in line.split()] for line in f if line.strip() != '']


def extrapolate_value_history(history: list[int], forward=True) -> int:
    if all(value == 0 for value in history):
        return 0

    diffs = [history[i] - history[i - 1] for i in range(1, len(history))]

    if forward:
        return history[-1] + extrapolate_value_history(diffs, forward)
    else:
        return history[0] - extrapolate_value_history(diffs, forward)
