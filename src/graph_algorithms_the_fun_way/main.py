"""Small runnable demo for building and visualizing a five-node graph."""

from graph_algorithms_the_fun_way.graph import Graph
from graph_algorithms_the_fun_way.visualization import draw_graph


def build_simple_five_node_graph() -> Graph:
	"""Build a simple undirected graph with five nodes."""
	g = Graph(5, undirected=True)
	g.insert_edge(0, 1, 1.0)
	g.insert_edge(1, 2, 1.0)
	g.insert_edge(2, 3, 1.0)
	g.insert_edge(3, 4, 1.0)
	g.insert_edge(4, 0, 1.0)
	g.insert_edge(0, 2, 1.5)
	return g


def visualize_simple_five_node_graph() -> Graph:
	"""Build and display a simple five-node graph."""
	g = build_simple_five_node_graph()
	draw_graph(g, layout="spring", show_weights=True, show=True)
	return g

def main():
	"""Run the demo and display the graph window."""
	g = build_simple_five_node_graph()
	draw_graph(g, layout="spring", show_weights=True, show=True)


if __name__ == "__main__":
	main()
