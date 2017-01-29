import pandas as pd
from List import get_filepaths
import csv


match = (r'^(.*)((((0[1-9])|([1-2][0-9])|(3[0-1]))|([1-9]))(\s|\-|\x2F)((Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember|January|February|March|May|June|July|August|October|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Mei|Agu|Okt|Des)|(((0[1-9])|(1[0-2]))|([1-9])))(\s|\-|\x2F)(((19)|([2]([0]{1})))([0-9]{2})))s*')
filenames = get_filepaths(r"C:\Users\firlyarmanda\PycharmProjects\Ekstraksi_Metadata\EM-TCver1")
index = 0
for f in filenames:
    file_html=open(str(f),"r")
    dataf = pd.read_csv(file_html)
    df = dataf.dropna() #menghilangkan kolom NaN
    candidate_groups = df.groupby('candidate')
    tag_groups = df.groupby(df.index)

    final_text_list = []

    Tanggal = '\n'.join(df['Words'][df['Words'].str.contains(match)].head(1))#Aturan tanggal yang ditemukan pertama
    for _, group_df in tag_groups:
        if group_df[(group_df['TAG'].str.contains('h1').any()) & (group_df['LTC'] == 0) & (group_df['TC'].sum() > 1)].shape[0] > 0: #aturan Judul yang mengandung h1
            Judul = '\n'.join(group_df['Words'].astype(str))

    for _, group_df in candidate_groups:
        if group_df['TC'].sum() > 40:  # 40 is the threshold, aturan isi
            Isi = '\n'.join(group_df['Words'].astype(str))
    final_text =[Judul, Tanggal,Isi]
    final_text_list.append(final_text)

    index += 1
    stored_file = "EM-TVver1/" + '{0:03}'.format(index) + ".csv"
    firstline = ["Judul"," Tanggal", "Isi Berita"]
    filewrite = open(stored_file, "wb")
    writer = csv.writer(filewrite, lineterminator='\n')
    writer.writerow(firstline)
    for val in final_text_list:
        writer.writerow(val)
    filewrite.close


