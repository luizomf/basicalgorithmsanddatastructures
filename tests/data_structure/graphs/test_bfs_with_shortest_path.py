import unittest
from data_structure.graphs.bfs_with_shortest_path import Vertex
from data_structure.graphs.bfs_with_shortest_path import Graph


class VertexTest(unittest.TestCase):
    def setUp(self):
        self.vertex_a = Vertex('A')
        self.vertex_b = Vertex('B')
        self.vertex_c = Vertex('C')
        self.vertex_d = Vertex('D')
        self.vertex_e = Vertex('E')

    def test_vertex_name(self):
        self.assertEqual(self.vertex_a.name, 'A')
        self.assertEqual(self.vertex_b.name, 'B')
        self.assertEqual(self.vertex_c.name, 'C')
        self.assertEqual(self.vertex_d.name, 'D')

    def test_vertex_add_neighbors_of_type_vertex(self):
        self.vertex_a.add_neighbors(self.vertex_b, self.vertex_c)
        self.vertex_a.add_neighbors(self.vertex_d)

        neighbor_names = ['A', 'B', 'C', 'D']

        for neighbor in self.vertex_a.neighbors:
            with self.subTest(neighbor=neighbor):
                self.assertTrue(neighbor.name in neighbor_names)

    def test_vertex_add_neighbors_wrong_type(self):
        with self.assertRaises(TypeError):
            self.vertex_a.add_neighbors('A')

    def test_vertex_clear(self):
        vertex = Vertex('E')
        vertex.add_neighbors(self.vertex_b, self.vertex_c, self.vertex_d)
        vertex.clear()
        self.assertEqual(len(vertex.neighbors), 0)

    def test_vertex_str(self):
        vertex = Vertex('VERTEXNAME')
        self.assertEqual(str(vertex), 'VERTEXNAME')


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

        self.vertex_a = Vertex('a')
        self.vertex_b = Vertex('b')
        self.vertex_c = Vertex('c')
        self.vertex_d = Vertex('d')
        self.vertex_e = Vertex('e')
        self.vertex_f = Vertex('f')

        self.vertex_a.add_neighbors(self.vertex_b)
        self.vertex_a.add_neighbors(self.vertex_c)
        self.vertex_b.add_neighbors(self.vertex_d)
        self.vertex_b.add_neighbors(self.vertex_e)
        self.vertex_d.add_neighbors(self.vertex_f)
        self.vertex_e.add_neighbors(self.vertex_f)

        self.graph.add_vertices(
            self.vertex_a, self.vertex_b, self.vertex_c, self.vertex_d,
            self.vertex_e, self.vertex_f
        )

    def test_graph_content(self):
        self.assertEqual(
            str(self.graph.graph),
            "{'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}"
        )

    def test_graph_shortest_path_from_a_to_b(self):
        self.assertEqual(
            self.graph.bfs_algorithm(self.vertex_a, self.vertex_b),
            [self.vertex_a, self.vertex_b]
        )

    def test_graph_shortest_path_from_a_to_d(self):
        self.assertEqual(
            self.graph.bfs_algorithm(self.vertex_a, self.vertex_d),
            [self.vertex_a, self.vertex_b, self.vertex_d]
        )

    def test_graph_shortest_path_from_a_to_f(self):
        self.assertEqual(
            self.graph.bfs_algorithm(self.vertex_a, self.vertex_f),
            [self.vertex_a, self.vertex_b, self.vertex_d, self.vertex_f]
        )

    def test_graph_shortest_path_from_a_to_e(self):
        self.assertEqual(
            self.graph.bfs_algorithm(self.vertex_a, self.vertex_e),
            [self.vertex_a, self.vertex_b, self.vertex_e]
        )
