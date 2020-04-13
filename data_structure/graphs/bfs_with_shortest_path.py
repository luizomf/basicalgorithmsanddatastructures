from __future__ import annotations
from typing import List, Dict, Deque, Set
from pprint import pprint
from collections import deque


class Vertex:
    """Class representing a Vertex"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors: List[Vertex] = []

    def add_neighbors(self, *vertex: Vertex) -> None:
        for v in vertex:
            if not isinstance(v, Vertex):
                raise TypeError('Must be of type Vertex')
            self.neighbors.append(v)

    def clear(self) -> None:
        self.neighbors.clear()

    def __repr__(self) -> str:
        return f'{self.name}'


class Graph:
    """Class Representing a Graph"""

    def __init__(self) -> None:
        self.graph: Dict[str, Vertex] = {}

    def add_vertices(self, *vertex: Vertex) -> None:
        for v in vertex:
            self.graph[v.name] = v

    def show(self) -> None:
        pprint(self.graph)

    def bfs_algorithm(self, start: Vertex, end: Vertex) -> List[Vertex]:
        """ BFS Algorithm """

        queue: Deque[Vertex] = deque()
        visited_vertices: Set[str] = set()
        bfs_unsolved: List[Vertex] = []

        queue.append(start)
        bfs_unsolved.append(start)
        visited_vertices.add(start.name)

        if start == end:
            return [end]

        if not self.graph.get(start.name) or not self.graph.get(end.name):
            return []

        while queue:
            next_vertext = queue.popleft()
            neighbors = next_vertext.neighbors

            if end in neighbors:
                bfs_unsolved.append(next_vertext)
                break

            for neighbor in neighbors:
                if neighbor.name in visited_vertices:
                    continue

                visited_vertices.add(neighbor.name)
                queue.append(neighbor)
                bfs_unsolved.append(next_vertext)

        bfs_unsolved.append(end)
        shortest_path = self.get_shortest_path(bfs_unsolved)

        return shortest_path

    def get_shortest_path(self, bfs_unsolved: List[Vertex]) -> List[Vertex]:
        """ Solve BFS and get shortest path """
        shortest_path = [bfs_unsolved[-1]]

        for vertex in bfs_unsolved[::-1]:
            prev = shortest_path[-1]

            if vertex in shortest_path:
                continue

            if prev in vertex.neighbors:
                shortest_path.append(vertex)

        return shortest_path[::-1]


def main() -> None:
    list_of_vertices: List[Vertex] = [
        Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'),
        Vertex('E'), Vertex('F'), Vertex('G'), Vertex('H'),
        Vertex('I'), Vertex('J'), Vertex('K'), Vertex('L'),
        Vertex('M'), Vertex('N'), Vertex('O'), Vertex('P'),
        Vertex('Q'), Vertex('R'), Vertex('S'), Vertex('T'),
        Vertex('U'), Vertex('V'), Vertex('W'), Vertex('X'),
        Vertex('Y'), Vertex('Z'),
    ]

    VA = list_of_vertices[0]
    VB = list_of_vertices[1]
    VC = list_of_vertices[2]
    VD = list_of_vertices[3]
    VE = list_of_vertices[4]
    VF = list_of_vertices[5]
    VG = list_of_vertices[6]
    VH = list_of_vertices[7]
    VI = list_of_vertices[8]
    VJ = list_of_vertices[9]
    VK = list_of_vertices[10]
    VL = list_of_vertices[11]
    VM = list_of_vertices[12]
    VN = list_of_vertices[13]
    VO = list_of_vertices[14]
    VP = list_of_vertices[15]

    # noqa: F841 - is for in-line ignore the F841 warning from flake8
    # Because there are a bunch of variables not used bellow.
    #
    # Warning F841 is: local variable name is assigned to but never used
    # http://flake8.pycqa.org/en/2.5.5/warnings.html

    VQ = list_of_vertices[16]  # noqa: F841
    VR = list_of_vertices[17]  # noqa: F841
    VS = list_of_vertices[18]  # noqa: F841
    VT = list_of_vertices[19]  # noqa: F841
    VU = list_of_vertices[20]  # noqa: F841
    VV = list_of_vertices[21]  # noqa: F841
    VW = list_of_vertices[22]  # noqa: F841
    VX = list_of_vertices[23]  # noqa: F841
    VY = list_of_vertices[24]  # noqa: F841
    VZ = list_of_vertices[25]  # noqa: F841

    VA.add_neighbors(VF)
    VB.add_neighbors(VE, VD)
    VC.add_neighbors(VH)
    VD.add_neighbors(VG)
    VE.add_neighbors(VH, VG)
    VF.add_neighbors(VG, VI, VL)
    VG.add_neighbors(VJ)
    VH.add_neighbors(VM)
    VI.add_neighbors(VK)
    VJ.add_neighbors(VK)
    VK.add_neighbors(VN)
    VL.add_neighbors(VO, VK)
    VM.add_neighbors(VN)
    VN.add_neighbors(VP)
    VO.add_neighbors(VN)
    VP.add_neighbors(VP)

    directed_graph = Graph()
    directed_graph.add_vertices(VA, VB, VC, VD, VE, VF, VG, VH,
                                VI, VJ, VK, VL, VM, VN, VO, VP)

    print('From A to P')
    shortest_path_a_to_p = directed_graph.bfs_algorithm(VA, VP)
    pprint(shortest_path_a_to_p)
    print()

    print('From B to P')
    shortest_path_b_to_p = directed_graph.bfs_algorithm(VB, VP)
    pprint(shortest_path_b_to_p)
    print()

    print('From C to P')
    shortest_path_c_to_p = directed_graph.bfs_algorithm(VC, VP)
    pprint(shortest_path_c_to_p)
    print()


if __name__ == "__main__":
    main()
