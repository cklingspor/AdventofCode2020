import networkx as nx
import utils
from matplotlib import pyplot as plt


class Node:

    def __init__(self):
        self.color = ''
        self.children = []
        self.parents = []

    def add_child(self, child: str):
        self.children.append(child)

    def add_color(self, color: str):
        self.color = color

    def get_color(self):
        return self.color

    def add_parent(self, parent: str):
        self.parents.append(parent)

    def get_parents(self):
        return self.parents

    def get_tuple_list(self):
        list = []
        for child in self.children:
            list.append((self.color, child))

        return list

    def has_child(self):
        return True if self.children else False


class Subsentence():

    def __init__(self, sentence):
        self.sentence = sentence
        self.num = 0
        self.color = 'empty'

    def parse_into_schema(self):
        if self.sentence != 'no other bags.':
            splitted = self.sentence.split()
            self.num = int(splitted[0])
            self.color = splitted[1] + ' ' + splitted[2]

    def get_color(self):
        return self.color

    def has_child(self):
        return True if self.color != 'empty' else False


def parse_sentences_to_nodes(input: list):
    nodes = {}

    for line in input:
        node = Node()
        splitted = line.split('bags contain', 1)
        node.add_color(splitted[0].strip())
        for string in splitted[1].strip().split(','):
            subsentence = Subsentence(string)
            subsentence.parse_into_schema()
            if subsentence.has_child():
                node.add_child(subsentence.get_color())
        if node.has_child():
            nodes[node.get_color()] = node

    return nodes


def create_graph(nodes: dict):
    graph = nx.DiGraph()
    for key in nodes.keys():
        graph.add_edges_from(nodes[key].get_tuple_list())

    return graph


def plot_graph(graph):
    plt.tight_layout()
    nx.draw_networkx(graph, arrows=True)
    plt.show()


def get_all_predecessors(graph, target):
    predecessors = []

    for path in get_all_paths(graph=graph, target=target):
        for elem in path[:-1]:
            if elem not in predecessors:
                predecessors.append(elem)

    return predecessors


def get_all_paths(graph, target):

    paths = []
    roots = get_roots(graph=graph)
    for root in roots:
        for path in nx.all_simple_paths(graph, root, target):
            paths.append(path)

    return paths


def get_roots(graph):
    return [n for n, d in graph.in_degree() if d == 0]


if __name__ == '__main__':
    input = utils.read_file(unc_path='./test_input.txt')
    input = utils.read_file(unc_path='./input.txt')
    nodes = parse_sentences_to_nodes(input=input)
    graph = create_graph(nodes=nodes)
    #plot_graph(graph=graph)
    predecessors = get_all_predecessors(graph=graph, target=nodes['shiny '
                                                                  'gold'].get_color())
    print('The node {} has {} predecessors.'.format("shiny gold",
                                                    len(predecessors)))


