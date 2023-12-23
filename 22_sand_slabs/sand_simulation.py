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

    def count_safe_to_disintegrate(self):
        not_safe = []

        # Instead of checking which boxes are above, we count the number of boxes that are only supported
        # by one below and thus unsafe. Then we can just use that number and total to find the number of safe boxes.
        for box in self.__boxes:
            if box.bottom == 1:
                continue

            below_z = box.bottom - 1
            if below_z not in self.__z_layers:
                assert False  # Means falling failed or something else is going weird

            intersect_count = 0
            last_unsafe_box = None
            for other in self.__z_layers[below_z]:
                if self.do_boxes_horizontally_intersect(box, other):
                    intersect_count += 1
                    last_unsafe_box = other
                    if intersect_count > 1:
                        break

            assert intersect_count >= 1
            if intersect_count == 1 and last_unsafe_box not in not_safe:
                not_safe.append(last_unsafe_box)

        return len(self.__boxes) - len(not_safe)

    @staticmethod
    def do_boxes_horizontally_intersect(box1: BoundingBox, box2: BoundingBox):
        is_right = box1.left > box2.right
        is_left = box1.right < box2.left
        is_closer = box1.back < box2.front
        is_further = box1.front > box2.back

        return not (is_right or is_left or is_closer or is_further)
