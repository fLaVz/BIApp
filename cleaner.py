# -*- coding: utf-8 -*

import pandas as pd

# Clean dates for table2.csv, needs refractor if format data
def cleanDate():
    data = pd.read_csv('table2.csv', sep=',')
    for i, date in data.iterrows():
        #print(date)
        if '-' in date['DTNAIS']:
            data.drop(i, inplace=True)
    print('Dates like \'00-00-0000\' removed') 


cleanDate()



    #def clean