### 
### Plotting the  time series of the two patients
###

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("131j1LMT.csv")

# Uncomment to plot the 2nd Dataset instead
# df = pd.read_csv("081d0LMT.csv")


# Convert indices to seconds
time_seconds = np.arange(len(df)) / 200  #  As 200 Hz is the sampling rate

# Plotting
plt.figure(figsize=(10, 6)) 
for column in df.columns[1:]:
    plt.plot(time_seconds, df[column], label=column)

plt.title('Time Series Data')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
# plt.legend(loc="upper right")  
plt.grid(True)
plt.show()
