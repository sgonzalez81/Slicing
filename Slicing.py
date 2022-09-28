# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:11:48 2022

@author: salva

Use numpy.array to define a 3-by-7 array, A.  In array location (i,j), row i, column j,  put the number i*j

Use slicing to produce and print:

1)  row 2 of A

2) row 2 of A in reverse order

3) the sub-matrix consisting or the bottom right 2x2 sub-array 

4) the sub-array consisting of the bottom left 2x2 sub-array

5) the 3x3 sub-array in the middle of A
"""
import numpy as np

A = np.zeros(shape = (3,7))

for i in range(3):
    for j in range(7):
        A[i,j] = i*j
        
        print(f"row 2 of A: {A[2,:]}")
        print(f"row 2 of A, reverse order: {A[1:,5:]}")
        
        print(f"sub matrix botom right 2x2 {A[1:,5:]}")
        
        print(A[1:,:2])
        
        print(A[:,2:5])
        