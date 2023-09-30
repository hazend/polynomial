"""
An implementation of a ``Polynomial`` class, with some useful features

"""
# Libraries
import numpy as np

class Polynomial():
    '''
    The polynomial instance defined by this class is a vector of 
    coefficiants, p = [[a_0], [a_1], [a_2], ....[a_n]] such that 
    polynomial = p.x = a_0 + a_1x + a_2x^2 +....+ a_nx^n.

    Default initialization for n = 100.
    '''
    def __init__(self, p, n=10):
        '''
        ``p`` is a list-like of coefficiants in order [[a_0], [a_1], [a_2], ....[a_n]].
        ``n`` is the degree of polynomial, by default n=10
        '''
        self.n = n
        self.p = p

    # def 