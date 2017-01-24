import pandas as pd


dataf = pd.read_csv('9.csv')
df = dataf.dropna() #menghilangkan kolom NaN
candidate_groups = df.groupby('candidate')

for _, group_df in candidate_groups:
    if group_df['TC'].sum() > 30 : # 30 is the threshold
        print '\n'.join(group_df['Words'].astype(str))

    elif group_df[(group_df['TAG'] == "['h1']") & (group_df['LTC'] == 0) & (group_df['TC'] > 0)].shape[0] > 0:
        print '\n'.join(group_df['Words'].astype(str))