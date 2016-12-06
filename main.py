import pandas as pd

df = pd.read_csv('Smoothing/Smoothing002.csv')

def create_candidates(df, thetaCTTD, thetaGAP):
    k = 0
    TB = {}
    TC = 0
    for index in range(0, len(df) - 1):
        start = index
        if df.ix[index]['CTTDs'] > thetaCTTD:
            start = index
            gap = 0
            TC = df.ix[index]['TC']
            for index in range(index + 1, len(df) - 1):
                if df.ix[index]['TG'] == 0:
                    continue
                elif df.ix[index]['CTTDs'] <= thetaCTTD and gap >= thetaGAP:
                    break
                elif df.ix[index]['CTTDs'] <= thetaCTTD:
                    gap += 1
                TC += df.ix[index]['TC']
        if (TC < 1) or (start == index):
            continue
        TB.update({
            k: {
                'start': start,
                'end': index - 1
            }
        })
        k += 1
    return TB


def get_unique(tb):
    tb_copy = tb.copy()
    for key, value in tb.iteritems():
        if key == len(tb) - 1:
            break
        elif value['end'] == tb[key+1]['end']:
            del tb_copy[key+1]
    return tb_copy


def remove_overlap_candidate(tb):
    tb = get_unique(tb)
    keys = tb.keys()
    for index in range(len(keys)-1):
        if (tb[keys[index]]['start'] <
                tb[keys[index+1]]['start'] <
                tb[keys[index]]['end'] <
                tb[keys[index+1]]['end']):
            tb[keys[index]]['end'] = tb[keys[index+1]]['start'] - 1
        else:
            continue
    return tb

text_box = create_candidates(df, 6, 10)
TB_clean = remove_overlap_candidate(text_box)

idx = []
for key, value in TB_clean.iteritems():
    idx = idx + (range(value['start'], value['end']))

df = df.ix[idx]
df = df.reset_index()

text_box_main_content = create_candidates(df, 15, 10)
TB_clean_main_content = remove_overlap_candidate(text_box_main_content)

idx = []

for key, value in TB_clean_main_content.iteritems():
    idx = idx + (range(value['start'], value['end']))

df_main = df.ix[idx]
df_main = df_main.reset_index(drop=True)
df_main.to_csv('content.csv')
df_title = df.drop(df.index[idx])
df_title[df_title['TC'] > 0].to_csv('title_date.csv')