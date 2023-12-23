from collections import defaultdict
from bounding_box import BoundingBox


class SandSimulation:
    def __init__(self, boxes: list[BoundingBox]):
        self.__boxes = []
        self.__z_layers = defaultdict(lambda: [])

        for box in boxes:
            self.add_box(box)

    @classmethod
    def from_file(cls, file_path) -> 'SandSimulation':
        with open(file_path) as f:
            lines = [line.strip() for line in f]

        boxes = []
        for idx, line in enumerate(lines):
            box = BoundingBox.from_line(line)
            box.label = chr(ord('a') + idx)
            boxes.append(box)

        return cls(boxes)

    def add_box(self, box: BoundingBox):
        self.__boxes.append(box)
        for z in range(box.bottom, box.top + 1):
            self.__z_layers[z].append(box)

    def simulate_falling(self):
        self.__boxes.sort(key=lambda x: x.bottom)

        for box in self.__boxes:
            new_bottom = -1

            for z in range(box.bottom - 1, 0, -1):
                if z not in self.__z_layers:
                    new_bottom = z
                    continue

                intersection = False
                for other in self.__z_layers[z]:
                    if self.do_boxes_horizontally_intersect(box, other):
                        intersection = True
                        break

                if intersection:
                    break

                new_bottom = z

            if new_bottom == -1:
                continue

            self.move_box_down(box, new_bottom)

    def move_box_down(self, box: BoundingBox, new_bottom: int):
        height = box.top - box.bottom + 1
        new_top = new_bottom + height - 1
        top_of_insertion = min(new_top, box.bottom)
        for z in range(new_bottom, top_of_insertion + 1):
            self.__z_layers[z].append(box)

        bottom_of_removal = box.top - height + 1

        for z in range(bottom_of_removal, box.top + 1):
            self.__z_layers[z].remove(box)

        box.top = new_top
        box.bottom = new_bottom

    def determine_supported_by(self) -> dict[BoundingBox, list[BoundingBox]]:
        supported_by = defaultdict(lambda: [])

        for box in self.__boxes:
            if box.bottom == 1:
                continue  # Supported by ground

            below_z = box.bottom - 1
            if below_z not in self.__z_layers:
                continue

            for other in self.__z_layers[below_z]:
                if self.do_boxes_horizontally_intersect(box, other):
                    supported_by[box].append(other)

        return supported_by

    def count_safe_to_disintegrate(self) -> int:
        supported_by = self.determine_supported_by()
        unsafe = []
        for box in supported_by:
            supporting_boxes = supported_by[box]
            n_supporting_boxes = len(supporting_boxes)
            if n_supporting_boxes == 0:
                continue

            if n_supporting_boxes == 1:
                if supporting_boxes[0] not in unsafe:
                    unsafe.append(supporting_boxes[0])

        return len(self.__boxes) - len(unsafe)

    @staticmethod
    def do_boxes_horizontally_intersect(box1: BoundingBox, box2: BoundingBox):
        is_right = box1.left > box2.right
        is_left = box1.right < box2.left
        is_closer = box1.back < box2.front
        is_further = box1.front > box2.back

        return not (is_right or is_left or is_closer or is_further)
