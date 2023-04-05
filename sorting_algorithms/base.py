from abc import ABC, abstractmethod

from managers.file import FileManager


class BaseSortAlgorithm(ABC):
    __manager = FileManager()
    
    def __init__(self) -> None:
        self._arr = []
    
    @abstractmethod
    def execute(self, arr: list[int]) -> list[int]:
        raise NotImplementedError
    
    def read(self, filename: str) -> list[int]:
        return self.__manager.read(filename)
    
    def write(self, filename: str) -> None:
        self.__manager.write(filename, self._arr)
