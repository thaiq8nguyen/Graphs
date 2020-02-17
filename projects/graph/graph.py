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
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #1. Create an empty queue
        q = Queue()
        #2. Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        #3. Create an empty set to store visited nodes
        visited = set()
        #4. While the queue is not empty
        while q.size() > 0:
        #5. Dequeue, the first vertex
            vertex = q.dequeue()
        #6. Check if it's been visited
            if vertex not in visited:
        #7. If is has not been visited
            #8. Mark it as visited
                print(vertex)
                visited.add(vertex)
            #9. Then add all neighbors to to the back of the Queue
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)
        print("==END BFT==")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # The algorithm is the same as in BFT but we are using a Stack
        #1. Create an empty stack
        s = Stack()
        #2. Add the starting vertex_id to the stack
        s.push(starting_vertex)
        #3. Create an empty set to store the visited nodes
        visited = set()
        #4. While the stack is not empty
        while s.size() > 0:
            #5. Pop the first vertex
            vertex = s.pop()
            #6. Check if it's been visited
            if vertex not in visited:
                
                visited.add(vertex)
                print(vertex)
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)


        print("==END DFT==")
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        def dft_recur(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            print(vertex)
            for v in self.vertices[vertex]:
                dft_recur(v)
        
        dft_recur(starting_vertex)

        print("==END DFT USING RECURSIVE==")

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #1. Create an empty queue and push a path to the starting vertex_id
        q = Queue()
        q.enqueue([starting_vertex])
        #2. Create a set to store visited vertices
        visited = set()
        #3. While the queue is not empty
        while q.size() > 0:
            #4. dequeue the first path
            last_path = q.dequeue()
            #5. Grab the last vertex from the path
            last_vertex = last_path[-1]
            #6. If that vertex has not been visited:
            if last_vertex not in visited:
            #7. Check if it's the destination
                if last_vertex == destination_vertex:
                    
            #8. If so:
                    #9. Return path
                    return last_path
                #9. Mark is as visited
                visited.add(last_vertex)
                #10. Add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                #11. Copy the path
                    new_path = [*last_path]

                #12. Append the neighbor to the back of the queue
                    new_path.append(v)
                    q.enqueue(new_path)
        print("==END BFS==")


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #1. Create an empty stack and push a path to the starting vertex_id
        s = Stack()
        s.push([starting_vertex])
        #2. Create a set to store visited vertices
        visited = set()
        #3. While the stack is not empty
        while s.size() > 0:
            #4. dequeue the first path
            last_path = s.pop()
            #5. Grab the last vertex from the path
            last_vertex = last_path[-1]
            #6. If that vertex has not been visited:
            if last_vertex not in visited:
            #7. Check if it's the destination
                if last_vertex == destination_vertex:
                    
            #8. If so:
                    #9. Return path
                    return last_path
                #9. Mark is as visited
                visited.add(last_vertex)
                #10. Add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                #11. Copy the path
                    new_path = [*last_path]

                #12. Append the neighbor to the back of the queue
                    new_path.append(v)
                    s.push(new_path)
        print("==END DFS==")

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        path = []

        def dfs_recur(starting_vertex, destination_vertex, path):
            if starting_vertex == destination_vertex:
                path.append(starting_vertex)
                return path
            if starting_vertex in visited:
                return path
            visited.add(starting_vertex)
            for v in self.vertices[starting_vertex]:
                if destination_vertex in dfs_recur(v, destination_vertex, path):
                    path.append(starting_vertex)
                    return path
            return path

        ret_path = dfs_recur(starting_vertex, destination_vertex, path)
        ret_path.reverse()

        return ret_path

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
