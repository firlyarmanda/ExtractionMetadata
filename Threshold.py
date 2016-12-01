from ListSmoothing import get_filepaths_smoothing
import pandas as pd
import numpy as np
import csv

filenames = get_filepaths_smoothing(r"C:\Users\firlyarmanda\PycharmProjects\EkstraksiBerita\smoothing")


index = 0
ress = []
for f in filenames:
    file_html=open(str(f),"r")
    df = pd.read_csv(file_html)
    news = np.array(df['CTTDs'])
    new = np.array(df['TG'])
    minval = np.min(news[np.nonzero(news)])
    maxval = np.max(news[np.nonzero(news)])
    th_gap = np.max(new[np.nonzero(new)])
    k = 0.5
    th_cttd = minval + (k * (maxval - minval))
    res = [minval, maxval, th_gap, th_cttd]
    ress.append(res)

    firstline = ["Minimun CTTD", "Maximum CTTD", "Threshold_Gap", "Threshold_CTTD"]
    index += 1
    stored_file = "TH/threshold" + '{0:03}'.format(index) + ".csv"
    filewrite = open(stored_file, "wb")
    writer = csv.writer(filewrite, lineterminator='\n')
    writer.writerow(firstline)
    #for val in ress:
    writer.writerow(res)
    filewrite.close






