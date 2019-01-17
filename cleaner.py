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


def mergetables(type):
    df1 = pd.read_csv('clean1.csv')
    df2 = pd.read_csv('clean2.csv')
    df1['CLASS'] = 1
    df2 = addTarget(df2)

    if type == 'base':  
        print('Unification simple')
        cols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDCATCL', 'CDSITFAM', 'CLASS']
        # dftest = pd.read_csv('clean1.csv', usecols=cols)
    elif type == 'evolved':
        print('Unification complexe')
        df2['AGEAD'] = list(map(sub_year, zip(df2['DTADH'], df2['DTNAIS'])))
        df2['AGEDEM'] = list(map(sub_year, zip(df2['DTDEM'], df2['DTNAIS'])))
        cols = ['CDSEXE', 'MTREV', 'NBENF', 'CDTMT', 'CDSITFAM', 'CDCATCL', 'AGEAD', 'AGEDEM', 'CLASS']

    clean1 = pd.DataFrame(df1, columns=cols)
    clean1 = getDumm(clean1)
    clean2 = pd.DataFrame(df2, columns=cols)
    clean2 = getDumm(clean2)
    
    cols = list(clean2)
    
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
    
    alldata = [m_learn, m_validate, m_test]
    return alldata

def getDumm(df):
    cat = ['CDSEXE', 'CDSITFAM', 'CDTMT', 'CDCATCL']
    dumm = pd.get_dummies(df, columns=cat)
    return dumm


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
    

# def mergetables_knn_eq():
#     clean1 = pd.read_csv('clean1.csv')
#     clean2 = pd.read_csv('clean2.csv')

#     clean1['CLASS'] = 1
#     clean2 = addTarget(clean2)
#     print(clean2)
    


# cleanDate('table2.csv')
# cleanColumn('RANGDEM', 'data/table1.csv')
# cleanRange('RANGADH', 'data/table1.csv')