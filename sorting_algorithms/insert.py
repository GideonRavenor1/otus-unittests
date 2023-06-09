from sorting_algorithms.base import BaseSortAlgorithm


class InsertionSort(BaseSortAlgorithm):
    def execute(self, arr: list[int]) -> list[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        self._arr = arr
        return arr
