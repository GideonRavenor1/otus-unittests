from copy import copy

from interfaces.matrix import IMatrix
from managers.matrix_generator import MatrixGenerator
from services.base import BaseService


class MatrixGeneratorFileWriterService(BaseService):
    generator = MatrixGenerator()
    
    def __init__(self, output_file: str, matrix: IMatrix) -> None:
        self.output_file = output_file
        self.matrix = matrix
        
    def __call__(self) -> None:
        matrix_a = self.generator.generate(copy(self.matrix))
        matrix_b = self.generator.generate(copy(self.matrix))
        self.file_manager.to_file(filename=self.output_file, matrix=matrix_a)
        self.file_manager.to_file(filename=self.output_file, matrix=matrix_b)
