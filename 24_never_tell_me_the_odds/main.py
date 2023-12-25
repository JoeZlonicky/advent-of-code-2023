from intersection import count_ray_intersections
from ray import parse_rays_from_file

INPUT_FILE_PATH = './inputs/puzzle.txt'
MIN_XY = 200000000000000
MAX_XY = 400000000000000


def main():
    rays = parse_rays_from_file(INPUT_FILE_PATH)
    n_intersections = count_ray_intersections(rays, lambda p: MIN_XY <= p[0] <= MAX_XY and MIN_XY <= p[1] <= MAX_XY)
    print(f'(Part 1) # ray intersections: {n_intersections}')


if __name__ == '__main__':
    main()
