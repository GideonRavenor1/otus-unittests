import numpy as np

from interfaces.matrix import IMatrix


class Matrix:
    
    def __init__(self, rows: int = 3, cols: int = 3) -> None:
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols))
        
    def set_size(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols))

    def set_value(self, row: int, col: int, value: float) -> None:
        self.data[row][col] = value

    def __add__(self, other: "IMatrix") -> "IMatrix":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same shape!")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_value(i, j, self.data[i][j] + other.data[i][j])
        return result

    def __str__(self) -> str:
        return str(self.data)
