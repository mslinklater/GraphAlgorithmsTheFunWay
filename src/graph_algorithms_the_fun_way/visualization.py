"""Helpers for visualizing graph structures.

This module provides plotting utilities for the Graph class using
optional third-party dependencies.
"""

from typing import Dict, Optional, Tuple

from graph_algorithms_the_fun_way.graph import Graph


def to_networkx_graph(g: Graph):
    """Convert a Graph object into a NetworkX graph.

    Parameters
    ----------
    g : Graph
        The graph to convert.

    Returns
    -------
    nx_graph : networkx.Graph or networkx.DiGraph
        A NetworkX graph populated with nodes and weighted edges.
    """
    try:
        import networkx as nx
    except ImportError as exc:
        raise ImportError(
            "to_networkx_graph requires the optional dependency 'networkx'. "
            "Install it with: pip install networkx"
        ) from exc

    nx_graph = nx.Graph() if g.undirected else nx.DiGraph()

    for node in g.nodes:
        nx_graph.add_node(node.index, label=node.label)

    for node in g.nodes:
        for edge in node.edges.values():
            nx_graph.add_edge(edge.from_node, edge.to_node, weight=edge.weight)

    return nx_graph


def draw_graph(
    g: Graph,
    pos: Optional[Dict[int, Tuple[float, float]]] = None,
    layout: str = "spring",
    with_labels: bool = True,
    show_weights: bool = False,
    node_color: str = "#6aaed6",
    edge_color: str = "#555555",
    node_size: int = 650,
    figsize: Tuple[float, float] = (8.0, 6.0),
    ax=None,
    show: bool = True,
):
    """Draw a Graph using matplotlib and NetworkX.

    Parameters
    ----------
    g : Graph
        The graph to draw.
    pos : dict, optional
        Optional positions for nodes, keyed by node index.
    layout : str
        One of "spring", "circular", "shell", "kamada_kawai", or "random".
        Used only when ``pos`` is not provided.
    with_labels : bool
        Whether to draw labels for nodes.
    show_weights : bool
        Whether to draw edge weight labels.
    node_color : str
        Color used for nodes.
    edge_color : str
        Color used for edges.
    node_size : int
        Node size in points^2.
    figsize : tuple
        Figure size used when ``ax`` is not provided.
    ax : matplotlib axis, optional
        Axis to draw on.
    show : bool
        Whether to call ``plt.show()`` after drawing.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The axis where the graph was drawn.
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ImportError(
            "draw_graph requires the optional dependency 'matplotlib'. "
            "Install it with: pip install matplotlib"
        ) from exc

    try:
        import networkx as nx
    except ImportError as exc:
        raise ImportError(
            "draw_graph requires the optional dependency 'networkx'. "
            "Install it with: pip install networkx"
        ) from exc

    nx_graph = to_networkx_graph(g)

    if ax is None:
        _, ax = plt.subplots(figsize=figsize)

    if pos is None:
        if layout == "spring":
            pos = nx.spring_layout(nx_graph, seed=0)
        elif layout == "circular":
            pos = nx.circular_layout(nx_graph)
        elif layout == "shell":
            pos = nx.shell_layout(nx_graph)
        elif layout == "kamada_kawai":
            pos = nx.kamada_kawai_layout(nx_graph)
        elif layout == "random":
            pos = nx.random_layout(nx_graph, seed=0)
        else:
            raise ValueError(f"Unknown layout '{layout}'")

    labels = None
    if with_labels:
        labels = {}
        for node in g.nodes:
            labels[node.index] = node.label if node.label is not None else str(node.index)

    nx.draw(
        nx_graph,
        pos=pos,
        ax=ax,
        labels=labels,
        with_labels=with_labels,
        node_color=node_color,
        edge_color=edge_color,
        node_size=node_size,
    )

    if show_weights:
        edge_labels = nx.get_edge_attributes(nx_graph, "weight")
        nx.draw_networkx_edge_labels(nx_graph, pos=pos, edge_labels=edge_labels, ax=ax)

    if show:
        plt.show()

    return ax
