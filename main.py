"""Small runnable demo for building and visualizing a five-node graph."""

from graph_algorithms_the_fun_way.file_reader import save_graph_to_csv
from graph_algorithms_the_fun_way.file_reader import make_graph_from_weighted_csv
from graph_algorithms_the_fun_way.graph import Graph
from graph_algorithms_the_fun_way.visualization import draw_graph


def build_simple_five_node_graph() -> Graph:
	"""Build a simple undirected graph with five nodes."""
	g = Graph(5, undirected=False)
	g.insert_edge(0, 1, 1.0)
	g.insert_edge(1, 2, 1.0)
	g.insert_edge(2, 3, 1.0)
	g.insert_edge(3, 4, 1.0)
	g.insert_edge(4, 0, 1.0)
	g.insert_edge(0, 2, 1.5)
	return g


def main():
	"""Run the demo and display the graph window."""
	#	g = build_simple_five_node_graph()
	#g = make_graph_from_weighted_csv("five_node_graph.csv", undirected=False)
	#g = make_graph_from_weighted_csv("road_network_250_node_graph.csv", undirected=True)
	g = make_graph_from_weighted_csv("data/road_network_50_node_graph.csv", undirected=True)
	draw_graph(g, layout="spring", show_weights=True, show=True)


if __name__ == "__main__":
	main()
