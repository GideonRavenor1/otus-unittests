import sys
import math
from decimal import Decimal

epsilon = sys.float_info.epsilon
zero = Decimal(0)


def solve(a: float, b: float, c: float) -> list[float]:
	"""
	Решает уравнение ax^2 + bx + c = 0.
	:param a: коэффициент A.
	:param b: Коэффициент B.
	:param c: Коэффициент C.
	:return: Корни квадратного уравнения
	"""
	
	if a == zero:
		raise ZeroDivisionError
	
	discriminant = b ** 2 - 4 * a * c
	if math.isclose(discriminant, 0, rel_tol=epsilon, abs_tol=epsilon):
		return [-b / (2 * a)]
	elif discriminant > -epsilon:
		sqrt_discriminant = math.sqrt(discriminant)
		x1 = (-b + sqrt_discriminant) / (2 * a)
		x2 = (-b - sqrt_discriminant) / (2 * a)
		return [x1, x2]
	else:
		return []


if __name__ == '__main__':
	print(solve(a=0.0001, b=0.001, c=0.23))
