from __future__ import annotations
import math
from typing import Dict, List, Optional


class Vertex:
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors: Dict[str, float] = {}

    def add_neighbor(self, neighbor: Vertex, weight: float = math.inf) -> None:
        self.neighbors[neighbor.name] = weight

    def __repr__(self) -> str:
        neighbors = ','.join([n for n in self.neighbors])
        return f'{self.name}({neighbors})'


class Graph:
    def __init__(self) -> None:
        self.graph: Dict[str, Vertex] = {}
        self.costs: Dict[str, float] = {}
        self.parents: Dict[str, str] = {}
        self.visited_vertices: List[Vertex] = []

    def add_vertex(self, vertex: Vertex) -> None:
        self.graph[vertex.name] = vertex

    def set_starting_data(self, vertex: Vertex):
        for name, cost in vertex.neighbors.items():
            self.costs[name] = cost
            self.parents[name] = vertex.name

    def dijkstra_algorithm(self, start: Vertex, end: Vertex) -> None:
        self.visited_vertices.clear()
        self.set_starting_data(start)

        if start == end:
            return

        if not self.graph.get(start.name) or not self.graph.get(end.name):
            raise ValueError('Start or end vertex not in graph')

        lowest_cost_neighbor = self.get_lowest_cost()

        while lowest_cost_neighbor:
            for neighbor, cost in lowest_cost_neighbor.neighbors.items():
                if cost < self.costs.get(neighbor, math.inf):
                    self.costs[neighbor] = cost + \
                        self.costs[lowest_cost_neighbor.name]
                    self.parents[neighbor] = lowest_cost_neighbor.name

            self.visited_vertices.append(lowest_cost_neighbor)

            if lowest_cost_neighbor == end:
                break

            lowest_cost_neighbor = self.get_lowest_cost()

    def get_shortest_path(self, start: Vertex, end: Vertex):
        self.dijkstra_algorithm(start, end)

        shortest_path = [end]
        vertex: str = self.parents[end.name]

        for _ in enumerate(self.parents):
            shortest_path.append(self.graph[vertex])
            vertex = self.parents.get(vertex, '')

        return shortest_path[::-1]

    def get_lowest_cost(self) -> Optional[Vertex]:
        lowest_cost: float = math.inf
        vertex_with_lowest_cost = None

        for name, cost in self.costs.items():
            vertex = self.graph[name]
            if cost < lowest_cost and vertex not in self.visited_vertices:
                lowest_cost = cost
                vertex_with_lowest_cost = vertex
        return vertex_with_lowest_cost


if __name__ == "__main__":
    graph = Graph()

    inicio = Vertex('inicio')
    a = Vertex('a')
    b = Vertex('b')
    fim = Vertex('fim')

    inicio.add_neighbor(neighbor=a, weight=6)
    inicio.add_neighbor(neighbor=b, weight=2)
    a.add_neighbor(neighbor=fim, weight=1)
    b.add_neighbor(neighbor=a, weight=3)
    b.add_neighbor(neighbor=fim, weight=5)

    graph.add_vertex(vertex=inicio)
    graph.add_vertex(vertex=a)
    graph.add_vertex(vertex=b)
    graph.add_vertex(vertex=fim)

    shortest_path = graph.get_shortest_path(start=inicio, end=fim)
    print(shortest_path)
