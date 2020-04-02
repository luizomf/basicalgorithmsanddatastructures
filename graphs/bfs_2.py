from __future__ import annotations
from typing import List, Dict, Deque
from pprint import pprint
from collections import deque


class Vertex:
    """Class representing a Vertex"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbors: List[Vertex] = []

    def add_neighbors(self, *vertex: Vertex) -> None:
        for v in vertex:
            self.neighbors.append(v)

    def clear(self) -> None:
        self.neighbors.clear()

    def __repr__(self) -> str:
        return f'{self.name} -> ' \
            f'{", ".join([v.name for v in self.neighbors])}'


class Graph:
    """Class Representing a Grapth"""

    def __init__(self) -> None:
        self.graph: Dict[str, Vertex] = {}

    def add_vertices(self, *vertex: Vertex) -> None:
        for v in vertex:
            self.graph[v.name] = v

    def show(self) -> None:
        pprint(self.graph)

    def bfs_algorithm(self, starting_vertex: Vertex) -> List[Vertex]:
        bfs_queue: Deque[Vertex] = deque()
        visited_vertices: List[Vertex] = []
        bfs_return_value: List[Vertex] = []

        bfs_queue.append(starting_vertex)
        visited_vertices.append(starting_vertex)

        while bfs_queue:
            checking_vertex = bfs_queue.popleft()
            neighbors = checking_vertex.neighbors

            bfs_return_value.append(checking_vertex)

            for neighbor in neighbors:
                if neighbor in visited_vertices:
                    continue

                visited_vertices.append(neighbor)
                bfs_queue.append(neighbor)

        return bfs_return_value


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
    VS = list_of_vertices[18]
    VT = list_of_vertices[19]  # noqa: F841
    VU = list_of_vertices[20]  # noqa: F841
    VV = list_of_vertices[21]
    VW = list_of_vertices[22]  # noqa: F841
    VX = list_of_vertices[23]
    VY = list_of_vertices[24]  # noqa: F841
    VZ = list_of_vertices[25]

    # For undirected graph
    VA.add_neighbors(VS, VZ)
    VZ.add_neighbors(VA)
    VS.add_neighbors(VA, VX)
    VX.add_neighbors(VS, VD, VC)
    VD.add_neighbors(VX, VC, VF)
    VC.add_neighbors(VX, VD, VF, VV)
    VF.add_neighbors(VD, VC, VV)

    undirected_graph = Graph()
    undirected_graph.add_vertices(VA, VZ, VS, VX, VD, VC, VF)

    bfs_undirected_graph_from_s = undirected_graph.bfs_algorithm(VS)
    print('Undirected Graph')
    pprint(bfs_undirected_graph_from_s)
    print()

    # Clear vertices
    for vertex in list_of_vertices:
        vertex.clear()

    # For directed graph
    VA.add_neighbors(VF)
    VB.add_neighbors(VE, VF)
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

    print('Directed Graph Starting From A')
    bfs_starting_from_a = directed_graph.bfs_algorithm(VA)
    pprint(bfs_starting_from_a)
    print()

    print('Directed Graph Starting From B')
    bfs_starting_from_b = directed_graph.bfs_algorithm(VB)
    pprint(bfs_starting_from_b)
    print()

    print('Directed Graph Starting From C')
    bfs_starting_from_c = directed_graph.bfs_algorithm(VC)
    pprint(bfs_starting_from_c)
    print()


if __name__ == "__main__":
    main()
