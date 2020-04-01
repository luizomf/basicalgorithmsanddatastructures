from collections import defaultdict, deque
from typing import DefaultDict, List, Deque, Set
from pprint import pprint


class Graph:
    """A class representing a graph"""

    def __init__(self) -> None:
        """Constructor (sort of)"""
        self.graph: DefaultDict[str, List[str]] = defaultdict(list)

        # We'll fill this using bfs algorithm
        self.bfs: List[str] = []

    def add_edge(self, key, vertex) -> None:
        """Add edge to graph"""
        self.graph[key].append(vertex)

    def bfs_algorithm(self, starting_vertex: str) -> List[str]:
        """Breadth-First Search - BFS algorithm"""

        # Clear bfs attribute
        self.bfs.clear()

        # Set of visited vertices
        visited_vertices: Set[str] = set()

        # Create a queue for the algorithm
        vertices_queue: Deque[str] = deque()

        # The starting vertex is enqueued and marked as visited
        vertices_queue.append(starting_vertex)
        visited_vertices.add(starting_vertex)

        while vertices_queue:
            # Dequeue the starting vertex and add it to
            # the BFS list
            checking_vertex = vertices_queue.popleft()
            self.bfs.append(checking_vertex)

            # Loop through the checking vertex's adjacent vertices
            for adjacent_vertex in self.graph[checking_vertex]:
                # Make sure we won't enqueue visited vertices
                if adjacent_vertex in visited_vertices:
                    continue

                # Enqueue adjacent vertex and mark it as visited
                vertices_queue.append(adjacent_vertex)
                visited_vertices.add(adjacent_vertex)

        return self.bfs


def main() -> None:
    sample_graph = Graph()
    sample_graph.add_edge('A', 'F')
    sample_graph.add_edge('B', 'E')
    sample_graph.add_edge('B', 'D')
    sample_graph.add_edge('C', 'H')
    sample_graph.add_edge('D', 'G')
    sample_graph.add_edge('E', 'H')
    sample_graph.add_edge('E', 'G')
    sample_graph.add_edge('F', 'G')
    sample_graph.add_edge('F', 'I')
    sample_graph.add_edge('F', 'L')
    sample_graph.add_edge('G', 'J')
    sample_graph.add_edge('H', 'M')
    sample_graph.add_edge('I', 'K')
    sample_graph.add_edge('J', 'K')
    sample_graph.add_edge('K', 'N')
    sample_graph.add_edge('L', 'K')
    sample_graph.add_edge('L', 'O')
    sample_graph.add_edge('M', 'N')
    sample_graph.add_edge('N', 'P')
    sample_graph.add_edge('O', 'N')
    sample_graph.add_edge('P', 'P')

    pprint(sample_graph.graph)

    bfs_starting_from_a = sample_graph.bfs_algorithm('A')
    pprint(bfs_starting_from_a)
    # ['A', 'F', 'G', 'I', 'L', 'J', 'K', 'O', 'N', 'P']

    bfs_starting_from_b = sample_graph.bfs_algorithm('B')
    pprint(bfs_starting_from_b)
    # ['B', 'E', 'D', 'H', 'G', 'M', 'J', 'N', 'K', 'P']

    bfs_starting_from_c = sample_graph.bfs_algorithm('C')
    pprint(bfs_starting_from_c)
    # ['C', 'H', 'M', 'N', 'P']


if __name__ == "__main__":
    main()
