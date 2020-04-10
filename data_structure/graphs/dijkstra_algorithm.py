from __future__ import annotations
import math
from typing import Dict, List, Optional
from pprint import pprint


class VertexNotInGraphError(ValueError):
    ...


class NotAVertexError(TypeError):
    ...


class Vertex:
    """A class representing a vertex"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors: Dict[str, float] = {}

    def add_neighbor(self, neighbor: Vertex, weight: float = math.inf) -> None:
        """ Add a neighbor and its weight """
        self.neighbors[neighbor.name] = weight

    def __repr__(self) -> str:
        return f'{self.name}'


class Graph:
    """A class representing a graph"""

    def __init__(self) -> None:
        self.graph: Dict[str, Vertex] = {}
        self._reset()

    def add_vertex(self, *vertex: Vertex) -> None:
        """Add a vertex or vertices separeted by comma to graph"""
        for v in vertex:
            self._check_vertex_type(v)
            self.graph[v.name] = v

    def _check_vertex_type(self, vertex: Vertex) -> None:
        if not isinstance(vertex, Vertex):
            raise NotAVertexError(f'{vertex} has to be of type Vertex')

    def _check_vertex_in_graph(self, vertex: Vertex) -> None:
        self._check_vertex_type(vertex)

        if not self.graph.get(vertex.name):
            raise VertexNotInGraphError(f'{vertex} not in graph')

    def _set_starting_data(self, vertex: Vertex):
        self._check_vertex_type(vertex)

        if vertex.name not in self.graph:
            raise VertexNotInGraphError(f'{vertex.name} not in graph')

        for name, cost in vertex.neighbors.items():
            self.costs[name] = cost
            self._parents[name] = vertex.name

    def _reset(self) -> None:
        self.costs: Dict[str, float] = {}
        self._parents: Dict[str, str] = {}
        self._visited_vertices: List[Vertex] = []

    def _dijkstra_algorithm(self, start: Vertex, end: Vertex) -> None:
        self._reset()
        self._set_starting_data(start)

        if start == end:
            return

        self._check_vertex_in_graph(start)
        self._check_vertex_in_graph(end)

        vertex = self._get_lowest_cost()

        while vertex:
            for neighbor, cost in vertex.neighbors.items():
                if cost < self.costs.get(neighbor, math.inf):
                    self.costs[neighbor] = cost + self.costs[vertex.name]
                    self._parents[neighbor] = vertex.name

            self._visited_vertices.append(vertex)

            if vertex == end:
                break

            vertex = self._get_lowest_cost()

    def get_shortest_path(self, start: Vertex, end: Vertex) -> List[Vertex]:
        # Get costs and parents
        self._dijkstra_algorithm(start, end)

        if not self._parents or not self.costs:
            return []

        if end.name not in self.costs:
            return []

        shortest_path = [end]
        vertex: str = self._parents.get(end.name, '')

        for _ in self._parents:
            if not vertex:
                continue

            shortest_path.append(self.graph[vertex])
            vertex = self._parents.get(vertex, '')

        return shortest_path[::-1]

    def _get_lowest_cost(self) -> Optional[Vertex]:
        lowest_cost: float = math.inf
        vertex_with_lowest_cost = None

        for name, cost in self.costs.items():
            vertex = self.graph.get(name)

            if not vertex:
                raise VertexNotInGraphError(f'{name} not in graph')

            if cost < lowest_cost and vertex not in self._visited_vertices:
                lowest_cost = cost
                vertex_with_lowest_cost = vertex
        return vertex_with_lowest_cost


if __name__ == "__main__":
    graph = Graph()

    va = Vertex('a')
    vb = Vertex('b')
    vc = Vertex('c')
    vd = Vertex('d')
    ve = Vertex('e')
    vf = Vertex('f')
    vg = Vertex('g')
    vh = Vertex('h')
    vi = Vertex('i')
    vj = Vertex('j')
    vk = Vertex('k')
    vl = Vertex('l')
    vm = Vertex('m')
    vn = Vertex('n')
    vo = Vertex('o')
    vp = Vertex('p')

    va.add_neighbor(neighbor=vb, weight=10)
    va.add_neighbor(neighbor=ve, weight=5)
    va.add_neighbor(neighbor=vf, weight=50)
    vb.add_neighbor(neighbor=vg, weight=6)
    vc.add_neighbor(neighbor=vd, weight=9)
    vd.add_neighbor(neighbor=vg, weight=20)
    vd.add_neighbor(neighbor=vh, weight=3)
    ve.add_neighbor(neighbor=vj, weight=15)
    vf.add_neighbor(neighbor=vg, weight=3)
    vf.add_neighbor(neighbor=vj, weight=6)
    vg.add_neighbor(neighbor=vk, weight=1)
    vg.add_neighbor(neighbor=vl, weight=15)
    vh.add_neighbor(neighbor=vl, weight=18)
    vi.add_neighbor(neighbor=vm, weight=16)
    vi.add_neighbor(neighbor=vn, weight=8)
    vj.add_neighbor(neighbor=vo, weight=55)
    vk.add_neighbor(neighbor=vj, weight=22)
    vk.add_neighbor(neighbor=vl, weight=13)
    vk.add_neighbor(neighbor=vo, weight=1)
    vl.add_neighbor(neighbor=vp, weight=32)
    vm.add_neighbor(neighbor=vn, weight=21)
    vn.add_neighbor(neighbor=vj, weight=7)
    vo.add_neighbor(neighbor=vp, weight=1)

    graph.add_vertex(va, vb, vc, vd, ve, vf, vg, vh,
                     vi, vj, vk, vl, vm, vn, vo, vp)

    shortest_path = graph.get_shortest_path(start=va, end=vp)

    pprint('SHORTEST PATH:')
    pprint(shortest_path)

    print()

    pprint('COSTS:')
    pprint(graph.costs, width=40)

    """
    OUTPUT:

    'SHORTEST PATH:'
    [a, b, g, k, o, p]

    'COSTS:'
    {'b': 10,
    'e': 5,
    'f': 50,
    'g': 16,
    'j': 20,
    'k': 17,
    'l': 30,
    'o': 18,
    'p': 19}
    """
