import matplotlib.pyplot as plt
import sys
from scipy.signal import find_peaks, butter, filtfilt
import numpy as np


def lowpass(data):
    B, A = butter(2, 0.35, output="ba")
    smooth_data = filtfilt(B, A, data)

    return smooth_data


# Function that takes in dataset and returns heights and index of each peak
def get_peaks(data):
    # Get peak heights and positions
    peaks = find_peaks(data, height=760, threshold=0, distance=6)
    heights = peaks[1]["peak_heights"]
    peak_positions = peaks[0]

    return heights, peak_positions


# Function to plot line graph of data with pulses as red dots
def plot_data():
    # Plot the data
    plt.plot(data, label="original data")
    plt.plot(smooth_data, "y-", label="smoothed data")
    plt.xlabel("time")
    plt.title("pulses")
    plt.scatter(peak_positions, heights, color="r", s=10, label="pulse", zorder=3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Open file and store in data
    file_name = sys.argv[1]
    f = open(file_name, "r")
    data = f.read().splitlines()

    # Change all values in data to integers
    data = [int(i) for i in data]
    data = np.array(data)

    # Smooth data
    smooth_data = lowpass(data)

    # Get heights and positions of peaks
    heights, peak_positions = get_peaks(smooth_data)

    # Print number of peaks
    print(len(heights))

    # Plot data
    plot_data()
