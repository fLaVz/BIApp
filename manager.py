# -*- coding: utf-8 -*

from functools import wraps
from time import time
import configparser as cp


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end-start))
        exec_time = format(end-start)
        # get name + phase of function via magic method
        section = f.__name__.split('_')[1].upper() + '_' + args[len(args) - 1]
    
        if args[len(args) - 2] == 'validation':
            config = cp.ConfigParser()
            config.read('results.ini')
            config.set(section, 'exec_time', str(exec_time))
            with open('results.ini', 'w') as configfile:
                config.write(configfile)

        return result
    return wrapper

def define_best():
    config = cp.ConfigParser()
    config.read('results.ini')

    best_score = 100
    method = 'default'

    for section in config.sections():
        tmp = config.getfloat(section, 'exec_time') / config.getfloat(section, 'score')
        if tmp < best_score:
            best_score = tmp
            method = section

    best = [method.split('_')[0], method.split('_')[1]]
    return best