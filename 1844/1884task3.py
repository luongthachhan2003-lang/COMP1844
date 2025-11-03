import numpy as np
import networkx as nx

# ================================
# RECREATE THE GRAPH FROM TASK 2
# (Data copied exactly from your Task 2 code)
# ================================

# Real track distances (km) from TfL 2025
lines_data = {
    'Bakerloo': {
        'stations': ['Baker Street', "Regent's Park", 'Oxford Circus', 'Piccadilly Circus',
                     'Charing Cross', 'Embankment', 'Waterloo'],
        'distances': [1.20, 0.94, 0.66, 0.77, 0.62, 1.51]
    },
    'Piccadilly': {
        'stations': ["King's Cross St. Pancras", 'Russell Square', 'Holborn', 'Covent Garden',
                     'Leicester Square', 'Piccadilly Circus', 'Green Park'],
        'distances': [1.23, 0.64, 0.44, 0.26, 0.44, 0.51]
    },
    'Northern': {
        'stations': ['Euston', 'Warren Street', 'Goodge Street', 'Tottenham Court Road',
                     'Leicester Square', 'Charing Cross', 'Embankment', 'Waterloo', 'Kennington'],
        'distances': [0.87, 0.3, 0.3, 0.38, 0.62, 0.40, 1.61, 1.10]
    },
    'Central': {
        'stations': ['Oxford Circus', 'Tottenham Court Road', 'Holborn', 'Chancery Lane',
                     "St. Paul's", 'Bank'],
        'distances': [0.50, 0.66, 0.33, 0.44, 0.40]
    },
    'Victoria': {
        'stations': ['Warren Street', 'Oxford Circus', 'Green Park', 'Victoria',
                     'Pimlico', 'Vauxhall', 'Stockwell'],
        'distances': [0.74, 0.62, 1.42, 0.86, 0.99, 1.04]
    }
}

# Create undirected graph
G = nx.Graph()

# Add edges with rounded distances
for line, data in lines_data.items():
    stations = data['stations']
    distances = data['distances']
    for i in range(len(stations) - 1):
        u, v = stations[i], stations[i + 1]
        dist = round(distances[i], 1)
        G.add_edge(u, v, weight=dist)

# ================================
# TASK 3: CALCULATE STATISTICS
# ================================

# Extract all edge weights (distances)
distances = [data['weight'] for u, v, data in G.edges(data=True)]

# Calculate statistics using NumPy
total_length = np.sum(distances)
average_distance = np.mean(distances)
std_deviation = np.std(distances)

# ================================
# DISPLAY RESULTS
# ================================

print("\n" + "="*60)
print(" " * 15 + "TASK 3: NETWORK STATISTICS")
print("="*60)
print(f"{'Total length of the network:':<40} {total_length:>6.1f} km")
print(f"{'Average distance between stations:':<40} {average_distance:>6.2f} km")
print(f"{'Standard deviation of distances:':<40} {std_deviation:>6.2f} km")
print("="*60)