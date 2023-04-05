from collections.abc import Generator

import pytest
from managers.file import FileManager


def test_get_array_from_file(paths_to_files: Generator[tuple[str, str], None, None], array: list[int]) -> None:
    """Проверяем, что метод корректно возвращает массив чисел из файла"""
    
    input_path, _ = paths_to_files
    arr = FileManager.read(input_path)
    assert arr == array


def test_get_array_from_file_missing():
    """Проверяем, что метод выбрасывает исключение, если файл отсутствует"""
    
    with pytest.raises(FileNotFoundError):
        FileManager.read("missing_file.txt")


def test_write_array_to_file(
    paths_to_files: Generator[tuple[str, str], None, None],
    array: list[int],
) -> None:
    """Проверяем, что метод корректно записывает массив чисел в файл"""
    
    _, output_path = paths_to_files
    FileManager.write(output_path, array)
    
    with open(output_path, encoding="utf-8") as file:
        assert list(map(int, file.read().split())) == array


def test_read_write_consistency(
    paths_to_files: Generator[tuple[str, str], None, None],
    array: list[int],
) -> None:
    """Проверяем, что записанный и прочитанный массивы совпадают"""

    _, output_path = paths_to_files
    FileManager.write(output_path, array)
    read_arr = FileManager.read(output_path)
    assert array == read_arr
