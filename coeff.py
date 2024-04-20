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

def compute_clustering_coefficient(file_paths):
    clustering_coefficients_all = []

    for file_path in file_paths:
        threshold = find_threshold(file_path) 
        mi_matrix = load_mi_matrix(file_path, threshold)
        G = nx.Graph(mi_matrix)
        clustering_coefficients = nx.clustering(G)
        clustering_coefficients_all.append(list(clustering_coefficients.values()))

    return clustering_coefficients_all

def plot_heatmap(clustering_coefficients_all, s):
    plt.figure(figsize=(8, 6))
    plt.imshow(clustering_coefficients_all, cmap='hot', aspect='auto')
    plt.colorbar(label='Clustering Coefficient')
    plt.title(f"Clustering Coefficients for {s}")
    plt.xlabel("Node Index")
    plt.ylabel("Network")
    plt.savefig(f"degree/{s}_clustering_coefficient.png")
    plt.close()

mi_directory = "matrices/"

for s in ["081", "131"]:
    file_paths = [f"{mi_directory}/{s}_{i}.txt" for i in range(1, 15)]
    clustering_coefficients_all = compute_clustering_coefficient(file_paths)
    plot_heatmap(clustering_coefficients_all, s)
