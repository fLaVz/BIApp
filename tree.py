# -*- coding: utf-8 -*

from pandas import DataFrame, read_csv
from sklearn import tree as tr

import pandas as pd 
# import sklearn


def read_file(file):
	return pd.read_csv(file, encoding = "utf-8")

def drop_class_data(data):
	return data.loc[:, data.columns != 'CLASS']

def only_class_data(data):
	return data['CLASS']

def fit_data(data,classe):
	dectree = tr.DecisionTreeClassifier()
	dectree.fit(data,classe)
	return dectree

def acc_score(neigh,dataTest,classeTest):
	return neigh.score(dataTest,classeTest)

def show_accuracy(res):
	print("Précision du résultat : %f" % res)

def run_tree(tab):
    X = drop_class_data(tab[0])
    y = only_class_data(tab[0])
    dec = fit_data(X,y)
    Xtest = drop_class_data(tab[1])
    Ytest = only_class_data(tab[1])
    show_accuracy(acc_score(dec,Xtest,Ytest))
