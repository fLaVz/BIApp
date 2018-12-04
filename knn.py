# -*- coding: utf-8 -*

from pandas import DataFrame, read_csv
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd 
import sklearn
import numpy as np
import matplotlib.pyplot as plt


def read_file(file):
	#data.replace('nan','999999',inplace=True)
	#print(data)
	return pd.read_csv(file, encoding = "utf-8")

def drop_class_data(data):
	return data.loc[:, data.columns != 'CLASS']

def only_class_data(data):
	return data['CLASS']

def fit_data(data,classe):
	neigh = KNeighborsClassifier(n_neighbors=34, algorithm='auto')
	test = neigh.fit(data,classe)
	print(test)
	return neigh

def graphs_k(neigh,data):
	g = neigh.kneighbors_graph(data)
	print(g)

def acc_score(neigh,dataTest,classeTest):
	res = neigh.score(dataTest,classeTest)
	print("Précision du résultat : %f" % res)

def run_knn(tab):
	X = drop_class_data(tab[0])
	y = only_class_data(tab[0])
	neigh = fit_data(X,y)
	Xtest = drop_class_data(tab[1])
	Ytest = only_class_data(tab[1])
	acc_score(neigh,Xtest,Ytest)

#data = read_file("test2.csv")
#X = drop_class_data(data)
#Y = only_class_data(data)
#neigh = fit_data(X,Y)
#graphs_k(neigh,X)
#data_test = read_file("test3.csv")
#Xtest = drop_class_data(data_test)
#Ytest = only_class_data(data_test)
#acc_score(neigh,Xtest,Ytest)