### 
### Plotting the  time series of the two patients
###

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import subprocess

def plot(csv_file):
    df = pd.read_csv(csv_file)
    
    # Convert indices to seconds
    time_seconds = np.arange(len(df)) / 200  #  As 200 Hz is the sampling rate

    # Plotting
    plt.figure(figsize=(10, 6)) 
    for column in df.columns[1:]:
        plt.plot(time_seconds, df[column], label=column)

    plt.title('Time Series')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Signal')
    # plt.legend(loc="upper right")  
    plt.grid(True)
    plt.show()


print("Do you want the Time Domain(1) or Frequency Domain(2)")
x = int(input());
if(x == 1):
    plot("./filter_data/081_f.csv")
    plot("./filter_data/131_f.csv")
else:
    subprocess.call(["python", "data_transform.py"])

