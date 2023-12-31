from collections import defaultdict
from math import inf
import random

type node = str
type edge = set[str, str]


class Graph:
    def __init__(self):
        self.nodes: list[node] = []
        self.edges = defaultdict(lambda: set())

    def add_nodes_from_file(self, file_path):
        with open(file_path) as f:
            lines = [line.strip() for line in f]

        lines = [line for line in lines if line]
        for line in lines:
            left_label, right = [side.strip() for side in line.split(':')]
            right_labels = [label for label in right.split()]

            for label in [left_label] + right_labels:
                if label in self.nodes:
                    continue
                self.nodes.append(label)

            for right_label in right_labels:
                self.edges[left_label].add(right_label)
                self.edges[right_label].add(left_label)

    # Important is defined as having the most traversals from paths of nodes that are the furthest from each other
    def find_n_most_important_edges(self, n: int = 1, max_paths_to_test: int = 25) -> list[edge]:
        edge_travel_count = defaultdict(lambda: 0)

        n_paths_to_test = min(len(self.nodes), max_paths_to_test)
        for start_node in random.choices(self.nodes, k=n_paths_to_test):
            # Go to the furthest, and then from the furthest go to the furthest from that to get a long path that
            # *should* go through a bridge, at least for the puzzle input
            path_to_furthest = self.shortest_path_to_furthest_node(start_node)
            new_start_node = tuple(path_to_furthest[-1])[0]
            shortest_path = self.shortest_path_to_furthest_node(new_start_node)
            for travelled_edge in shortest_path:
                edge_travel_count[tuple(travelled_edge)] += 1

        edges = list(edge_travel_count.keys())
        edges.sort(key=lambda x: edge_travel_count[x], reverse=True)
        return edges[:n]

    def shortest_path_to_furthest_node(self, start_node: node) -> list[edge]:
        distances = defaultdict(lambda: inf)
        distances[start_node] = 0
        previous: dict[node, node] = {start_node: None}

        unvisited = list(self.nodes)

        while unvisited:
            current = min(unvisited, key=lambda x: distances[x])
            unvisited.remove(current)

            distance_to_next = distances[current] + 1
            for connected in self.edges[current]:
                if distance_to_next >= distances[connected]:
                    continue

                distances[connected] = distance_to_next
                previous[connected] = current

        furthest = max(distances, key=lambda x: distances[x])

        path: list[edge] = []
        current = furthest
        while True:
            next_node = previous[current]
            path.append({current, next_node})

            if next_node == start_node:
                break
            current = previous[current]

        return path

    def count_groups(self) -> list[int]:
        visited = defaultdict(lambda: False)

        groups = []

        for n in self.nodes:
            if visited[n]:
                continue

            visited[n] = True
            count = 0

            stack = [n]
            while stack:
                current = stack.pop()
                count += 1
                for connected_node in self.edges[current]:
                    if visited[connected_node]:
                        continue

                    visited[connected_node] = True
                    stack.append(connected_node)

            groups.append(count)

        return groups
