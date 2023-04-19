import numpy as np

from interfaces.matrix import IMatrix


class MatrixGenerator:
    
    @staticmethod
    def generate(matrix: IMatrix) -> IMatrix:
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                matrix.set_value(i, j, np.random.random())
        return matrix
