import sys
import cleaner
import knn

if __name__ == "__main__":

    # Knn basic
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    merge = cleaner.mergetablesKnn('base')
    knn.run_knn(merge)

    # Knn evolved
    merge = cleaner.mergetablesKnn('evolved')
    knn.run_knn(merge)