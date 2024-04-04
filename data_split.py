import pandas as pd
import math
### Now we fragment the data into 14 parts ###

### 2 Before episode
### 10 during
### 2 After episode

def split_csv(csv_file, n_parts):
    df = pd.read_csv(csv_file)
    chunk_size = math.ceil(len(df) / n_parts)
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

    for i, chunk in enumerate(chunks, start=1):
        filename = csv_file.split("/")[-1].split(".")[0][:3]
        chunk.to_csv(f"split_data/{filename}_{i}.csv", index=False)

split_csv("filter_data/081_f.csv",14)
split_csv("filter_data/131_f.csv",14)