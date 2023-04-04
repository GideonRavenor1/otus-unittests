from abc import ABC, abstractmethod

from sorting_algorithms.base import BaseSortAlgorithm


class SortFactory(ABC):
    @abstractmethod
    def create_sort(self) -> BaseSortAlgorithm:
        raise NotImplementedError
