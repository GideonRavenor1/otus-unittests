import os
from collections.abc import Generator

import pytest
from managers.file import FileManager, MatrixFileManager
from managers.matrix_addrer import MatrixAdder
from matrix.base import Matrix


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


def test_add_two_matrices():
    matrix1 = Matrix()
    matrix1.set_value(0, 0, 1)
    matrix1.set_value(1, 1, 1)
    matrix1.set_value(2, 2, 1)

    matrix2 = Matrix()
    matrix2.set_value(0, 0, 9)
    matrix2.set_value(1, 1, 9)
    matrix2.set_value(2, 2, 9)

    expected = Matrix()
    expected.set_value(0, 0, 10)
    expected.set_value(1, 1, 10)
    expected.set_value(2, 2, 10)

    result = MatrixAdder.add([matrix1, matrix2])

    assert result.rows == 3
    assert result.cols == 3
    assert result.data.all() == expected.data.all()


def test_add_three_matrices():
    matrix1 = Matrix()
    matrix1.set_value(0, 0, 1)
    matrix1.set_value(1, 1, 1)
    matrix1.set_value(2, 2, 1)

    matrix2 = Matrix()
    matrix2.set_value(0, 0, 9)
    matrix2.set_value(1, 1, 9)
    matrix2.set_value(2, 2, 9)

    matrix3 = Matrix()
    matrix3.set_value(0, 1, 2)
    matrix3.set_value(1, 2, 3)
    matrix3.set_value(2, 0, 7)

    expected = Matrix()
    expected.set_value(0, 0, 10)
    expected.set_value(0, 1, 2)
    expected.set_value(1, 1, 10)
    expected.set_value(1, 2, 3)
    expected.set_value(2, 0, 7)
    expected.set_value(2, 2, 1)

    result = MatrixAdder.add([matrix1, matrix2, matrix3])

    assert result.rows == 3
    assert result.cols == 3
    assert result.data.all() == expected.data.all()


def test_add_raises_exception_on_one_matrix():
    matrix = Matrix()
    with pytest.raises(ValueError):
        MatrixAdder.add([matrix])


def test_add_raises_exception_on_empty_list():
    with pytest.raises(ValueError):
        MatrixAdder.add([])


def test_add_raises_exception_if_matrices_have_different_shapes():
    matrix1 = Matrix()
    matrix1.set_value(0, 0, 1)
    matrix1.set_value(1, 1, 1)
    matrix1.set_value(2, 2, 1)

    matrix2 = Matrix(2, 2)
    matrix2.set_value(0, 0, 9)
    matrix2.set_value(1, 1, 9)

    with pytest.raises(ValueError):
        MatrixAdder.add([matrix1, matrix2])


def test_from_file_returns_list_of_matrices():
    filename = "test.txt"
    with open(filename, "w", encoding="utf_8") as file:
        file.write("2 2\n1.0 2.0\n3.0 4.0\n2 2\n5.0 6.0\n7.0 8.0\n")

    matrix = Matrix(2, 2)
    result = MatrixFileManager.from_file(filename, matrix)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all([isinstance(mat, type(matrix)) for mat in result])


def test_to_file_saves_matrix():
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)
    matrix = Matrix(2, 2)
    matrix.set_value(0, 0, 1.0)
    matrix.set_value(0, 1, 2.0)
    matrix.set_value(1, 0, 3.0)
    matrix.set_value(1, 1, 4.0)
    MatrixFileManager.to_file(filename, matrix)

    with open(filename, "r") as file:
        lines = file.readlines()
        assert len(lines) == 3
        assert lines[0].strip() == "2 2"
        assert lines[1].strip() == "1.0 2.0"
        assert lines[2].strip() == "3.0 4.0"
    
    if os.path.exists(filename):
        os.remove(filename)


def test_from_file_raises_exception_on_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        MatrixFileManager.from_file("nonexistent.txt", Matrix(2, 2))
