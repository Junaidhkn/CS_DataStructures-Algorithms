# Graphs have vertex(or node),vertices or nodes in plural,and connection between them are called edge(or connection).


# Representation of Graphs:
# 1) Adjacency Matrix-
# Space complexity-Big(O) : O(|V|^2), where V is number of vertices, as it also stores the values that each vertex is not connected to.


# 2) Adjacency List - Representation in the form of Dictionary
#     Space complexity-Big(O) :  O(|V|+|E|), where v is number of vertices and E is number of edges


# Time Complexity : Big O
#                       Adjacency Matrix     |      Adjacency List
# Adding a Vertex:         O(|V|^2)                     O(1)
# Adding an Edge:            O(1)                       O(1)
# Remove the Edge:           O(1)                       O(|E|)
# Remove a Vertex:          O(|V|^2)                    O(|V|+|E|)


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
        # if all(v in self.adjacency_list for v in (vertex1, vertex2)):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])





my_graph = Graph()

my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_vertex('c')
my_graph.add_edge('a','b')

my_graph.print_graph()


