import numpy as np
import pytest

from adapters.services import AdderGeneratorServiceAdapter
from interfaces.matrix import IMatrix


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
