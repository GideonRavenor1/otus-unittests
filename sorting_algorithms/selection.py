from sorting_algorithms.base import BaseSortAlgorithm


class SelectionSort(BaseSortAlgorithm):
    def execute(self, arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        self._arr = arr
        return arr
