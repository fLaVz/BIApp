import sys
import cleaner
import knn

if __name__ == "__main__":

    # Knn basic
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    merge = cleaner.mergetablesKnn('base')
    knn.run_knn(merge, 34)
    # knn.make_graph(1,101,1,merge,"graphKnn")

    # Knn evolved
    merge = cleaner.mergetablesKnn('evolved')
    knn.run_knn(merge, 3)
    # knn.make_graph(1,101,1,merge,"graphKnn2")