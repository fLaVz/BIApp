import sys
import cleaner
import knn

if __name__ == "__main__":
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    merge = cleaner.mergetables()
    knn.run_knn(merge)