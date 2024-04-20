import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def load_mi_matrix(file_path, threshold):
    mi_matrix = np.loadtxt(file_path)
    adjacency_matrix = (mi_matrix > threshold).astype(int)
    return adjacency_matrix

def visualize_graph(adjacency_matrix, idx, s):
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                edges.append((i, j))

    G = nx.Graph(edges)
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=200, font_size=8, edge_color='gray')
    plt.title(f"Graph for {s}_{idx}")
    plt.savefig(f"graphs/{s}_{idx}.png")
    plt.close()

def find_threshold(file_path):
    lower_bound = 0.0
    upper_bound = 100.0
    threshold = (lower_bound + upper_bound) / 2
    last_successful_threshold = None
    tolerance = 0.00001

    while True:
        mi_matrix = load_mi_matrix(file_path, threshold)
        G = nx.Graph(mi_matrix)
        Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
        giant_component_size = len(Gcc[0])
        total_nodes = len(G)
        giant_component_ratio = giant_component_size / total_nodes

        if giant_component_ratio >= 0.95:
            # print("Giant Component Found", threshold)
            last_successful_threshold = threshold
            lower_bound = threshold
        elif giant_component_ratio < 0.95:
            upper_bound = threshold
        else:
            lower_bound = threshold

        threshold = (lower_bound + upper_bound) / 2

        if upper_bound - lower_bound < tolerance:
            break

    return last_successful_threshold


mi_directory = "matrices/"

for s in ["081", "131"]:
    for i in range(1, 15):
        mi_file = f"{mi_directory}/{s}_{i}.txt"
        threshold = find_threshold(f"{mi_directory}/{s}_{i}.txt") 
        print(f"Threshold for {s}_{i}: {threshold}")  
        mi_matrix = load_mi_matrix(mi_file, threshold)
        visualize_graph(mi_matrix, i, s)
        