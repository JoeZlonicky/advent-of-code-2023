from graph import Graph
from math import prod

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    graph = Graph()
    graph.add_nodes_from_file(INPUT_FILE_PATH)

    for i in range(3):
        edge = graph.find_n_most_important_edges(1)[0]
        graph.edges[edge[0]].remove(edge[1])
        graph.edges[edge[1]].remove(edge[0])

    groups = graph.count_groups()
    print(prod(groups))


if __name__ == '__main__':
    main()
