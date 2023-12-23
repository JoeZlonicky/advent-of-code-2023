class BoundingBox:
    def __init__(self, top: int, right: int, bottom: int, left: int, front: int, back: int):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.front = front
        self.back = back
        self.label = ''

    @classmethod
    def from_line(cls, line: str):
        start, end = line.split('~')
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]
        return cls(end[2], end[0], start[2], start[0], start[1], end[1])
