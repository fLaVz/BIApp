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
    f.write('[KNN_base]\n[SVM_base]\n[TREE_base]\n[KNN_evolved]\n[SVM_evolved]\n[TREE_evolved]')
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

    ######################################################################################################
    # basic
    cprint('Phase d\'apprentissage', 'red')
    print('Version Basique')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_base, 34, 'apprentissage', 'base')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_base, 'apprentissage', 'base')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_base, 'apprentissage', 'base')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # evolved
    print('Version Evoluée')
    cprint('Knn en cours...', 'cyan')
    knn.run_knn(merge_evo, 34, 'apprentissage', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('SVM en cours...', 'cyan')
    svm.run_svm(merge_evo, 'apprentissage', 'evolved')
    print('-----------------------------------------------------------------')
    cprint('Arbre de décision en cours...', 'cyan')
    tree.run_tree(merge_evo, 'apprentissage', 'evolved')
    print('-----------------------------------------------------------------')
    print('=================================================================')
    # logistic.run_logistic(merge)
    #knn.feature_ablation(merge, 34)
    # knn.best_knn(1,101,10,merge)

######################################################################################################

    # basic
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

    # evolved
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

######################################################################################################

    ## test
    print('=================================================================')
    cprint('Phase de test', 'red')
    data = manager.define_best()
    print('La meilleure combinaison est: ' + data[0] + ' avec le jeu: ' + data[1])

    if data[0] == 'KNN':
        if data[1] == 'base':
            knn.run_knn(merge_base, 34, 'test', data[1])
        if data[1] == 'evolved':
            knn.run_knn(merge_evo, 34, 'test', data[1])
    elif data[0] == 'SVM':
        if data[1] == 'base':
            svm.run_svm(merge_base, 'test', data[1])
        if data[1] == 'evolved':
            svm.run_svm(merge_evo,'test', data[1])
    elif data[0] == 'TREE':
        if data[1] == 'base':
            tree.run_tree(merge_base, 'test', data[1])
        if data[1] == 'evolved':
            tree.run_tree(merge_evo, 'test', data[1])
    
    # knn.make_graph(1, 101, 10, merge, "graphKnn2test")