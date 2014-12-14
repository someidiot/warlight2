from math import fmod, pi
from time import clock

class Random(object):
    '''
    Random class
    '''
    @staticmethod
    def randrange(min, max):
        '''
        A pseudo random number generator to replace random.randrange
        
        Works with an inclusive left bound and exclusive right bound.
        E.g. Random.randrange(0, 5) in [0, 1, 2, 3, 4] is always true
        '''
        return min + int(fmod(pow(clock() + pi, 2), 1.0) * (max - min))

    @staticmethod
    def shuffle(items):
        '''
        Method to shuffle a list of items
        '''
        i = len(items)
        while i > 1:
            i -= 1
            j = Random.randrange(0, i)
            items[j], items[i] = items[i], items[j]
        return items
