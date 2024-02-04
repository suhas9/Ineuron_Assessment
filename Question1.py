'''Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:

1.Integers in each row are sorted from right to left.

2.The first integer of each row is greater than the last integer of the previous row.

    Example-: 

        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

        Output: True'''

import numpy as np
matrix = np.array([[1,3,5,7],[10,11,16,20],[23,30,34,60]])
def find_number(mat,target):
    res = any(target in sub for sub in mat)
    print(res)
            
def main():
    matrix = np.array([[1,3,5,7],[10,11,16,20],[23,30,34,60]])
    find_number(matrix,3)                   
 
if __name__=="__main__":
    main() 