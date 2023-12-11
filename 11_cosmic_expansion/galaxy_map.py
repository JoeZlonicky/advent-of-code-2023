import itertools

type MapPos = tuple[int, int]


class GalaxyMap:
    GALAXY_CHAR = '#'

    def __init__(self, width, height, galaxies: list[MapPos]):
        self.width = width
        self.height = height
        self.galaxies = galaxies

    def get_galaxy_pairs(self) -> list[tuple[MapPos, MapPos]]:
        return list(itertools.combinations(self.galaxies, 2))

    @staticmethod
    def distance_between_positions(p1: MapPos, p2: MapPos) -> int:
        x_diff = abs(p2[0] - p1[0])
        y_diff = abs(p2[1] - p1[1])
        return x_diff + y_diff

    @classmethod
    def from_file(cls, file_name, expansion_multiplier=1):
        with open(file_name) as f:
            rows = [line.strip() for line in f]
            rows = [row for row in rows if row != '']

            width, height = len(rows[0]), len(rows)
            galaxies = [(x, y) for y in range(height) for x in range(width) if rows[y][x] == cls.GALAXY_CHAR]

            if expansion_multiplier == 1:
                return cls(width, height, galaxies)

            return cls.expanded(width, height, galaxies, expansion_multiplier)

    @classmethod
    def expanded(cls, width, height, galaxies, expansion_multiplier):
        expanded_columns = []
        expanded_rows = []
        expansion_offset = expansion_multiplier - 1

        for y in range(height):
            if any(galaxy[1] == y for galaxy in galaxies):
                continue
            expanded_rows.append(len(expanded_rows) * expansion_offset + y)

        for x in range(width):
            if any(galaxy[0] == x for galaxy in galaxies):
                continue
            expanded_columns.append(len(expanded_columns) * expansion_offset + x)

        expanded_galaxies = []
        for galaxy in galaxies:
            expanded_x, expanded_y = galaxy
            for row in expanded_rows:
                if expanded_y > row:
                    expanded_y += expansion_offset
            for column in expanded_columns:
                if expanded_x > column:
                    expanded_x += expansion_offset
            expanded_galaxies.append((expanded_x, expanded_y))

        expanded_width = width + len(expanded_columns) * expansion_offset
        expanded_height = height + len(expanded_rows) * expansion_offset
        return cls(expanded_width, expanded_height, expanded_galaxies)
