ANN1_corr = np.corrcoef(nANN1_num, nFAO56_PM_num)
RF2_corr = np.corrcoef(nRF2_num, nFAO56_PM_num)
RF3_corr = np.corrcoef(nRF3_num, nFAO56_PM_num)
RF4_corr = np.corrcoef(nRF4_num, nFAO56_PM_num)

HS_corr = np.corrcoef(nHS_num, nETO_num)
CALJH_corr = np.corrcoef(nCALJH_num, nETO_num)

corr = [ANN1_corr, RF2_corr, RF3_corr, RF4_corr, HS_corr, CALJH_corr]

ANN1_correlation = ANN1_corr[0, 1]
RF2_correlation = RF2_corr[0, 1]
RF3_correlation = RF3_corr[0, 1]
RF4_correlation = RF4_corr[0, 1]
HS_correlation = HS_corr[0, 1]
CALJH_correlation = CALJH_corr[0, 1]
