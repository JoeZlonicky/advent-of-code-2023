from typing import Callable
from ray import Ray
import numpy as np

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


def get_ray_that_hits_all(rays: list[Ray]) -> Ray:
    # First we need to solve for x, dx, y, and dy
    # x + t_i * dx = x_i + t_i * dx_i
    # t_i * dx - t_i * dx_i = x_i - x
    # t_i = (x_i - x) / (dx - dx_i)
    # (x_i - x) / (dx - dx_i) = (y_i - y) / (dy - dy_i)
    # (x_i - x)(dy - dy_i) + (y - y_i)(dx - dx_i) = (equation for second ray k)
    # Some moving around...
    # x*(dy_i-dy_k) + y*(dx_k-dx_i) + dx*(y_k-y_i) + dy*(x_i-x_k) = x_i*dy_i - x_k*dy_k - y_i*dx_i + y_k*dx_k
    # A linear equation with 4 unknowns!

    rows = []
    rhs = []
    r1, r2, r3, r4, r5 = rays[0], rays[1], rays[2], rays[3], rays[4]
    for i, k in [(r1, r2), (r2, r3), (r3, r4), (r4, r5)]:
        a_x, a_y = i.point[0:2]
        b_x, b_y = k.point[0:2]
        a_dx, a_dy = i.direction[0:2]
        b_dx, b_dy = k.direction[0:2]

        rows.append([a_dy - b_dy, b_dx - a_dx,
                     b_y - a_y, a_x - b_x])
        rhs.append(-b_x * b_dy + a_x * a_dy + b_y * b_dx - a_y * a_dx)

    coefficients = np.linalg.solve(np.array(rows), np.array(rhs))
    x, y, dx, dy = [n for n in coefficients]

    # Now we can solve for z, dz using the following equation for two different rays:
    # z + dz * t_i = z_i + t_i * dz_i

    rows = []
    rhs = []
    for r in [r1, r2]:
        t = (r.point[0] - x) / (dx - r.direction[0])
        rows.append([1, t])
        rhs.append(r.point[2] + t * r.direction[2])

    coefficients = np.linalg.solve(np.array(rows), np.array(rhs))
    z, dz = [round(n) for n in coefficients]
    
    x, y, dx, dy = [round(n) for n in [x, y, dx, dy]]

    return Ray((x, y, z), (dx, dy, dz))
