from hash_algorithm import hash_string


class LensBox:
    def __init__(self, box_index: int):
        self.box_index = box_index
        self.lenses: dict[str, int] = {}

    def sum_lens_focusing_powers(self):
        power_sum = 0
        i = 0
        for lens in self.lenses:
            power_sum += (self.box_index + 1) * (i + 1) * self.lenses[lens]
            i += 1
        return power_sum

    def add_lens(self, lens_label, focal_length):
        self.lenses[lens_label] = focal_length

    def remove_lens(self, lens_label):
        if lens_label in self.lenses:
            del self.lenses[lens_label]


def create_lens_boxes(n: int) -> list[LensBox]:
    return [LensBox(i) for i in range(n)]


def perform_operations_on_boxes(boxes: list[LensBox], operations: list[str]):
    for operation in operations:
        if '=' in operation:
            label, focal_length = operation.split('=')
            add_lens(boxes, label, int(focal_length))
        elif '-' in operation:
            label = operation.split('-')[0]
            remove_lens(boxes, label)


def add_lens(boxes: list[LensBox], lens_label: str, focal_length: int):
    box_index = hash_string(lens_label)
    boxes[box_index].add_lens(lens_label, focal_length)


def remove_lens(boxes: list[LensBox], lens_label: str):
    box_index = hash_string(lens_label)
    boxes[box_index].remove_lens(lens_label)


def sum_focusing_powers(boxes: list[LensBox]):
    total_sum = 0
    for box in boxes:
        total_sum += box.sum_lens_focusing_powers()
    return total_sum
