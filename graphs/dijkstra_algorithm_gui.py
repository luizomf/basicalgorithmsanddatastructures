"""
This code is a mess, it's only for me to
show dijkstra algorithm visually
using tkinter (GUI)

If you need to check something here, just
copy and paste the full file and execute it.

Python 3.8.0
"""

from __future__ import annotations
import math
import tkinter as tk
from typing import Dict, List, Optional
from random import choices


def generate_hex_color() -> str:
    letters_and_numbes = f'ABCDEF0123456789'
    return '#' + ''.join(choices(letters_and_numbes, k=6))


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
        self._set_initial_attributes()

        # From here on, only tkinter setup
        self.tkinter = TkinterBoilerplate()
        self.root = self.tkinter.root
        self.main_frame = self.tkinter.main_frame

        self.canvas = tk.Canvas(
            self.main_frame, width=560,
            height=560, background='#f4f4f8'
        )
        self.canvas.grid(sticky='news')

        self.root.geometry('570x570+100+100')
        self.root.title('Dijkstra Algorithm')

    def show_graph_gui(self, shortest_path=None) -> None:
        """ Show graph using tkinter """
        for vertex in self.graph:
            self._add_edge_to_canvas(self.graph[vertex])

        if shortest_path is not None:
            seconds = 0
            color = generate_hex_color()
            self.root.after(
                seconds + 1000,
                lambda: self._change_vertex_color(
                    shortest_path, seconds, color
                )
            )

        # tkinter
        self.canvas.scale('all', 0, 0, 1.5, 1.5)  # type: ignore
        self.tkinter.mainloop()

    def _change_vertex_color(self, vertices, seconds: int, color: str) -> None:
        """ Show shortest path in graph """
        if not hasattr(vertices, '__next__'):
            vertices_iterator = iter(vertices)
        else:
            vertices_iterator = vertices

        try:
            self.canvas.itemconfig(
                next(vertices_iterator).id - 1,
                fill=color
            )
            self.root.after(
                seconds + 500,
                lambda: self._change_vertex_color(
                    vertices_iterator, seconds, color
                )
            )
        except StopIteration:
            self.root.after_cancel(1)  # type: ignore

    def add_vertex(self, *vertex: Vertex) -> None:
        """Add a vertex or vertices separeted by comma to graph"""
        for v in vertex:
            self._check_vertex_type(v)
            self.graph[v.name] = v
            vertex_id = self._add_vertex_to_canvas(v)
            v.id = vertex_id

    def _add_vertex_to_canvas(self, vertex: Vertex) -> int:
        """ Add vertex to canvas - tkinter """
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

    def _add_edge_to_canvas(self, vertex: Vertex):
        """Make edge connections from vertex to it's neighbors"""
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
        """All vertices need to use Vertex class"""
        if not isinstance(vertex, Vertex):
            raise NotAVertexError(f'{vertex} has to be of type Vertex')

    def _check_vertex_in_graph(self, vertex: Vertex) -> None:
        self._check_vertex_type(vertex)

        if not self.graph.get(vertex.name):
            raise VertexNotInGraphError(f'{vertex} not in graph')

    def _set_initial_data(self, vertex: Vertex):
        """Fill costs and parents initial data"""
        self._check_vertex_type(vertex)

        if vertex.name not in self.graph:
            raise VertexNotInGraphError(f'{vertex.name} not in graph')

        for name, cost in vertex.neighbors.items():
            self.costs[name] = cost
            self._parents[name] = vertex.name

    def _set_initial_attributes(self) -> None:
        """Declare initial attributes"""
        self.costs: Dict[str, float] = {}
        self._parents: Dict[str, str] = {}
        self._visited_vertices: List[Vertex] = []

    def _dijkstra_algorithm(self, start: Vertex, end: Vertex) -> None:
        self._set_initial_attributes()
        self._set_initial_data(start)

        if start == end:
            return

        self._check_vertex_in_graph(start)
        self._check_vertex_in_graph(end)

        head_vertex = self._get_lowest_cost()

        while head_vertex:
            for neighbor, cost in head_vertex.neighbors.items():
                if cost < self.costs.get(neighbor, math.inf):
                    self.costs[neighbor] = cost + self.costs[head_vertex.name]
                    self._parents[neighbor] = head_vertex.name

            self._visited_vertices.append(head_vertex)

            if head_vertex == end:
                break

            head_vertex = self._get_lowest_cost()

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
        """ Get lowest cost vertex in costs """
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

    va = Vertex(name='a', position=(10, 10))
    vb = Vertex(name='b', position=(110, 10))
    vc = Vertex(name='c', position=(210, 10))
    vd = Vertex(name='d', position=(310, 10))
    ve = Vertex(name='e', position=(10, 110))
    vf = Vertex(name='f', position=(110, 110))
    vg = Vertex(name='g', position=(210, 110))
    vh = Vertex(name='h', position=(310, 110))
    vi = Vertex(name='i', position=(10, 210))
    vj = Vertex(name='j', position=(110, 210))
    vk = Vertex(name='k', position=(210, 210))
    vl = Vertex(name='l', position=(310, 210))
    vm = Vertex(name='m', position=(10, 310))
    vn = Vertex(name='n', position=(110, 310))
    vo = Vertex(name='o', position=(210, 310))
    vp = Vertex(name='p', position=(310, 310))

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
