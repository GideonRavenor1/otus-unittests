from typing import Any

import pytest

from main import solve


def test_solve_return_empty_array() -> None:
	""" x^2+1 = 0 """
	assert solve(a=1.0, b=0.0, c=1.0) == []
	

def test_solve_return_two_roots() -> None:
	""" x^2-1 = 0 """
	assert solve(a=1.0, b=0.0, c=-1.0) == [1.0, -1.0]
	
	
def test_solve_return_one_root() -> None:
	""" x^2+2x+1 = 0 """
	assert solve(a=1.0, b=2.0, c=1.0) == [-1.0]


def test_solve_raise_zero_division_error() -> None:
	""" raise ZeroDivisionError """
	with pytest.raises(ZeroDivisionError):
		solve(a=0.0, b=2.0, c=1.0)
		

@pytest.mark.parametrize(
	"a, b, c",
	[
		(1.0, 2.0, "1.0"),
		({},  2.0, 1.0),
		(1.0, [], 0.0),
		(1.0, None, 2.0)
	]
)
def test_solve_raise_type_error(a: Any, b: Any, c: Any) -> None:
	""" raise TypeError """
	with pytest.raises(TypeError):
		solve(a=a, b=b, c=c)  # type: ignore
	
	
def test_solve_discriminant_was_less_than_the_specified_epsilon() -> None:
	"""D = b2 – 4ac = 0.0012 – 4·0.0001·0.23 = -0.00009100000000000002"""
	assert solve(a=0.0001, b=0.001, c=0.23) == []
