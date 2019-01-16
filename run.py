import sys
import cleaner
import knn
import svm
import tree
import logistic
from termcolor import colored, cprint

if __name__ == "__main__":

    ## Apprentissage
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    print("Unification des tables...")
    merge_base = cleaner.mergetables('base')
    merge_evo = cleaner.mergetables('evolved')

    # basic
    cprint('Phase d\'apprentissage', 'red')
    print('Version Basique')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_base, 34, 'test')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_base, 'test')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_base, 'test')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # evolved
    print('Version Evoluée')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_evo, 34, 'test')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_evo, 'test')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_evo, 'test')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # logistic.run_logistic(merge)
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)

    ## Validation
    print('=================================================================')
    cprint('Phase de validation', 'red')
    print('Version Basique')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_base, 34, 'validation')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_base, 'validation')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_base, 'validation')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # Knn evolved
    print('Version Evoluée')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_evo, 34, 'validation')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_evo, 'validation')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_evo, 'validation')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # logistic.run_logistic(merge)
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)

    
    
    # knn.make_graph(1, 101, 10, merge, "graphKnn2test")