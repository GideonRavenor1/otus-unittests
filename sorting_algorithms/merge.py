from sorting_algorithms.base import BaseSortAlgorithm


class MergeSort(BaseSortAlgorithm):
    def execute(self, arr: list[int]) -> list[int]:
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self.execute(L)
            self.execute(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        
        self._arr = arr
        return arr
