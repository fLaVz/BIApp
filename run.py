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
    knn.run_knn(merge, 34)
    # svm.run_svm(merge)
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # Knn evolved
    merge = cleaner.mergetablesKnn('evolved')
    knn.run_knn(merge, 34)
    # svm.run_svm(merge)
    print('=================================================================')
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)
    # logistic.run_logistic(merge)
    # tree.run_tree(merge)
    
    # knn.make_graph(1, 101, 10, merge, "graphKnn2test")