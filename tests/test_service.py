import numpy as np
import pytest

from adapters.services import AdderGeneratorServiceAdapter
from interfaces.matrix import IMatrix
from managers.file import MatrixFileManager
from managers.matrix_addrer import MatrixAdder
from matrix.base import Matrix
from services.add import MatrixAdderFileWriterService
from services.generate import MatrixGeneratorFileWriterService


class TestMatrixAdderFileWriterService:
    @pytest.fixture
    def service(self, tmp_path) -> MatrixAdderFileWriterService:
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        matrix = Matrix(2, 2)
        matrix.set_value(0, 0, 1)
        matrix.set_value(0, 1, 2)
        matrix.set_value(1, 0, 3)
        matrix.set_value(1, 1, 4)
        MatrixFileManager.to_file(input_file, matrix)
        MatrixAdder()
        MatrixFileManager()
        return MatrixAdderFileWriterService(input_file=input_file, output_file=output_file, matrix=matrix)

    def test_from_file_raises_error_when_file_does_not_exists(self):
        service = MatrixAdderFileWriterService(
            input_file="path/to/nonexistent/input",
            output_file="path/to/nonexistent/output",
            matrix=Matrix(2, 2)
        )
        with pytest.raises(FileNotFoundError):
            service()

    def test_from_file_raises_error_when_file_has_wrong_format(self, tmp_path):
        file = tmp_path / "test.txt"
        with open(file, "w") as f:
            f.write("not a matrix")
        service = MatrixAdderFileWriterService(
            input_file=file,
            output_file=tmp_path / "output.txt",
            matrix=Matrix(2, 2))
        with pytest.raises(ValueError):
            service()


class TestMatrixGeneratorFileWriterService:
    @pytest.fixture
    def service(self, tmp_path) -> MatrixGeneratorFileWriterService:
        output_file = tmp_path / "output.txt"
        matrix = Matrix(2, 2)
        matrix.set_value(0, 0, 1)
        matrix.set_value(0, 1, 2)
        matrix.set_value(1, 0, 3)
        matrix.set_value(1, 1, 4)
        return MatrixGeneratorFileWriterService(output_file=output_file, matrix=matrix)

    def test_from_file_raises_error_when_file_does_not_exists(self):
        service = MatrixGeneratorFileWriterService(
            output_file="path/to/nonexistent/output",
            matrix=Matrix(2, 2)
        )
        with pytest.raises(FileNotFoundError):
            service()

    
class MockMatrix(IMatrix):
    
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols))
        
    def set_size(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        
    def set_value(self, row: int, col: int, value: float) -> None:
        self.data[row][col] = 0
        
    def __add__(self, other: "IMatrix") -> "IMatrix":
        return MockMatrix(self.rows, self.cols)
    
    
class TestAdderServiceAdapter:
    @pytest.fixture
    def adapter(self, tmp_path) -> AdderGeneratorServiceAdapter:
        input_file = tmp_path / "input.txt"
        output_file = tmp_path / "output.txt"
        matrix = MockMatrix(2, 2)
        return AdderGeneratorServiceAdapter(
            input_file=input_file,
            output_file=output_file,
            matrix=matrix
        )

    def test_input_file_is_written_and_added_to_output_file(self, adapter: AdderGeneratorServiceAdapter):
        adapter()
        with open(adapter.output_file, "r") as f:
            result = f.read()
            expected = "2 2\n0.0 0.0\n0.0 0.0\n"
            assert result == expected
