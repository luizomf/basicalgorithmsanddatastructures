import unittest
from data_structure.graphs.bfs_with_shortest_path import Vertex


class VertexTest(unittest.TestCase):
    def setUp(self):
        self.vertex_a = Vertex('A')
        self.vertex_b = Vertex('B')
        self.vertex_c = Vertex('C')
        self.vertex_d = Vertex('D')

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
        vertex = Vertex('THIS IS MY NAME')
        self.assertEqual(str(vertex), 'THIS IS MY NAME')
