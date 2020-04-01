from collections import defaultdict, deque
from typing import DefaultDict, List, Deque


class Graph:
    """A class representing a graph"""

    def __init__(self) -> None:
        """Constructor (sort of)"""
        self.graph: DefaultDict[int, List[int]] = defaultdict(list)

        # We'll fill this using bfs algorithm
        self.bfs: List[int] = []

    def add_edge(self, index, vertex) -> None:
        """Add edge to graph"""
        self.graph[index].append(vertex)

    def bfs_algorithm(self, starting_vertex) -> List[int]:
        """Breadth-First Search - BFS algorithm"""

        # Mark visited vertices
        visited_vertices: List[bool] = [False] * len(self.graph)

        # Create a queue for the algorithm
        vertices_queue: Deque[int] = deque()

        # The starting vertex is enqueued and marked as visited
        vertices_queue.append(starting_vertex)
        visited_vertices[starting_vertex] = True

        while vertices_queue:
            # Dequeue the starting vertex and add it to
            # the BFS list
            checking_vertex = vertices_queue.popleft()
            self.bfs.append(checking_vertex)

            # Loop through the checking vertex's adjacent vertices
            for adjacent_vertex in self.graph[checking_vertex]:
                # Make sure we won't enqueue visited vertices
                if visited_vertices[adjacent_vertex]:
                    continue

                # Enqueue adjacent vertex and mark it as visited
                vertices_queue.append(adjacent_vertex)
                visited_vertices[adjacent_vertex] = True

        return self.bfs


def main() -> None:
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    bfs = g.bfs_algorithm(2)
    print(bfs)


if __name__ == "__main__":
    main()
