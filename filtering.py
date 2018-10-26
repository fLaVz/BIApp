# -*- coding: utf-8 -*

import mrs
import glob
import sys
import re


# Regarde la distribution des valeurs si discrètes -> valeurs abbérantes etc ..

class WordCount(mrs.MapReduce):

    def input_data(self, job):
        repo = self.args[0]
        print(repo)
        fileList = glob.glob(repo + '/*.csv')
        print(fileList)
        print('\n ----------------------------------------------------------------- \n')
        return job.file_data(fileList)

    def map(self, key, value):

        #print(value)
        #print('\n ----------------------------------------------------------------- \n')
        #print('\n ----------------------------------------------------------------- \n')
        enc = value.split(',')
        #print(enc)
        #print('\n ----------------------------------------------------------------- \n')
        #print('\n ----------------------------------------------------------------- \n')
        
        id = 'ID'
        if enc[0] != id:
            yield enc[14], 1

    def reduce(self, key, value):
        #print(value)
        
        yield len(tuple(value))


if __name__ == '__main__':
    mrs.main(WordCount)