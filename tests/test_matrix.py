import pytest

from matrix.base import Matrix


def test_set_size():
    matrix = Matrix()
    matrix.set_size(2, 2)
    assert matrix.rows == 2
    assert matrix.cols == 2
    assert str(matrix) == "[[0. 0.]\n [0. 0.]]"


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

    result = matrix1 + matrix2

    assert result.rows == 3
    assert result.cols == 3
    assert result.data.all() == expected.data.all()


def test_add_raises_exception_on_matrices_with_different_shapes():
    matrix1 = Matrix(2, 2)
    matrix2 = Matrix()
    with pytest.raises(ValueError):
        matrix1 + matrix2
