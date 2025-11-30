import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


lines_data = {
    'Bakerloo': {
        'color': '#B36305',
        'stations': ['Baker Street', "Regent's Park", 'Oxford Circus', 'Piccadilly Circus', 
                     'Charing Cross', 'Embankment', 'Waterloo'],
        'distances': [1.20, 0.94, 0.66, 0.77, 0.62, 1.51]  # km thực tế
    },
    'Piccadilly': {
        'color': '#0019A8',
        'stations': ["King's Cross St. Pancras", 'Russell Square', 'Holborn', 'Covent Garden', 
                     'Leicester Square', 'Piccadilly Circus', 'Green Park'],
        'distances': [1.23, 0.64, 0.44, 0.26, 0.44, 0.51]
    },
    'Northern': {
        'color': '#000000',
        'stations': ['Euston', 'Warren Street', 'Goodge Street', 'Tottenham Court Road', 
                     'Leicester Square', 'Charing Cross', 'Embankment', 'Waterloo', 'Kennington'],
        'distances': [0.87, 0.3, 0.3, 0.38, 0.62, 0.40, 1.61, 1.10]
    },
    'Central': {
        'color': '#EE1D23',
        'stations': ['Oxford Circus', 'Tottenham Court Road', 'Holborn', 'Chancery Lane', 
                     "St. Paul's", 'Bank'],
        'distances': [0.50, 0.66, 0.33, 0.44, 0.40]
    },
    'Victoria': {
        'color': '#0098D4',
        'stations': ['Warren Street', 'Oxford Circus', 'Green Park', 'Victoria', 
                     'Pimlico', 'Vauxhall', 'Stockwell'],
        'distances': [0.74, 0.62, 1.42, 0.86, 0.99, 1.04]
    }
}


G = nx.Graph()


for line, data in lines_data.items():
    stations = data['stations']
    distances = data['distances']
    for i in range(len(stations) - 1):
        u = stations[i]
        v = stations[i + 1]
        dist = round(distances[i], 1)  
        G.add_edge(u, v, weight=dist, color=data['color'], line=line)
        
        G.add_edge(v, u, weight=dist, color=data['color'], line=line)


pos = {
    "Baker Street": (-0.9, 5.5),
    "Regent's Park": (-0.65, 5.5),
    "Oxford Circus": (-0.65, 3),
    "Piccadilly Circus": (-0.343, 1.47),
    "Charing Cross": (0.024, 1.03),
    "Embankment": (0.268, 1.03),
    "Westminster": (1.2, 1.5),
    "Green Park": (-0.656, 1.26),
    "Leicester Square": (-0.221, 2.22),
    "Covent Garden": (-0.045, 2.22),
    "Holborn": (0.09, 3),
    "Russell Square": (-0.045, 4.6),
    "King's Cross St. Pancras": (-0.045, 9),
    "Warren Street": (-0.375, 4.4),
    "Goodge Street": (-0.2, 3.85),
    "Tottenham Court Road": (-0.375, 3),
    "Bond Street": (-1.5, 3),
    "Marble Arch": (-2, 2.5),
    "Lancaster Gate": (-2.5, 2),
    "Paddington": (-2.7, 3.2),
    "Victoria": (-0.656, -1.8),
    "Pimlico": (-0.362, -3.55),
    "Vauxhall": (0.163, -3.55),
    "Stockwell": (0.163, -7.8),
    "Kennington": (1.4, -1.24),
    "Waterloo": (1.182, 1.03),
    "Euston": (-0.143, 5.6),
    "Chancery Lane": (0.3, 3),
    "St. Paul's": (0.5, 3),
    "Bank": (0.7, 3)

}


plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=400, edgecolors='black', linewidths=1)
edge_colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=3)
# Render edge labels on two lines: number above, 'km' below
edge_labels = {(u, v): f"{G[u][v]['weight']:.1f}\nkm" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7)

# Labels 
short_labels = {node: node.replace(" St. Pancras", "").replace("'", "") for node in G.nodes()}


label_pos = {}
for node, (x, y) in pos.items():
    
    exact_on_node = {"Baker Street", "Warren Street", "Goodge Street", "Covent Garden", "Waterloo", "Kennington"}
    if node in exact_on_node:
        label_pos[node] = (x, y)
        continue

    
    if "Circus" in node or "Square" in node:
        label_pos[node] = (x, y - 0.1)  
    elif "Street" in node or "Garden" in node:
        label_pos[node] = (x + 0.1, y)  
    elif x < -1:  
        label_pos[node] = (x - 0.05, y)  
    elif x > 1:   
        label_pos[node] = (x + 0.05, y)  
    else:
        label_pos[node] = (x, y + 0.1)  
nx.draw_networkx_labels(G, label_pos, labels=short_labels, font_size=7,
                       bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=2),
                       horizontalalignment='center')


legend_elements = [plt.Line2D([0], [0], color=data['color'], lw=4, label=line) for line, data in lines_data.items()]
plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))

plt.axis('off')
plt.title('London Underground Central Section (TfL October 2025)', fontsize=14)
plt.tight_layout()
plt.show()

