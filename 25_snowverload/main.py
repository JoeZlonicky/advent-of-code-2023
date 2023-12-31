from graph import Graph
from math import prod

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    graph = Graph()
    graph.add_nodes_from_file(INPUT_FILE_PATH)

    # Finding the most travelled edges *usually* gives the right result, but can get messed up on ties
    # So... we just do it until it works
    # Is this hacky? Yes. Does it work? Also yes.
    while True:
        removed_edges = []
        for i in range(3):
            edge = graph.find_most_travelled_edge_on_average()
            graph.remove_edge(edge[0], edge[1])
            removed_edges.append(edge)

        groups = graph.count_groups()
        if len(groups) == 2:
            break

        for edge in removed_edges:
            graph.add_edge(edge[0], edge[1])

    print(prod(groups))


if __name__ == '__main__':
    main()
