from ListTD import get_filepaths_td
import pandas as pd
import numpy as np

filenames = get_filepaths_td(r"C:\Users\firlyarmanda\PycharmProjects\EkstraksiBerita\textdetection")
index = 0
for f in filenames:
    file_html=open(str(f),"r")
    df = pd.read_csv(file_html)
#cttd = df['CTTD']
#print cttd

    vals = np.append(np.append([0, 0], df['CTTD']), [0, 0])
    cttds = np.array([vals[i - 2] + 2 * vals[i - 1] + 4 * vals[i] + 2 * vals[i + 1] + vals[i + 2] for i in range(2, len(vals) - 2)]) / 10.

    index += 1
    stored_file = "smoothing\Smoothing" + '{0:03}'.format(index) + ".csv"
    filewrite = open(stored_file, "w")
    df['CTTDs'] = cttds
    filewrite.close
    df.to_csv(filewrite)

#def calc_new_cttd(series):
    #vals = series.values
    #cttds = np.array([vals[i-2] + 2*vals[i-1] + 4*vals[i] + 2*vals[i+1] + vals[i+2] for i in range(2,len(vals)-2)])/10.
    #return np.append(np.append([0,0], cttds),[0,0])
#calc_new_cttd(df["CTTD"])
#df["transformed_cttd"] = calc_new_cttd(df["CTTD"])
#df.to_csv("book2.csv")
