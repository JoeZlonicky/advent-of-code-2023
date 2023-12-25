type n3 = tuple[float, float, float]


class Ray:
    def __init__(self, point: n3, direction: n3):
        self.point = point
        self.direction = direction

    @classmethod
    def from_line(cls, line):
        pos, d = line.split('@')
        pos = [float(i) for i in pos.split(',')]
        d = [float(i) for i in d.split(',')]
        return cls((pos[0], pos[1], pos[2]), (d[0], d[1], d[2]))


def parse_rays_from_file(file_path) -> list[Ray]:
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    return [Ray.from_line(line) for line in lines if line]
