from collections import defaultdict
from bounding_box import BoundingBox


class SandSimulation:
    def __init__(self, boxes: list[BoundingBox]):
        self.__boxes = []
        self.__z_layers = defaultdict(lambda: [])
        for box in boxes:
            self.add_box(box)

        self.__supported_by = defaultdict(lambda: [])
        self.__supports = defaultdict(lambda: [])
        self.__simulated = False

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
        self.__simulated = False

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

            self.__move_box_down(box, new_bottom)

        self.__determine_supported_by()
        self.__determine_supports()
        self.__simulated = True

    def __move_box_down(self, box: BoundingBox, new_bottom: int):
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

    def __determine_supported_by(self):
        for box in self.__boxes:
            if box.bottom == 1:
                continue  # Supported by ground

            below_z = box.bottom - 1
            if below_z not in self.__z_layers:
                continue

            for other in self.__z_layers[below_z]:
                if self.do_boxes_horizontally_intersect(box, other):
                    self.__supported_by[box].append(other)

    def __determine_supports(self):
        for box in self.__boxes:
            above_z = box.top + 1
            if above_z not in self.__z_layers:
                continue

            for other in self.__z_layers[above_z]:
                if self.do_boxes_horizontally_intersect(box, other):
                    self.__supports[box].append(other)

    def get_unsafe_to_disintegrate(self) -> list[BoundingBox]:
        assert self.__simulated

        unsafe = []
        for box in self.__supported_by:
            supporting_boxes = self.__supported_by[box]
            n_supporting_boxes = len(supporting_boxes)
            if n_supporting_boxes == 0:
                continue

            if n_supporting_boxes == 1:
                if supporting_boxes[0] not in unsafe:
                    unsafe.append(supporting_boxes[0])

        return unsafe

    def calc_safe_to_disintegrate(self) -> int:
        return len(self.__boxes) - len(self.get_unsafe_to_disintegrate())

    def sum_affected_for_each_block_disintegrated(self):
        affected_total = 0
        unsafe = self.get_unsafe_to_disintegrate()
        for unsafe_box in unsafe:
            affected = [unsafe_box]
            to_check = self.__supports[unsafe_box][:]
            while to_check:
                above_box = to_check.pop()

                above_supported_by = self.__supported_by[above_box]
                if any([supported_by not in affected for supported_by in above_supported_by]):
                    continue

                if above_box not in affected:
                    affected.append(above_box)

                for b in self.__supports[above_box]:
                    if b not in affected and b not in to_check:
                        to_check.append(b)

            affected_total += len(affected) - 1  # -1 because we don't count the disintegrated box

        return affected_total

    @staticmethod
    def do_boxes_horizontally_intersect(box1: BoundingBox, box2: BoundingBox):
        is_right = box1.left > box2.right
        is_left = box1.right < box2.left
        is_closer = box1.back < box2.front
        is_further = box1.front > box2.back

        return not (is_right or is_left or is_closer or is_further)
