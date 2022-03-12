'''
Time Evaluation Test
Author: Christiaan van Eeden
Version: 0.1
'''

#import packages
from basicmatrix import BasicMatrix
import numpy as np
import time

#Init matrices for testing
X = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
XX = np.array([[15, 18, 21], [42, 54, 66], [69, 90, 111]])


m1 = BasicMatrix(3, 3)
m2 = BasicMatrix(3, 3)
m1.set_matrix(X)
m2.set_matrix(X)

def time_dot():
    '''
    Dot product time test
    '''
    start1 = time.time()
    m3 = BasicMatrix.dot(m1, m2)
    print(m3)
    print('Duration for BasicMatrix dot: {} seconds'.format(time.time() - start1))
    
    start2 = time.time()
    m3 = np.dot(m1.get_matrix(), m2.get_matrix())
    print(m3)
    print('Duration for BasicMatrix dot: {} seconds'.format(time.time() - start2))
    
time_dot()

