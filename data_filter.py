from scipy.signal import butter, filtfilt
import pandas as pd

def filter_data(input_csv):
    truncated_df = pd.read_csv(input_csv)

    # Alpha band frequency range
    alpha_band = (8, 12) 

    # Design a digital bandpass filter for the alpha band
    nyquist_freq = 0.5 * 200 
    alpha_band_norm = [freq / nyquist_freq for freq in alpha_band]
    b, a = butter(N=4, Wn=alpha_band_norm, btype='band')

    # Apply the filter to each column of the truncated data
    filtered_df = truncated_df.copy()
    for column in filtered_df.columns[1:]:
        filtered_df[column] = filtfilt(b, a, filtered_df[column])

    filtered_df.to_csv(input_csv.replace("_clean.csv","_f.csv"), index=False)


filter_data("filter_data/081_clean.csv")
filter_data("filter_data/131_clean.csv")