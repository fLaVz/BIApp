import sys
import cleaner
import knn
import svm
import tree
import logistic

if __name__ == "__main__":

    # Knn basic
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    merge = cleaner.mergetablesKnn('base')
    print("Knn en cours...")
    knn.run_knn(merge, 34)
    print("SVM en cours...")
    svm.run_svm(merge)
    print("Arbre de décision en cours...")
    tree.run_tree(merge)
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # Knn evolved
    merge = cleaner.mergetablesKnn('evolved')
    print("Knn en cours...")
    knn.run_knn(merge, 34)
    print("SVM en cours...")
    # svm.run_svm(merge)
    print("Régréssion logistique en cours...")
    # logistic.run_logistic(merge)
    print("Arbre de décision en cours...")
    tree.run_tree(merge)
    print('=================================================================')
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)
    
    
    # knn.make_graph(1, 101, 10, merge, "graphKnn2test")