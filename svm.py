import numpy as np
import matplotlib.pyplot as plt
# from sklearn import svm
import pandas as pd
from sklearn.svm import SVC
from matplotlib import style
style.use("ggplot")
from manager import timing
from termcolor import colored, cprint
import configparser as cp


# def Build_Data_Set(features = ["CDSITFAM", "MTREV"]):
    
#     data_df = pd.DataFrame.from_csv("data/table1.csv")
#     data_df = data_df[:100]

#     X = np.array(data_df[features].values)

#     y = (data_df["MTREV"]
#          .replace("underperform",0)
#          .replace("outperform",1)
#          .values.tolist())


#     return X,y

# def Analysis():
#     X, y = Build_Data_Set()

#     clf = svm.SVC(kernel="linear", C= 1.0)
#     clf.fit(X,y)
    
#     w = clf.coef_[0]
#     a = -w[0] / w[1]
#     xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
#     yy = a * xx - clf.intercept_[0] / w[1]

#     h0 = plt.plot(xx,yy, "k-", label="non weighted")

#     plt.scatter(X[:, 0],X[:, 1],c=y)
#     plt.ylabel("MTREV")
#     plt.xlabel("CDSEXE")
#     plt.legend()

#     plt.show()
    
# Analysis()

def read_file(file):
	return pd.read_csv(file, encoding = "utf-8")

def drop_class_data(data):
	return data.loc[:, data.columns != 'CLASS']

def only_class_data(data):
	return data['CLASS']

# def fit_data(data,classe):
	# svm = SVC(gamma='auto')
	# svm.fit(data,classe)
	# return svm

def acc_score(svm,dataTest,classeTest):
	#print("Précision du résultat : %f" % res)
	return svm.score(dataTest,classeTest)

def show_accuracy(res):
	cprint("Précision du résultat : %f" % res, 'green')


@timing
def run_svm(tab, phase, type):
	X = drop_class_data(tab[0])
	y = only_class_data(tab[0])
	svm = SVC(gamma='auto', kernel='rbf')
	svm.fit(X,y)

	if phase == 'test':	
		Xtest = drop_class_data(tab[2])
		Ytest = only_class_data(tab[2])
	elif phase == 'validation':
		Xtest = drop_class_data(tab[1])
		Ytest = only_class_data(tab[1])
		section = 'SVM_' + type
		option = 'score'
		config = cp.ConfigParser()
		config.read('results.ini')
		config.set(section, option, str(acc_score(svm,Xtest,Ytest)))
		with open('results.ini', 'w') as configfile:
			config.write(configfile)
	elif phase == 'apprentissage':
		Xtest = drop_class_data(tab[0])
		Ytest = only_class_data(tab[0])


	show_accuracy(acc_score(svm,Xtest,Ytest))
