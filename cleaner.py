# -*- coding: utf-8 -*

import pandas as pd
import shutil

path1 = 'clean1.csv'
path2 = 'clean2.csv'
shutil.copy2('data/table1.csv', path1)
shutil.copy2('data/table2.csv', path2)
DATA_1 = pd.read_csv(path1, sep=',')
DATA_2 = pd.read_csv(path2, sep=',')

# Clean dates for table2.csv, needs refractor if format data
def cleanDate():
    for i, date in DATA_2.iterrows():
        #print(date)
        if '-' in date['DTNAIS']:
            DATA_2.drop(i, inplace=True)
    print('Dates like \'00-00-0000\' removed')
    DATA_2.to_csv(path2, sep=',', encoding='utf-8', index=False)


def cleanColumn(name):
    del DATA_1[name]
    DATA_1.to_csv(path1, sep=',', encoding='utf-8', index=False)
    print(name + ': deleted')


def cleanRange(name):
    DATA_1[name] = DATA_1[name].astype(str)    
    DATA_1.replace('nan', '0', inplace=True)
    for i, row in enumerate(DATA_1[name]):
        DATA_1.at[i, name] = str(row).split()[0]
    
    for i, row in enumerate(DATA_1['RANGAGEAD']):
        DATA_1.at[i, 'RANGAGEAD'] = str(row).split()[0]
    
    for i, row in enumerate(DATA_1['RANGAGEDEM']):
        if 'a' in str(row):
            DATA_1.at[i, 'RANGAGEDEM'] = '10'
        elif 'b' in str(row): 
            DATA_1.at[i, 'RANGAGEDEM'] = '11'
        else:
            DATA_1.at[i, 'RANGAGEDEM'] = str(row).split()[0]

    DATA_1.to_csv(path1, sep=',', encoding='utf-8', index=False)
    print(name + ': cleaned')


def mergetables():

    lendata1 = len(DATA_1)
    learn1 = int(lendata1 * 0.8)
    test1 = learn1 + int(lendata1 * 0.1)

    lendata2 = len(DATA_2)
    learn2 = int(lendata2 * 0.8)
    test2 = learn2 + int(lendata2 * 0.1)

    data1learn = DATA_1[:learn1]
    data1test = DATA_1[learn1:test1]
    data1val = DATA_1[test1:]

    data2learn = DATA_2[:learn2]
    data2test = DATA_2[learn2:test2]
    data2val = DATA_2[test2:]


    cols = ['CDSEXE', 'DTDEM', 'CDTMT', 'CDCATCL', 'DTADH', 'CDMOTDEM']
    df = pd.DataFrame(columns=cols)


# cleanDate('table2.csv')
# cleanColumn('RANGDEM', 'data/table1.csv')
# cleanRange('RANGADH', 'data/table1.csv')