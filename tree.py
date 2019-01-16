# -*- coding: utf-8 -*

from pandas import DataFrame, read_csv
from sklearn import tree as tr

import pandas as pd 
# import sklearn
from manager import timing
from termcolor import colored, cprint
import configparser as cp


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
	cprint("Précision du résultat : %f" % res, 'green')

@timing
def run_tree(tab, phase, type):
	X = drop_class_data(tab[0])
	y = only_class_data(tab[0])
	dec = fit_data(X,y)

	if phase == 'test':
		Xtest = drop_class_data(tab[1])
		Ytest = only_class_data(tab[1])
	elif phase == 'validation':
		Xtest = drop_class_data(tab[2])
		Ytest = only_class_data(tab[2])
		section = 'TREE' + type
		option = 'score'
		config = cp.ConfigParser()
		config.read('results.ini')
		config.set(section, option, str(acc_score(dec,Xtest,Ytest)))
		with open('results.ini', 'w') as configfile:
			config.write(configfile)

	show_accuracy(acc_score(dec,Xtest,Ytest))

