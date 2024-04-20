import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from joblib import Parallel, delayed


def mutual_information(x, y, bins=10):
    # Compute histogram
    hist, x_edges, y_edges = np.histogram2d(x, y, bins=bins, density=True)
    
    p_xy = hist / np.sum(hist)
    
    # Compute marginal probability distributions
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i, j] > 0:
                mi += p_xy[i, j] * np.log(p_xy[i, j] / (p_x[i] * p_y[j]))
    return mi

def compute_mi(data, col1, col2):
    x = data[col1].values.reshape(-1, 1)
    y = data[col2].values
    return mutual_info_regression(x, y)[0]

def func_mi(csv,idx,s):
    data = pd.read_csv(csv)
    mi_matrix = np.zeros((len(data.columns), len(data.columns)))
    
    # Compute Mutual Information for each pair of columns
    for i, col1 in enumerate(data.columns):
        for j, col2 in enumerate(data.columns):
            x = data[col1]
            y = data[col2]
            mi_matrix[i, j] = mutual_information(x, y)

    # results = Parallel(n_jobs=-1)(delayed(compute_mi)(data, col1, col2)
    #                               for i, col1 in enumerate(data.columns)
    #                               for j, col2 in enumerate(data.columns))
    # for i, col1 in enumerate(data.columns):
    #     for j, col2 in enumerate(data.columns):
    #         mi_matrix[i, j] = results[i * len(data.columns) + j]

 
    print("MI Matrix:")
    print(mi_matrix)
    print(mi_matrix.shape)

    np.savetxt(f"matrices/{s}_{idx}.txt", mi_matrix)

    
    plt.figure(figsize=(10, 6))
    sns.heatmap(mi_matrix, cmap="coolwarm", linewidths=0.5, xticklabels=data.columns, yticklabels=data.columns)
    plt.title(f"MI Heatmap for {idx}th Split")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    # plt.show()
    plt.savefig(f"plots/MI2/{s}_{idx}")


def func_pc(csv,idx,s):
    data = pd.read_csv(csv)
    correlation_matrix = data.corr()


    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, cmap="coolwarm", linewidths=0.5)
    plt.title(f"PC Heatmap for {idx}th split")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    # plt.show()
    plt.savefig(f"plots/PC/{s}_{idx}")


for s in ["081", "131"]:
    for i in range(1, 15):
        csv_file = f"split_data/{s}_{i}.csv"
        func_mi(csv_file,i,s)
        func_pc(csv_file,i,s)
