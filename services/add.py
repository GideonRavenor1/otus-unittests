from interfaces.matrix import IMatrix
from managers.matrix_addrer import MatrixAdder
from services.base import BaseService


class MatrixAdderFileWriterService(BaseService):
    adder = MatrixAdder()
    
    def __init__(self, input_file: str, output_file: str, matrix: IMatrix) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = matrix

    def __call__(self) -> None:
        matrices = self.file_manager.from_file(filename=self.input_file, matrix=self.matrix)
        result = self.adder.add(matrices)
        self.file_manager.to_file(self.output_file, matrix=result)
