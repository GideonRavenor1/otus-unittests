from factories.base import SortFactory
from sorting_algorithms.insert import InsertionSort


class InsertionSortFactory(SortFactory):
    def create_sort(self) -> InsertionSort:
        return InsertionSort()
