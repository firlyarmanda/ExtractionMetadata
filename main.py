import pandas as pd

df = pd.read_csv('Smoothing/Smoothing008.csv')

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
    TB = tb.copy()
    for key, value in tb.iteritems():
        if key == len(tb) - 1:
            break
        elif value['end'] == tb[key+1]['end']:
            del TB[key+1]
    return TB

def remove_overlap_candidate(tb):
    TB = get_unique(tb)
    keys = TB.keys()
    for index in range(len(keys)-1):
        if TB[keys[index]]['start'] < TB[keys[index+1]]['start'] < TB[keys[index]]['end'] < TB[keys[index+1]]['end']:
            TB[keys[index]]['end'] = TB[keys[index+1]]['start'] - 1
        else:
            continue
    return TB

tb = create_candidates(df, 6, 10)
TB = remove_overlap_candidate(tb)

for x, vl in TB.iteritems():
    print x, vl
