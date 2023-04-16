from interfaces.matrix import IMatrix
from services.generate import MatrixGeneratorFileWriterService
from services.add import MatrixAdderFileWriterService


class AdderGeneratorServiceAdapter:
    generator: type[MatrixGeneratorFileWriterService] = MatrixGeneratorFileWriterService
    adder: type[MatrixAdderFileWriterService] = MatrixAdderFileWriterService
    
    def __init__(self, input_file: str, output_file: str, matrix: IMatrix) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = matrix
        
    def __call__(self) -> None:
        self.generator(
            output_file=self.input_file,
            matrix=self.matrix
        )()
        self.adder(
            input_file=self.input_file,
            output_file=self.output_file,
            matrix=self.matrix
        )()
