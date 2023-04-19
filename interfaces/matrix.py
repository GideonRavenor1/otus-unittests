from typing import Protocol

from numpy import ndarray


class IMatrix(Protocol):
    rows: int
    cols: int
    data: ndarray
    
    def set_size(self, rows: int, cols: int) -> None:
        ...
 
    def set_value(self, row: int, col: int, value: float) -> None:
        ...
    
    def __add__(self, other: "IMatrix") -> "IMatrix":
        ...
