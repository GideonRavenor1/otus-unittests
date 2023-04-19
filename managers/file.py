import os

from interfaces.matrix import IMatrix


class FileManager:
    
    @staticmethod
    def read(filename: str) -> list[int]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(filename, "r", encoding="utf-8") as f:
            arr = f.readline().strip().split()
            return [int(x) for x in arr]
    
    @staticmethod
    def write(filename: str, arr: list[int]) -> None:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(" ".join(map(str, arr)))


class MatrixFileManager:
    
    @staticmethod
    def from_file(filename: str, matrix: IMatrix) -> list[IMatrix]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(filename, "r") as file:
            lines = file.readlines()
            rows, cols = map(int, lines[0].split())
            matrices = []
            for i in range(1, len(lines), rows + 1):
                mat = type(matrix)(rows, cols)  # noqa
                for j in range(i, i + rows):
                    line = lines[j].strip().split()
                    for k in range(cols):
                        mat.set_value(j - i, k, float(line[k]))
                matrices.append(mat)
            return matrices
    
    @staticmethod
    def to_file(filename: str, matrix: IMatrix) -> None:
        with open(filename, "a", encoding="utf_8") as file:
            file.write(f"{matrix.rows} {matrix.cols}\n")
            for row in matrix.data:
                file.write(" ".join(str(e) for e in row) + "\n")
