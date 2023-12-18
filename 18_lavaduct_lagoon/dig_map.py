from dig_plan import Edge, DigPlan

type pos = tuple[int, int]


class DigMap:
    def __init__(self, outline_edges: list[Edge], top_left: pos, bottom_right: pos):
        self.outline_edges = outline_edges
        self.top_left = top_left
        self.bottom_right = bottom_right

        # +1 because corners are inclusive
        self.width = self.bottom_right[0] - self.top_left[0] + 1
        self.height = self.bottom_right[1] - self.top_left[1] + 1

        # Indices need to be positive so the get/set cells methods will handle the mapping so top-left refers to [0][0]
        self.grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.mark_edges(self.outline_edges)

    @classmethod
    def from_dig_plan(cls, plan: DigPlan):
        return cls(plan.edges, plan.top_left, plan.bottom_right)

    def mark_edges(self, edges: list[Edge]):
        for edge in edges:
            x_start = min(edge.start[0], edge.end[0])
            x_end = max(edge.start[0], edge.end[0])
            y_start = min(edge.start[1], edge.end[1])
            y_end = max(edge.start[1], edge.end[1])
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    self.mark_cell(x, y)

    def mark_cell(self, x: int, y: int):
        x -= self.top_left[0]
        y -= self.top_left[1]
        self.grid[y][x] = True

    def get_cell(self, x, y):
        x -= self.top_left[0]
        y -= self.top_left[1]
        return self.grid[y][x]

    def is_cell_in_bounds(self, x, y):
        return self.top_left[0] <= x <= self.bottom_right[0] and self.top_left[1] <= y <= self.bottom_right[1]

    def count_marked_cells(self):
        count = 0
        for row in self.grid:
            count += sum(row)
        return count

    # Doesn't handle consecutive marked cells correctly, going to try bucket-fill
    def scanline_fill(self):
        for y in range(self.top_left[1], self.bottom_right[1] + 1):
            start_x = -1
            intersections = 0
            for x in range(self.top_left[0], self.bottom_right[0] + 1):
                if not self.get_cell(x, y):
                    continue
                intersections += 1
                if intersections % 2 == 0:
                    for i in range(start_x, x):
                        self.mark_cell(i, y)
                else:
                    start_x = x + 1

    def span_fill(self, start: pos):
        stack = [(start[0], start[0], start[1], 1),
                 (start[0], start[0], start[1] - 1, -1)]
        while stack:
            x1, x2, y, dy = stack.pop()
            x = x1
            if self.is_in_bounds_and_unmarked(x, y):
                while self.is_in_bounds_and_unmarked(x - 1, y):
                    self.mark_cell(x - 1, y)
                    x -= 1
                if x < x1:
                    stack.append((x, x1 - 1, y - dy, -dy))
            while x1 <= x2:
                while self.is_in_bounds_and_unmarked(x1, y):
                    self.mark_cell(x1, y)
                    x1 += 1
                if x1 > x:
                    stack.append((x, x1 - 1, y + dy, dy))
                if x1 - 1 > x2:
                    stack.append((x2 + 1, x1 - 1, y - dy, -dy))
                x1 += 1
                while x1 < x2 and self.is_in_bounds_and_marked(x1, y):
                    x1 += 1
                x = x1

    def is_in_bounds_and_unmarked(self, x: int, y: int):
        return self.is_cell_in_bounds(x, y) and not self.get_cell(x, y)

    def is_in_bounds_and_marked(self, x: int, y: int):
        return self.is_cell_in_bounds(x, y) and self.get_cell(x, y)

    def __str__(self):
        lines = []
        for row in self.grid:
            lines.append(''.join(['#' if value else ' ' for value in row]))
        return '\n'.join(lines)
