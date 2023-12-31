from collections import defaultdict
import heapq
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
                self.add_edge(left_label, right_label)

    def remove_edge(self, node_a, node_b):
        self.edges[node_a].remove(node_b)
        self.edges[node_b].remove(node_a)

    def add_edge(self, node_a, node_b):
        self.edges[node_a].add(node_b)
        self.edges[node_b].add(node_a)

    def find_most_travelled_edge_on_average(self, max_paths_to_test: int = 10) -> edge:
        edge_travel_count = defaultdict(lambda: 0)

        n_paths_to_test = min(len(self.nodes), max_paths_to_test)
        for start_node in random.choices(self.nodes, k=n_paths_to_test):
            shortest_path = self.shortest_path_to_furthest_node(start_node)
            for travelled_edge in shortest_path:
                edge_travel_count[tuple(travelled_edge)] += 1

        edges = list(edge_travel_count.keys())
        edges.sort(key=lambda x: edge_travel_count[x], reverse=True)
        return edges[0]

    def shortest_path_to_furthest_node(self, start_node: node) -> list[edge]:
        distances = defaultdict(lambda: inf)
        distances[start_node] = 0
        previous: dict[node, node] = {start_node: None}

        unvisited = []
        heap_entries = {}
        heapq.heapify(unvisited)
        for n in self.nodes:
            priority_pair = [distances[n], n]
            heapq.heappush(unvisited, priority_pair)
            heap_entries[n] = priority_pair

        while unvisited:
            _, current_node = heapq.heappop(unvisited)
            if current_node == 'REMOVED':
                continue

            distance_to_next = distances[current_node] + 1
            for connected in self.edges[current_node]:
                if distance_to_next >= distances[connected]:
                    continue

                distances[connected] = distance_to_next
                previous[connected] = current_node
                entry = heap_entries[connected]
                entry[1] = 'REMOVED'
                new_priority_pair = [distance_to_next, connected]
                heapq.heappush(unvisited, new_priority_pair)

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
