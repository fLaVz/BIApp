import sys
import cleaner
import knn
import svm
import tree
import logistic
from termcolor import colored, cprint
import manager

def init_file():
    f = open('results.ini', 'w')
    f.write('[KNNbase]\n[SVMbase]\n[TREEbase]\n[KNNevolved]\n[SVMevolved]\n[TREEevolved]')
    f.close()


if __name__ == "__main__":

    ## Apprentissage
    # clean result file
    init_file()
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
    knn.run_knn(merge_base, 34, 'test', 'base')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_base, 'test', 'base')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_base, 'test', 'base')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # evolved
    print('Version Evoluée')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_evo, 34, 'test', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_evo, 'test', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_evo, 'test', 'evolved')
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
    knn.run_knn(merge_base, 34, 'validation', 'base')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_base, 'validation', 'base')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_base, 'validation', 'base')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # Knn evolved
    print('Version Evoluée')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_evo, 34, 'validation', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_evo, 'validation', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_evo, 'validation', 'evolved')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # logistic.run_logistic(merge)
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)

    print( 'Le meilleur résultat est: ' + str(manager.define_best()))
    
    
    # knn.make_graph(1, 101, 10, merge, "graphKnn2test")