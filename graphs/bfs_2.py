from __future__ import annotations
from typing import List, Dict, Deque
from pprint import pprint
from collections import deque


class Vertex:
    """Class representing a Vertex"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.adjacent_vertices: List[Vertex] = []

    def add_adjacent(self, *vertex: Vertex) -> None:
        for v in vertex:
            self.adjacent_vertices.append(v)

    def __repr__(self) -> str:
        return f'{self.name} -> ' \
            f'{", ".join([v.name for v in self.adjacent_vertices])}'


class DiGraph:
    """Class Representing a DiGrapth"""

    def __init__(self) -> None:
        self.graph: Dict[str, Vertex] = {}

    def add_vertex(self, *vertex: Vertex) -> None:
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
            adjacent_vertices = checking_vertex.adjacent_vertices

            bfs_return_value.append(checking_vertex)

            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex in visited_vertices:
                    continue

                visited_vertices.append(adjacent_vertex)
                bfs_queue.append(adjacent_vertex)

        return bfs_return_value


def main() -> None:
    VA = Vertex('A')
    VB = Vertex('B')
    VC = Vertex('C')
    VD = Vertex('D')
    VE = Vertex('E')
    VF = Vertex('F')
    VG = Vertex('G')
    VH = Vertex('H')
    VI = Vertex('I')
    VJ = Vertex('J')
    VK = Vertex('K')
    VL = Vertex('L')
    VM = Vertex('M')
    VN = Vertex('N')
    VO = Vertex('O')
    VP = Vertex('P')

    VA.add_adjacent(VF)
    VB.add_adjacent(VE, VF)
    VC.add_adjacent(VH)
    VD.add_adjacent(VG)
    VE.add_adjacent(VH, VG)
    VF.add_adjacent(VG, VI, VL)
    VG.add_adjacent(VJ)
    VH.add_adjacent(VM)
    VI.add_adjacent(VK)
    VJ.add_adjacent(VK)
    VK.add_adjacent(VN)
    VL.add_adjacent(VO, VK)
    VM.add_adjacent(VN)
    VN.add_adjacent(VP)
    VO.add_adjacent(VN)
    VP.add_adjacent(VP)

    graph = DiGraph()
    graph.add_vertex(VA, VB, VC, VD, VE, VF, VG, VH,
                     VI, VJ, VK, VL, VM, VN, VO, VP)

    # graph.show()

    bfs_starting_from_a = graph.bfs_algorithm(VA)
    pprint(bfs_starting_from_a)
    print()

    bfs_starting_from_b = graph.bfs_algorithm(VB)
    pprint(bfs_starting_from_b)
    print()

    bfs_starting_from_c = graph.bfs_algorithm(VC)
    pprint(bfs_starting_from_c)
    print()


if __name__ == "__main__":
    main()
