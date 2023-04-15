from factories.base import SortFactory
from sorting_algorithms.merge import MergeSort


class MergeSortFactory(SortFactory):
    def create(self) -> MergeSort:
        return MergeSort()
