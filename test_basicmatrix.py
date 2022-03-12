'''
Unit Test for BasicMatrix
Author: Christiaan van Eeden
Version: 0.1
'''

#import packages
from basicmatrix import BasicMatrix
import numpy as np

#Array init for testing class methods
X = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
Y = np.array([[0, 1], [2, 3], [4, 5]])
XY = np.array([[10, 13], [28, 40], [46, 67]])
XX = np.array([[15, 18, 21], [42, 54, 66], [69, 90, 111]])
aXX = np.array([[0, 2, 4], [6, 8, 10], [12, 14, 16]])
sXX = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_setget_matrix():
    '''
    Test set and get methods
    '''
    m1 = BasicMatrix(2, 3)
    m1.set_matrix(X)
    assert(m1.get_matrix().all() == X.all())
    
def test_shape():
    '''
    Test shape method
    '''
    m1 = BasicMatrix(3, 2)
    m1.set_matrix(X)
    assert(m1.shape() == (3, 3))

def test_dot1():
    '''
    Test different shape matrices of dot method
    '''
    m1 = BasicMatrix(3, 3)
    m1.set_matrix(X)
    m2 = BasicMatrix(3, 2)
    m2.set_matrix(Y)
    assert(BasicMatrix.dot(m1, m2).all() == XY.all())
    
def test_dot2():
    '''
    Test same shape matrices of dot method
    '''
    m1 = BasicMatrix(3, 3)
    m1.set_matrix(X)
    m2 = BasicMatrix(3, 3)
    m2.set_matrix(X)
    assert(BasicMatrix.dot(m1, m2).all() == XX.all())
    
def test_add():
    '''
    Test same shape matrices of add dunder method
    '''
    m1 = BasicMatrix(3, 3)
    m1.set_matrix(X)
    m2 = BasicMatrix(3, 3)
    m2.set_matrix(X)
    assert((m1 + m2).all() == aXX.all())
    
def test_sub():
    '''
    Test same shape matrices of subtract dunder method
    '''
    m1 = BasicMatrix(3, 3)
    m1.set_matrix(X)
    m2 = BasicMatrix(3, 3)
    m2.set_matrix(X)
    assert((m1 - m2).all() == sXX.all())
    
    
    
    
    
    