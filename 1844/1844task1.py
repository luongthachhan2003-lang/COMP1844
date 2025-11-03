import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
plt.figure(figsize=(15,5))
# Add nodes (stations)
stations = ["Oxford Circus", "Piccadilly Circus", "Leicester Square", "Covent Garden", "Charing Cross"]
G.add_nodes_from(stations)

# Add edges with actual distances (in km) and colors
edges = [
    ("Oxford Circus", "Piccadilly Circus", {"weight": "0.8km", "color": "brown", "line": "Bakerloo"}),  # a
    ("Piccadilly Circus", "Charing Cross", {"weight": "0.6km", "color": "brown", "line": "Bakerloo"}),  # b
    ("Piccadilly Circus", "Leicester Square", {"weight": "0.4km", "color": "blue", "line": "Piccadilly"}),  # d
    ("Leicester Square", "Covent Garden", {"weight": "0.3km", "color": "blue", "line": "Piccadilly"}),  # e
    ("Leicester Square", "Charing Cross", {"weight": "0.4km", "color": "black", "line": "Northern"})  # c
]
G.add_edges_from([(u, v, data) for u, v, data in edges])

# Positions adjusted to closely match the sample layout
pos = {
    "Oxford Circus": (0, 3),
    "Piccadilly Circus": (1, 1.53),
    "Leicester Square": (2, 1.53),
    "Covent Garden": (2.3, 2),
    "Charing Cross": (2, 0)
}

pos_labels = {
    "Oxford Circus": (0.2, 3),  # Move slightly up
    "Piccadilly Circus": (0.8, 1.3),  # Move slightly down
    "Leicester Square": (2.23, 1.5),  # Move slightly up
    "Covent Garden": (2.3, 2.3),  # Move right
    "Charing Cross": (2, -0.23)  # Move down
}

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=500)

# Draw edges with colors
edge_colors = [data["color"] for u, v, data in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

# Draw edge labels (distances)
edge_labels = {(u, v): data["weight"] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw node labels with custom positions
nx.draw_networkx_labels(G, pos_labels)

# Add legend (key)
from matplotlib.lines import Line2D


legend_elements = [
    Line2D([0], [0], color="blue", lw=2, label="Piccadilly"),
    Line2D([0], [0], color="black", lw=2, label="Northern"),
    Line2D([0], [0], color="brown", lw=2, label="Bakerloo")
]
plt.legend(handles=legend_elements, loc="lower right")

# Show plot without axes
plt.axis("off")
plt.show()