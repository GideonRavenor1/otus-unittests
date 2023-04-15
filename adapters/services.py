from interfaces.matrix import IMatrix
from services.generate import MatrixGeneratorFileWriterService
from services.add import MatrixAdderFileWriterService


class AdderGeneratorServiceAdapter:
    
    def __init__(self, input_file: str, output_file: str, matrix: IMatrix) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = matrix
        
    def __call__(self) -> None:
        MatrixGeneratorFileWriterService(
            output_file=self.input_file,
            matrix=self.matrix
        )()
        MatrixAdderFileWriterService(
            input_file=self.input_file,
            output_file=self.output_file,
            matrix=self.matrix
        )()
