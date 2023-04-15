from interfaces.matrix import IMatrix


class MatrixAdder:
    
    @staticmethod
    def add(matrices: list[IMatrix]) -> IMatrix:
        if len(matrices) < 2:
            raise ValueError("There must be at least two matrices!")
        
        result = None
        for index, matrix in enumerate(matrices, start=1):
            
            if result is None:
                result = matrix
                continue
                
            result += matrix
        return result
