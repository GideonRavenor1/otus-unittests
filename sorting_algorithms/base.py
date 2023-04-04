from abc import ABC, abstractmethod


class BaseSortAlgorithm(ABC):
    @abstractmethod
    def execute(self, arr: list[int]) -> list[int]:
        raise NotImplementedError
