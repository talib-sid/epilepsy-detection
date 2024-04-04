import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fft_transform(csv):    
    eeg_data = pd.read_csv(csv)
    eeg_data_values = eeg_data.iloc[:, 1:].values

    fft_data = np.fft.fft(eeg_data_values, axis=0)

    sampling_rate = 200 
    num_samples = len(eeg_data_values)
    frequencies = np.fft.fftfreq(num_samples, d=1/sampling_rate)

    plt.figure(figsize=(10, 6)) 
    for i in range(eeg_data_values.shape[1]):
        magnitude_spectrum = np.abs(fft_data[:num_samples // 2, i])
        plt.plot(frequencies[:num_samples // 2], magnitude_spectrum, label="Channel {}".format(i+1))

    plt.title("Frequency Spectrum for All Channels")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()


print("Filtered Data(1) or Unfiltered Data(2)")
x = int(input())
if(x == 1):
    fft_transform("filter_data/081_f.csv")
    fft_transform("filter_data/131_f.csv")
else:        
    fft_transform("filter_data/081_clean.csv")
    fft_transform("filter_data/131_clean.csv")