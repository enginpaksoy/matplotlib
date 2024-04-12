# Reading the data from the excel file according to the user's specifications
ANN1  = pd.read_excel(file_path, usecols='O', skiprows=1, nrows=1411)
RF2   = pd.read_excel(file_path, usecols='P', skiprows=1, nrows=1411)
RF3  = pd.read_excel(file_path, usecols='Q', skiprows=1, nrows=1411)
RF4 = pd.read_excel(file_path, usecols='R', skiprows=1, nrows=1411)
HS = pd.read_excel(file_path, usecols='E', skiprows=1, nrows=1499)
CALJH = pd.read_excel(file_path, usecols='F', skiprows=1, nrows=1499)

# Converting the data to NumPy arrays
ANN1_num = ANN1.to_numpy().flatten()
RF2_num = RF2.to_numpy().flatten()
RF3_num = RF3.to_numpy().flatten()
RF4_num = RF4.to_numpy().flatten()
HS_num = HS.to_numpy().flatten()
CALJH_num = CALJH.to_numpy().flatten()

medianprops = dict(linestyle='-', linewidth=2, color='red')
meanprops = dict(marker='+', markeredgecolor='black', markerfacecolor='blue')
flierprops = dict(marker='o', markeredgecolor='red', markersize=16)

ANN1_stats = calculate_statistics(ANN1_num)
RF2_stats = calculate_statistics(RF2_num)
RF3_stats = calculate_statistics(RF3_num)
RF4_stats = calculate_statistics(RF4_num)
HS_stats = calculate_statistics(HS_num)
CALJH_stats = calculate_statistics(CALJH_num)

print("ERROR ANN1 - Lower Quartile:", ANN1_stats[0], "Upper Quartile:", ANN1_stats[1], "Mean:", ANN1_stats[2], "Median:", ANN1_stats[3], "Standard Deviation:", ANN1_stats[4])
print("ERROR RF2 - Lower Quartile:", RF2_stats[0], "Upper Quartile:", RF2_stats[1], "Mean:", RF2_stats[2], "Median:", RF2_stats[3], "Standard Deviation:", RF2_stats[4])
print("ERROR RF3 - Lower Quartile:", RF3_stats[0], "Upper Quartile:", RF3_stats[1], "Mean:", RF3_stats[2], "Median:", RF3_stats[3], "Standard Deviation:", RF3_stats[4])
print("ERROR RF4 - Lower Quartile:", RF4_stats[0], "Upper Quartile:", RF4_stats[1], "Mean:", RF4_stats[2], "Median:", RF4_stats[3], "Standard Deviation:", RF4_stats[4])
print("ERROR HS - Lower Quartile:", HS_stats[0], "Upper Quartile:", HS_stats[1], "Mean:", HS_stats[2], "Median:", HS_stats[3], "Standard Deviation:", HS_stats[4])
print("ERROR CALJH - Lower Quartile:", CALJH_stats[0], "Upper Quartile:", CALJH_stats[1], "Mean:", CALJH_stats[2], "Median:", CALJH_stats[3], "Standard Deviation:", CALJH_stats[4])

# Plotting the boxplots
plt.figure(figsize = (10, 8))
plt.yticks(np.arange(0, 4.1, 0.5))
boxplots = plt.boxplot([ANN1_num, RF2_num, RF3_num, RF4_num, HS_num, CALJH_num], labels=['ANN1', 'RF2', 'RF3', 'RF4', 'HS', 'Cal_JH'], flierprops = flierprops, patch_artist=True, showmeans = True, medianprops=medianprops, meanprops=meanprops)
plt.ylabel(r'Prediction Errors, mm $d^{-1}$')
