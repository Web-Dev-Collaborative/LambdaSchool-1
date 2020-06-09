from util import Queue, Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # add a key/vertice:
        # '2': set(),
        # '3': {'0'}
        self.vertices[vertex_id] = set()
        return self.vertices

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            print(f"There is no vertex {v1}.  Try again!")

    def get_neighbors(self, vertex_id):
        # Get all neighbors (edges) of a vertex.
        if vertex_id in self.vertices:
            return self.vertices.get(vertex_id)
        else:
            return "This vertex has no neighbors."

    def bft(self, starting_vertex):
        # Write a function within your Graph class that takes a starting node as an argument, then performs BFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
        visited = ""
        if starting_vertex in self.vertices.keys():
            print(starting_vertex)
            visited = visited + str(starting_vertex)
        for vertex in self.vertices:
            if vertex != starting_vertex and (vertex - starting_vertex == 1):
                print(str(vertex))
                visited = visited + ", " + str(vertex)
                starting_vertex += 1
        return visited

    def dft(self, starting_vertex):
        # Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
        # {1: 2, 2: 3, 3: 5, 4: 6, 5: 3, 6: 3, 7: 6}
        # start with starting_vertex = current_vertex
        visited = []
        current_vertex = starting_vertex
        visited.append(current_vertex)
        for vertex in self.vertices:
            if vertex == current_vertex:
                if current_vertex in self.vertices.keys():
                    print(current_vertex)
                    visited.append(current_vertex)
                # get value of current_vertex as next_vertex
                next_vertex = self.vertices.get(current_vertex)
                # get value of next_vertex as current_vertex
                current_vertex = next_vertex
        # first one NOT visited, add as current_vertex
        for vertex in self.vertices:
            if vertex not in visited:
                current_vertex = vertex
                break
        # repeat previous loop starting with new current_vertex
        for vertex in self.vertices:
            if vertex not in visited:
                if vertex == current_vertex:
                    if current_vertex in self.vertices.keys():
                        print(current_vertex)
                    # get value of current_vertex as next_vertex
                    next_vertex = self.vertices.get(current_vertex)
                    visited.append(current_vertex)
                    # get value of next_vertex as current_vertex
                    current_vertex = next_vertex
        # first one NOT visited, add as current_vertex
        for vertex in self.vertices:
            if vertex not in visited:
                current_vertex = vertex
                break
        # repeat previous loop starting with new current_vertex
        for vertex in self.vertices:
            if vertex not in visited:
                if vertex == current_vertex:
                    if current_vertex in self.vertices.keys():
                        print(current_vertex)
                    # get value of current_vertex as next_vertex
                    next_vertex = self.vertices.get(current_vertex)
                    visited.append(current_vertex)
                    # get value of next_vertex as current_vertex
                    current_vertex = next_vertex

    def dft_recursive(self, starting_vertex, visited=[]):
        # Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT using recursion. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.

        # Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
        # {1: 2, 2: 3, 3: 5, 4: 6, 5: 3, 6: 3, 7: 6}
        # start with starting_vertex = current_vertex
        array_check = []
        current_vertex = starting_vertex
        visited.append(current_vertex)
        for vertex in self.vertices:
            if vertex == current_vertex:
                if current_vertex in self.vertices.keys():
                    print(current_vertex)
                    visited.append(current_vertex)
                # get value of current_vertex as next_vertex
                next_vertex = self.vertices.get(current_vertex)
                # get value of next_vertex as current_vertex
                current_vertex = next_vertex
        # first one NOT visited, add as current_vertex
        for vertex in self.vertices:
            if vertex not in visited:
                current_vertex = vertex
                self.dft_recursive(current_vertex, visited)
            else:
                array_check.append(vertex)
        if array_check == visited:
            return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs BFS. Your function should return the shortest path from the start node to the destination node. Note that there are multiple valid paths.

        tp = Queue()
        visited = []
        path = []
        # add starting vertex to the queue
        current_vertex = starting_vertex
        tp.enqueue(current_vertex)
        path.append(current_vertex)
        visited.append(current_vertex)
        # loop while queue not empty (while queue.size())
        print("vertices = " + str(self.vertices))
        while tp.size():
            print("current vertex = " + str(current_vertex))
            edges = self.get_neighbors(current_vertex)
            print("current vertex's edges = " + str(edges))
            # removes current item from queue
            tp.dequeue()
            # get value (edges) of current vertex
            for edge in edges:
                print('edge in loop = ' + str(edge))
                visited.append(edge)
                path.append(edge)
                # if any edges are destination, add it to path and return path
                if edge == destination_vertex:
                    print("you're home!")
                    return path
                # if edge is not destination:
                else:
                    subedges = self.get_neighbors(edge)
                    print("current vertex's subedges = " + str(subedges))
                    for subsubedge in subedges:
                        print("edge = " + str(edge))
                        print("subsubedge = " + str(subsubedge))
                        print("get subsubedge's neighbors = " + str(subsubedge))
                        visited.append(subsubedge)
                        subsubsubedges = self.get_neighbors(subsubedge)
                        if subsubedge == destination_vertex:
                            path.append(subsubedge)
                            return path
                        if destination_vertex in subsubsubedges:
                            path.append(subsubedge)
                            path.append(destination_vertex)
                            print(path)
                            return path
        # return path
        print(path)
        return path
            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs DFS. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node. Note that there are multiple valid paths.


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs DFS using recursion. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node. Note that there are multiple valid paths.
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    graph.add_edge(0, 4)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
