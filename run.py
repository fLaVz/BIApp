import sys
import cleaner

if __name__ == "__main__":
    cleaner.cleanDate()
    cleaner.cleanColumn('RANGDEM')
    cleaner.cleanRange('RANGADH')
    cleaner.mergetables()