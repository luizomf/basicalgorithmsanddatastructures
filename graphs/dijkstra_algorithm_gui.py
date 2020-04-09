"""
This code is a mess, it's only for me to
show dijkstra algorithm visually
using tkinter (GUI)
"""

from __future__ import annotations
import math
import tkinter as tk
from typing import Dict, List, Optional


class VertexNotInGraphError(ValueError):
    ...


class NotAVertexError(TypeError):
    ...


class AutoScrollbar(tk.Scrollbar):
    # http://effbot.org/zone/tkinter-autoscrollbar.htm
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()

        tk.Scrollbar.set(self, lo, hi)

    def pack(self, **kwargs):
        raise tk.TclError("cannot use pack with this widget")

    def place(self, **kwargs):
        raise tk.TclError("cannot use place with this widget")


class TkinterBoilerplate:
    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        self.root = tk.Tk()

        vscrollbar = AutoScrollbar(self.root)
        vscrollbar.grid(row=0, column=1, sticky='ns')

        hscrollbar = AutoScrollbar(self.root, orient='horizontal')
        hscrollbar.grid(row=1, column=0, sticky='ew')

        self.canvas = tk.Canvas(
            self.root,
            yscrollcommand=vscrollbar.set,
            xscrollcommand=hscrollbar.set,
            background='white'
        )

        self.canvas.grid(row=0, column=0, sticky='nsew')

        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview)

        tk.Grid.rowconfigure(self.root, 0, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1)

        self.main_frame = tk.Frame(self.canvas)
        tk.Grid.rowconfigure(self.main_frame, 1, weight=1)
        tk.Grid.columnconfigure(self.main_frame, 1, weight=1)

    def mainloop(self) -> None:
        self.canvas.create_window(
            0, 0, anchor='nw', window=self.main_frame
        )  # type: ignore
        self.main_frame.update_idletasks()  # type: ignore
        self.canvas.config(
            scrollregion=self.canvas.bbox("all"),  # type: ignore
        )  # type: ignore
        self.root.mainloop()


class Vertex:
    """A class representing a vertex"""

    def __init__(self, name: str, position: tuple) -> None:
        self.name = name
        self.neighbors: Dict[str, float] = {}
        self.position = position
        self.id = 0

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

        self.tkinter = TkinterBoilerplate()
        self.root = self.tkinter.root
        self.main_frame = self.tkinter.main_frame

        self.canvas = tk.Canvas(
            self.main_frame, width=1920,
            height=1080, background='#f4f4f8'
        )
        self.canvas.grid(sticky='news')

        self.root.geometry('840x800')
        self.root.title('Mostrar Grafo Por Tkinter')

    def show_graph_gui(self, shortest_path=None) -> None:
        for vertex in self.graph:
            self.add_edge_to_canvas(self.graph[vertex])

        if shortest_path is not None:
            seconds = 0
            shortest_path = iter(shortest_path)
            self.root.after(
                seconds + 1000,
                lambda: self._change_vertex_color(shortest_path, seconds)
            )

        self.canvas.scale('all', 0, 0, 1.5, 1.5)  # type: ignore
        self.tkinter.mainloop()

    def _change_vertex_color(self, iterator, seconds: int) -> None:
        try:
            self.canvas.itemconfig(
                next(iterator).id - 1,
                fill='#47B7CA'
            )
            self.root.after(
                seconds + 1000,
                lambda: self._change_vertex_color(iterator, seconds)
            )
        except StopIteration:
            ...

    def add_vertex(self, *vertex: Vertex) -> None:
        """Add a vertex or vertices separeted by comma to graph"""
        for v in vertex:
            self._check_vertex_type(v)
            self.graph[v.name] = v
            vertex_id = self.add_vertex_to_canvas(v)
            v.id = vertex_id

    def add_vertex_to_canvas(self, vertex: Vertex) -> int:
        size = 50

        x1, y1 = vertex.position
        x2 = x1 + size
        y2 = y1 + size

        x1_text = x1 + (size // 2)
        y1_text = y1 + (size // 2)

        self.canvas.create_oval(
            x1, y1, x2, y2, fill="#ff464b",
            width=0
        )  # type: ignore

        label_id: int = self.canvas.create_text(
            (x1_text, y1_text), text=vertex.name, fill="#FFF"
        )  # type: ignore

        return label_id

    def add_edge_to_canvas(self, vertex: Vertex):
        line_color = '#F7D765'
        coors1 = self.canvas.coords(vertex.id)  # type: ignore

        for n in vertex.neighbors:
            neighbor: Vertex = self.graph[n]
            coors2 = self.canvas.coords(neighbor.id)  # type: ignore

            x1, y1 = coors1
            x2, y2 = coors2

            x2 = x2 - 25 if x2 > x1 else x2
            y2 = y2 - 25 if y2 > y1 else y2

            x2 = x2 + 25 if x2 < x1 else x2
            y2 = y2 + 25 if y2 < y1 else y2

            line = self.canvas.create_line(
                x1, y1,
                x2, y2,
                fill=line_color, width=5,
                arrow=tk.LAST,
                arrowshape='8 10 2', capstyle="projecting"
            )  # type: ignore

            if vertex.neighbors[n] is not None:
                label = self.canvas.create_text(  # noqa
                    ((x1 + x2) / 2, (y1 + y2) / 2),
                    text=f'{vertex.neighbors[n]}', fill='black'
                )  # type: ignore

            self.canvas.tag_lower(line)  # type: ignore

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

    va = Vertex('a', (100, 100))
    vb = Vertex('b', (200, 100))
    vc = Vertex('c', (300, 100))
    vd = Vertex('d', (400, 100))
    ve = Vertex('e', (100, 200))
    vf = Vertex('f', (200, 200))
    vg = Vertex('g', (300, 200))
    vh = Vertex('h', (400, 200))
    vi = Vertex('i', (100, 300))
    vj = Vertex('j', (200, 300))
    vk = Vertex('k', (300, 300))
    vl = Vertex('l', (400, 300))
    vm = Vertex('m', (100, 400))
    vn = Vertex('n', (200, 400))
    vo = Vertex('o', (300, 400))
    vp = Vertex('p', (400, 400))

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

    graph.show_graph_gui(shortest_path)