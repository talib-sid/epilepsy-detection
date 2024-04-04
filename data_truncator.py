import pandas as pd

def truncate_csv(data_csv, start_index, end_index):
    df = pd.read_csv(data_csv)

    start_index = start_index - 5000
    end_index = end_index + 5000

    truncated_df = df.iloc[start_index:end_index]
    truncated_df.to_csv("./filter_data/" + data_csv.replace(".csv", "_t.csv"), index=False)



### File 081
### Start Index (Episode) : 48073
### Endin Index (Episode) : 127240
truncate_csv("081.csv", 48073, 127240)


### File 131
### Start Index (Episode) : 23693
### Endin Index (Episode) : 86026
truncate_csv("131.csv", 23693, 86026)
