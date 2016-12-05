import pandas as pd

df = pd.read_csv('Smoothing/Smoothing001.csv')

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

def get_unique_candidate(TB):
    TB = tb.copy()
    for key, value in tb.iteritems():
        if key == len(tb) - 1:
            break
        if value['end'] == tb[key+1]['end']:
            del TB[key+1]
        elif value['start'] < tb[key+1]['start'] < value['end']:
            TB[key]['end'] = tb[key+1]['start'] - 1
        else:
            continue
    return TB

tb = create_candidates(df, 6, 10)
TB = get_unique_candidate(tb)

for x in TB.iteritems():
    print x