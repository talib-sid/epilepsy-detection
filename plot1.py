### 
### Plotting the  time series of the two patients
###

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import subprocess
import mne 

def plot(csv_file):
    eeg_data = pd.read_csv(csv_file, index_col=0)
    channels = eeg_data.columns.tolist()
    plt.figure(figsize=(10, 6))
    
    # Plot EEG data for each channel with vertical offset
    for i, channel in enumerate(channels):
        plt.plot(eeg_data[channel] + 80 * i, label=channel)
    
    # Plot a dashed gray line at y=0
    plt.plot(np.zeros((len(eeg_data), len(channels))), '--', color='gray')
    
    # Customize the plot
    plt.yticks([])
    plt.axis('tight')
    plt.legend(loc='upper right', fontsize=8)
    plt.title('EEG Data')
    plt.xlabel('Timestamp')
    plt.show()

print("Time Domain(1) or Frequency Domain(2)")
x = int(input());
# x = 1
if(x == 1):
    plot("./filter_data/081_f.csv")
    plot("./filter_data/131_f.csv")
else:
    subprocess.call(["python", "data_transform.py"])

