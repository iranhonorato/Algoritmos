from typing import List 


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tam = len(matrix)
    

        for row in range(0, tam-1):
            for col in range(0, tam-row-1):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[tam-1-col][tam-1-row]
                matrix[tam-1-col][tam-1-row] = tmp 

        up = 0 
        down = tam-1

        while up < down:
            tmp = matrix[up]
            matrix[up] = matrix[down] 
            matrix[down] = tmp

            up += 1
            down -= 1 

        return 



