import sys, heapq

class Vertex:
    '''
        Node in a Graph
    '''
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize
        self.adjancency_list = []

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        return self.min_distance < other.min_distance

class Edge:
    '''
        Edge b/w 2 Vertices of a Graph
    '''
    def __init__(self, vertex1, vertex2):
        self.v1 = vertex1
        self.v2 = vertex2

def get_shortest_path(vertex_list, start_vertex):
    heap = []
    start_vertex.min_distance = 0
    heapq.heappush(heap, start_vertex)

    while len(heap) > 0:
        current_vertex = heapq.heappop(heap)
        for edge in current_vertex.adjancency_list:
            u = edge.v1
            v = edge.v2

            new_distance = u.min_distance + 1
            if new_distance < v.min_distance:
                v.predecessor = u
                v.min_distance = new_distance
                heapq.heappush(heap, v)

def get_shortest_path_to(target_vertex):
    print("Shortest path to ", target_vertex.name, " is ", target_vertex.min_distance)

    node = target_vertex
    while node is not None:
        print("%s -> " % node.name)
        node = node.predecessor

n1, n2, n3 = Vertex('A'), Vertex('B'), Vertex('C')
e1, e2, e3 = Edge(n1, n2), Edge(n2, n3), Edge(n1, n3)

n1.adjancency_list.append(e1)
n1.adjancency_list.append(e2)
n2.adjancency_list.append(e1)
n2.adjancency_list.append(e2)
n3.adjancency_list.append(e2)
n3.adjancency_list.append(e3)

vertex_list = (n1, n2, n3)
source = int(input())
dest = int(input())
get_shortest_path(vertex_list, vertex_list[source])
get_shortest_path_to(vertex_list[dest])