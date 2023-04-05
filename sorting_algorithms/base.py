from abc import ABC, abstractmethod

from managers.file import FileManager


class BaseSortAlgorithm(ABC):
    manager = FileManager()
    
    def __init__(self) -> None:
        self._arr = []
    
    @abstractmethod
    def execute(self, arr: list[int]) -> list[int]:
        raise NotImplementedError
    
    def read(self, filename: str) -> list[int]:
        return self.manager.read(filename)
    
    def write(self, filename: str) -> None:
        self.manager.write(filename, self._arr)
