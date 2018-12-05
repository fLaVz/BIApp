# -*- coding: utf-8 -*

import pandas as pd
import shutil
from datetime import datetime


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


def mergetablesKnn(type):

    clean1 = pd.read_csv('clean1.csv')
    clean2 = pd.read_csv('clean2.csv')
    dumm1 = pd.get_dummies(clean1['CDSITFAM'])
    dumm2 = pd.get_dummies(clean2['CDSITFAM'])
    
    if type == 'base':  
        cols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDCATCL', 'CLASS']
        numcols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDCATCL', 'CLASS']
        # dftest = pd.read_csv('clean1.csv', usecols=cols)
    elif type == 'evolved':
        clean2['AGEAD'] = list(map(sub_year, zip(clean2['DTADH'], clean2['DTNAIS'])))
        clean2['AGEDEM'] = list(map(sub_year, zip(clean2['DTDEM'], clean2['DTNAIS'])))
        cols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDCATCL', 'AGEAD', 'AGEDEM', 'CLASS']
        numcols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDCATCL', 'AGEAD', 'AGEDEM', 'CLASS']

    cols += list(dumm2)
    clean1['CLASS'] = 1
    clean2 = addTarget(clean2)
    clean1 = clean1[numcols].add(dumm1, fill_value=0)
    clean2 = clean2[numcols].add(dumm2, fill_value=0)

    lendata1 = len(clean1)
    learn1 = int(lendata1 * 0.8)
    test1 = learn1 + int(lendata1 * 0.1)

    lendata2 = len(clean2)
    learn2 = int(lendata2 * 0.8)
    test2 = learn2 + int(lendata2 * 0.1)

    data1learn = clean1[:learn1]
    data1test = clean1[learn1:test1]
    data1val = clean1[test1:]

    data2learn = clean2[:learn2]
    data2test = clean2[learn2:test2]
    data2val = clean2[test2:]

    m_learn = data1learn[cols].append(data2learn[cols])
    m_validate = data1test[cols].append(data2test[cols])
    m_test = data1val[cols].append(data2val[cols])
    
    # for tests purposes
    m_learn.to_csv('test.csv', sep=',', encoding='utf-8', index=False)
    
    alldata = [m_learn, m_test, m_validate]
    return alldata


def addTarget(df):
    df['CDMOTDEM'] = df['CDMOTDEM'].astype(str)
    df['CLASS'] = 1
    df.replace('nan', '0', inplace=True)
    for i, row in enumerate(df['CDMOTDEM']):
        if str(row) == '0':
            df.at[i, 'CLASS'] = 0
    return df
    
def sub_year(item):
    if int(item[0].split('/')[2]) != 1900:
        return int(item[0].split('/')[2]) - int(item[1].split('/')[2])
    else:
        return 2007 - int(item[1].split('/')[2])
    

def mergetables_knn_eq():
    clean1 = pd.read_csv('clean1.csv')
    clean2 = pd.read_csv('clean2.csv')

    clean1['CLASS'] = 1
    clean2 = addTarget(clean2)
    


# cleanDate('table2.csv')
# cleanColumn('RANGDEM', 'data/table1.csv')
# cleanRange('RANGADH', 'data/table1.csv')