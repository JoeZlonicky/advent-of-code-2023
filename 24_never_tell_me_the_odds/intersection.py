from typing import Callable
from ray import Ray

type Pos = tuple[float, float, float]

NO_INTERSECTION: Pos = (-1, -1, -1)


def count_ray_intersections(rays: list[Ray], count_intersection_predicate: Callable[[Pos], bool]):
    intersection_count = 0
    for i, ray in enumerate(rays):
        for second_ray in rays[i + 1:]:
            intersection = get_ray_intersection(ray, second_ray)
            if intersection == NO_INTERSECTION:
                continue

            if count_intersection_predicate(intersection):
                intersection_count += 1
    return intersection_count


# https://stackoverflow.com/questions/2931573/determining-if-two-rays-intersect
def get_ray_intersection(ray1: Ray, ray2: Ray) -> Pos:
    dx = ray2.point[0] - ray1.point[0]
    dy = ray2.point[1] - ray1.point[1]
    det = ray2.direction[0] * ray1.direction[1] - ray2.direction[1] * ray1.direction[0]
    if det == 0:
        return NO_INTERSECTION

    u = (dy * ray2.direction[0] - dx * ray2.direction[1]) / det
    v = (dy * ray1.direction[0] - dx * ray1.direction[1]) / det

    if u >= 0 and v >= 0:
        x = ray1.point[0] + ray1.direction[0] * u
        y = ray1.point[1] + ray1.direction[1] * u
        z = ray1.point[2] + ray1.direction[2] * u
        return x, y, z

    return NO_INTERSECTION
