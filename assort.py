import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def load_mi_matrix(file_path, threshold):
    mi_matrix = np.loadtxt(file_path)
    adjacency_matrix = (mi_matrix > threshold).astype(int)
    return adjacency_matrix

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

def compute_assortativity(file_paths, threshold):
    assortativity_all = []

    for file_path in file_paths:
        mi_matrix = load_mi_matrix(file_path, threshold)
        G = nx.Graph(mi_matrix)
        assortativity = nx.degree_assortativity_coefficient(G)
        assortativity_all.append(assortativity)

    return assortativity_all

def plot_heatmap(assortativity_all, s):
    plt.figure(figsize=(8, 6))
    plt.imshow([assortativity_all], cmap='hot', aspect='auto')
    plt.colorbar(label='Assortativity')
    plt.title(f"Heatmap of Assortativity for {s}")
    plt.xlabel("Network")
    plt.ylabel("Assortativity")
    plt.savefig(f"degree/{s}_assortativity_heatmap.png")
    plt.close()

mi_directory = "matrices/"

for s in ["081", "131"]:
    file_paths = [f"{mi_directory}/{s}_{i}.txt" for i in range(1, 15)]
    threshold = find_threshold(file_paths[0]) 
    assortativity_all = compute_assortativity(file_paths, threshold)
    plot_heatmap(assortativity_all, s)
