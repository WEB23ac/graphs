"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('Vertext does not exist.')

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge between two vertices.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError('Vertext does not exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('Vertext does not exist.')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a Set to store the vertices
        visited = set()
        # While the Queue is not empty:
        while q.size() > 0:
            # Dequeue first vertex
            curr_vertex = q.dequeue()
            # Check if the curr_vertex has not been vistited
            if curr_vertex not in visited:
               # print curr_vertex
                print(curr_vertex)
                # add to visited
                visited.add(curr_vertex)
                # enqueue each of its neighbors
                for neighbor in self.get_neighbors(curr_vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push staring_vertex to stack
        s.push(starting_vertex)
        # Create a visited set
        visited = set()
        # While the Stack is not empty
        while s.size() > 0:
            # Pop first vertex
            curr_vertex = s.pop()
            # check if curr_vertext has not been visited
            if curr_vertex not in visited:
                # print curr_vertex
                print(curr_vertex)
                # add to visited
                visited.add(curr_vertex)
                # and push neighbors to the stack
                for neighbor in self.get_neighbors(curr_vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a Queue
        q = Queue()
        # Enqueue a Path to the starting_vertex
        q.enqueue([starting_vertex])

        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first Path
            curr_path = q.dequeue()
            # Retrieve last entry in path
            last_vtx = curr_path[-1]
            print('curr_path', curr_path)

            print('last_vtx', last_vtx)
            # Check if it's been visited
            if last_vtx not in visited:
                visited.add(last_vtx)
                # if last_vtx is the target, return the current path
                if last_vtx == destination_vertex:
                    print(curr_path)
                    return curr_path

                # Find neighbors of last_vtx and create copies of the current_path and adding each neighbor to a copy
                for neighbor in self.get_neighbors(last_vtx):
                    next_path = curr_path.copy()
                    next_path.append(neighbor)
                    print('next_path', next_path)
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a Stack
        s = Stack()
        # Push the current path to the Stack
        s.push([starting_vertex])
        # Create set of visited vertices
        visited = set()
        # While the queue is not empty,
        while s.size() > 0:
            # Pop the last path from the stack
            curr_path = s.pop()
            # Retrieve the last entry in the stack
            curr_vtx = curr_path[-1]
            # Check if curr_vtx has not been visited
            if curr_vtx not in visited:
                # Add to visited
                visited.add(curr_vtx)

            # Check if last_entry is the target
                # If so, return the current path
                if curr_vtx == destination_vertex:
                    print(curr_path)
                    return curr_path
            # For each neighbor of current entry
                for neighbor in self.get_neighbors(curr_vtx):
                    next_path = curr_path.copy()
                    next_path.append(neighbor)
                    s.push(next_path)
                # create copy of current path
                # append neighbor to copy
                # push copy to stack

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, curr_path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print('dfs_r start')
        if visited is None:
            visited = set()
        if curr_path is None:
            curr_path = [starting_vertex]
        curr_vtx = curr_path[-1]
        print('visited', visited)
        print('curr_path', curr_path)
        print('curr_vtx', curr_vtx)

        if curr_vtx not in visited:
            visited.add(curr_vtx)
            if curr_vtx == destination_vertex:
                print('dfs_rec', curr_path)
                return curr_path
            for neighbor in self.get_neighbors(curr_vtx):
                next_path = curr_path.copy()
                next_path.append(neighbor)
                self.dfs_recursive(
                    starting_vertex, destination_vertex, visited, next_path)


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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

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
