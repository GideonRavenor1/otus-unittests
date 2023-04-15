from factories.base import SortFactory
from sorting_algorithms.selection import SelectionSort


class SelectionSortFactory(SortFactory):
    def create(self) -> SelectionSort:
        return SelectionSort()
