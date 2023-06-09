from collections.abc import Generator

import pytest

from factories import InsertionSortFactory, MergeSortFactory, SelectionSortFactory


def test_sort_file_not_exist():
    factory = SelectionSortFactory()
    sorter = factory.create()
    
    with pytest.raises(FileNotFoundError):
        sorter.read("missing_file.txt")


def test_selection_sort(
    paths_to_files: Generator[tuple[str, str], None, None],
    array: list[int],
    sorted_array: list[int],
):
    """Тест для фабрики сортировки выбором"""
    input_path, output_path = paths_to_files

    factory = SelectionSortFactory()
    sorter = factory.create()
    
    arr = sorter.read(input_path)
    assert arr == array
    assert sorter.execute(array) == sorted_array
    
    sorter.write(output_path)
    with open(output_path, "r", encoding="utf-8") as file:
        assert list(map(int, file.read().split())) == sorted_array


def test_insertion_sort(
    paths_to_files: Generator[tuple[str, str], None, None],
    array: list[int],
    sorted_array: list[int],
):
    """Тест для фабрики сортировки вставками"""
    input_path, output_path = paths_to_files
    
    factory = InsertionSortFactory()
    sorter = factory.create()
    
    arr = sorter.read(input_path)
    assert arr == array
    assert sorter.execute(array) == sorted_array
    
    sorter.write(output_path)
    with open(output_path, "r", encoding="utf-8") as file:
        assert list(map(int, file.read().split())) == sorted_array
    
   
def test_merge_sort(
    paths_to_files: Generator[tuple[str, str], None, None],
    array: list[int],
    sorted_array: list[int],
):
    """Тест для фабрики сортировки слиянием"""
    input_path, output_path = paths_to_files
    
    factory = MergeSortFactory()
    sorter = factory.create()
    
    arr = sorter.read(input_path)
    assert arr == array
    assert sorter.execute(array) == sorted_array
    
    sorter.write(output_path)
    with open(output_path, "r", encoding="utf-8") as file:
        assert list(map(int, file.read().split())) == sorted_array
