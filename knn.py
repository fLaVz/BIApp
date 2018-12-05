# -*- coding: utf-8 -*

from pandas import DataFrame, read_csv
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd 
import sklearn
import numpy as np
import matplotlib
matplotlib.use("Agg")
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
	neigh.fit(data,classe)
	return neigh

def fit_data2(data,classe,n):
	neigh = KNeighborsClassifier(n_neighbors=n, algorithm='auto')
	neigh.fit(data,classe)
	return neigh

def acc_score(neigh,dataTest,classeTest):
	#print("Précision du résultat : %f" % res)
	return neigh.score(dataTest,classeTest)

def run_knn(tab, neighbors):
	X = drop_class_data(tab[0])
	y = only_class_data(tab[0])
	neigh = fit_data2(X,y, neighbors)
	Xtest = drop_class_data(tab[1])
	Ytest = only_class_data(tab[1])
	show_accuracy(acc_score(neigh,Xtest,Ytest))

def make_graph(start, end, step, tab, nameFig):
	print("Création du graphe en cours")
	t = np.array(0.)
	t2 = np.array(0)
	for i in range(start,end,step):
		# print(i)
		t2 = np.append(t2,i)
		X = drop_class_data(tab[0])
		y = only_class_data(tab[0])
		neigh = fit_data2(X,y,i)
		Xtest = drop_class_data(tab[1])
		Ytest = only_class_data(tab[1])
		t = np.append(t,acc_score(neigh,Xtest,Ytest))
	figure = pd.Series(t, index=t2)
	figure.plot(kind='line')
	plt.title("Graphique des scores")
	plt.xlabel("Nombre de voisin")
	plt.ylabel("Score")
	plt.savefig(nameFig)
	plt.show()
	print("Graphe créé !")

def show_accuracy(res):
	print("Précision du résultat : %f" % res)

#data = read_file("test2.csv")
#X = drop_class_data(data)
#Y = only_class_data(data)
#neigh = fit_data(X,Y)
#graphs_k(neigh,X)
#data_test = read_file("test3.csv")
#Xtest = drop_class_data(data_test)
#Ytest = only_class_data(data_test)
#acc_score(neigh,Xtest,Ytest)