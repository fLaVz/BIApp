# -*- coding: utf-8 -*

import pandas as pd

# Clean dates for table2.csv, needs refractor if format data
def cleanDate(fpath):
    data = pd.read_csv(fpath, sep=',')
    for i, date in data.iterrows():
        #print(date)
        if '-' in date['DTNAIS']:
            data.drop(i, inplace=True)
    print('Dates like \'00-00-0000\' removed')
    data.to_csv("test.csv", sep=',', encoding='utf-8', index=False)


cleanDate('table2.csv')

def cleanColumn(name, fpath):
    pass

    