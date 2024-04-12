import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.projections import PolarAxes
import mpl_toolkits.axisartist.grid_finder as gf
import mpl_toolkits.axisartist.floating_axes as fa
from mpl_toolkits.axisartist import Subplot
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear


file_path = 'a.xlsx'

# Reading the data from the excel file according to the user's specifications
ANN1  = pd.read_excel(file_path, usecols='J', skiprows=1, nrows=1411)
RF2   = pd.read_excel(file_path, usecols='K', skiprows=1, nrows=1411)
RF3  = pd.read_excel(file_path, usecols='L', skiprows=1, nrows=1411)
RF4 = pd.read_excel(file_path, usecols='M', skiprows=1, nrows=1411)
HS = pd.read_excel(file_path, usecols='A', skiprows=1, nrows=1499)
CALJH = pd.read_excel(file_path, usecols='B', skiprows=1, nrows=1499)
FAO56_PM = pd.read_excel(file_path, usecols='I', skiprows=1, nrows=1411)
ETO = pd.read_excel(file_path, usecols='C', skiprows=1, nrows=1499)

# Converting the data to NumPy arrays
nANN1_num = ANN1.to_numpy().flatten()
nRF2_num = RF2.to_numpy().flatten()
nRF3_num = RF3.to_numpy().flatten()
nRF4_num = RF4.to_numpy().flatten()
nHS_num = HS.to_numpy().flatten()
nCALJH_num = CALJH.to_numpy().flatten()
nFAO56_PM_num = FAO56_PM.to_numpy().flatten()
nETO_num = ETO.to_numpy().flatten()
medianprops = dict(linestyle='-', linewidth=2, color='red')
meanprops = dict(marker='+', markeredgecolor='black', markerfacecolor='blue')
flierprops = dict(marker='o', markeredgecolor='green', markersize=16)

# Assuming ANN_num, RF_num, SVM_num are your datasets
def calculate_statistics(data):
    lower_quartile = np.percentile(data, 25)
    upper_quartile = np.percentile(data, 75)
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    return lower_quartile, upper_quartile, mean, median, std_dev

nANN1_stats = calculate_statistics(nANN1_num)
nRF2_stats = calculate_statistics(nRF2_num)
nRF3_stats = calculate_statistics(nRF3_num)
nRF4_stats = calculate_statistics(nRF4_num)
nHS_stats = calculate_statistics(nHS_num)
nCALJH_stats = calculate_statistics(nCALJH_num)
nFAO56_PM_stats = calculate_statistics(nFAO56_PM_num)

print("ANN1 - Lower Quartile:", nANN1_stats[0], "Upper Quartile:", nANN1_stats[1], "Mean:", nANN1_stats[2], "Median:", nANN1_stats[3], "Standard Deviation:", nANN1_stats[4])
print("RF2 - Lower Quartile:", nRF2_stats[0], "Upper Quartile:", nRF2_stats[1], "Mean:", nRF2_stats[2], "Median:", nRF2_stats[3], "Standard Deviation:", nRF2_stats[4])
print("RF3 - Lower Quartile:", nRF3_stats[0], "Upper Quartile:", nRF3_stats[1], "Mean:", nRF3_stats[2], "Median:", nRF3_stats[3], "Standard Deviation:", nRF3_stats[4])
print("RF4 - Lower Quartile:", nRF4_stats[0], "Upper Quartile:", nRF4_stats[1], "Mean:", nRF4_stats[2], "Median:", nRF4_stats[3], "Standard Deviation:", nRF4_stats[4])
print("HS - Lower Quartile:", nHS_stats[0], "Upper Quartile:", nHS_stats[1], "Mean:", nHS_stats[2], "Median:", nHS_stats[3], "Standard Deviation:", nHS_stats[4])
print("Cal_JH - Lower Quartile:", nCALJH_stats[0], "Upper Quartile:", nCALJH_stats[1], "Mean:", nCALJH_stats[2], "Median:", nCALJH_stats[3], "Standard Deviation:", nCALJH_stats[4])
print("FAO56-PM - Lower Quartile:", nFAO56_PM_stats[0], "Upper Quartile:", nFAO56_PM_stats[1], "Mean:", nFAO56_PM_stats[2], "Median:", nFAO56_PM_stats[3], "Standard Deviation:", nFAO56_PM_stats[4])


# Plotting the boxplots

plt.figure(figsize = (10, 8))
plt.yticks(np.arange(0, 12.1, 0.5))
boxplots = plt.boxplot([nANN1_num, nRF2_num, nRF3_num, nRF4_num, nHS_num, nCALJH_num, nFAO56_PM_num], labels=['ANN1', 'RF2', 'RF3', 'RF4', 'HS', 'Cal_JH', 'FAO56-PM'], patch_artist=True, flierprops = flierprops, showmeans = True, medianprops=medianprops, meanprops=meanprops)
plt.ylabel(r'ETo, mm $d^{-1}$')
