import importlib.util
import unittest

from graph_algorithms_the_fun_way.graph import Graph
from graph_algorithms_the_fun_way.visualization import draw_graph, to_networkx_graph

HAS_NETWORKX = importlib.util.find_spec("networkx") is not None
HAS_MATPLOTLIB = importlib.util.find_spec("matplotlib") is not None


@unittest.skipUnless(HAS_NETWORKX, "networkx is required for visualization tests")
class TestToNetworkXGraph(unittest.TestCase):
    def test_directed_graph_conversion(self):
        """Test conversion of a directed Graph to NetworkX."""
        g = Graph(3, undirected=False)
        g.insert_edge(0, 1, 2.5)
        g.insert_edge(1, 2, 1.0)

        nx_graph = to_networkx_graph(g)

        self.assertEqual(nx_graph.number_of_nodes(), 3)
        self.assertEqual(nx_graph.number_of_edges(), 2)
        self.assertTrue(nx_graph.has_edge(0, 1))
        self.assertTrue(nx_graph.has_edge(1, 2))
        self.assertAlmostEqual(nx_graph[0][1]["weight"], 2.5)

    def test_undirected_graph_conversion(self):
        """Test conversion of an undirected Graph to NetworkX."""
        g = Graph(3, undirected=True)
        g.insert_edge(0, 1, 3.0)
        g.insert_edge(1, 2, 4.0)

        nx_graph = to_networkx_graph(g)

        self.assertEqual(nx_graph.number_of_nodes(), 3)
        self.assertEqual(nx_graph.number_of_edges(), 2)
        self.assertTrue(nx_graph.has_edge(0, 1))
        self.assertTrue(nx_graph.has_edge(1, 2))
        self.assertAlmostEqual(nx_graph[1][2]["weight"], 4.0)


@unittest.skipUnless(
    HAS_NETWORKX and HAS_MATPLOTLIB,
    "networkx and matplotlib are required for visualization draw tests",
)
class TestDrawGraph(unittest.TestCase):
    def test_draw_graph_returns_axis(self):
        """Test drawing returns a Matplotlib axis without requiring GUI display."""
        import matplotlib

        matplotlib.use("Agg")

        g = Graph(4, undirected=True)
        g.insert_edge(0, 1, 1.0)
        g.insert_edge(1, 2, 1.0)
        g.insert_edge(2, 3, 1.0)

        ax = draw_graph(g, show=False)

        self.assertTrue(hasattr(ax, "plot"))
        self.assertGreater(len(ax.collections), 0)

    def test_draw_graph_invalid_layout(self):
        """Test drawing with an unknown layout raises ValueError."""
        g = Graph(2, undirected=False)
        g.insert_edge(0, 1, 1.0)

        with self.assertRaises(ValueError):
            draw_graph(g, layout="not_a_layout", show=False)
