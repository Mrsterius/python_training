class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __repr__(self):
        return str(self.value)
class Graph:

    def __init__(self):
        self.vertices = []

    def find(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def add_vertex(self, value):
        if not self.find(value):
            self.vertices.append(Vertex(value))

    def add_edge(self, source, target):
        source_v = self.find(source)
        target_v = self.find(target)

        if source_v and target_v:
            source_v.neighbours.append(target_v)
            target_v.neighbours.append(source_v)

    def depth_first_traversal(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def breadth_first_traversal(self, source=None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def connected_comp(self):
        queue = list()
        visited = set()
        conn_comp = list()
        for vertex in self.vertices:

            if vertex not in visited:
                comp = set()
                queue.append(vertex)
                visited.add(vertex)

                while len(queue) > 0:
                    vertex = queue.pop(0)
                    comp.add(vertex)

                    for neighbour in vertex.neighbours:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                conn_comp.append(comp)
        return conn_comp

    def is_bipartite(self):
        queue = list()
        visited = set()
        red = set()
        green = set()
        for vertex in self.vertices:
            if vertex not in visited:

                queue.append(vertex)
                visited.add(vertex)
                red.add(vertex)
                while len(queue) > 0:
                    vertex = queue.pop(0)

                    for neighbour in vertex.neighbours:

                        # not visited items are to be divided
                        if neighbour not in visited:
                            if vertex in red:
                                green.add(neighbour)
                            if vertex in green:
                                red.add(neighbour)

                            visited.add(neighbour)
                            queue.append(neighbour)
                        # visited items are to be verified
                        else:
                            if vertex in red and neighbour in red:
                                return False
                            if vertex in green and neighbour in green:
                                return False
        return True
    def depth_first_search(self, source, target):
        vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            vertex = stack.pop()

            if vertex.value == target:
                return True

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return False

    def breadth_first_search(self, source, target):
        vertex = self.find(source)

        queue = list()
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)

            if vertex.value == target:
                return True

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False

    def display(self):

        for vertex in self.vertices:
            print(vertex, end=" : ")

            # way 1
            print(" , ".join([str(neighbour) for neighbour in vertex.neighbours]))
            #way 2
            # for neighbour in vertex.neighbours:
            #     print(neighbour, end= " ,")
            # print()
if __name__ == "__main__":

    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("D", "E")
    graph.add_edge("E", "F")

    graph.display()
    print(graph.connected_comp())
    # graph.depth_first_traversal()
