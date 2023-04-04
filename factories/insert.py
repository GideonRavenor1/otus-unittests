from factories.base import SortFactory
from sorting_algorithms.insert import InsertionSort


class InsertionSortFactory(SortFactory):
    def create(self) -> InsertionSort:
        return InsertionSort()
