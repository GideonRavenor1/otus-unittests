import math
from decimal import Decimal


def solve(a: float, b: float, c: float) -> list[float]:
	"""
	Решает уравнение ax^2 + bx + c = 0.
	:param a: коэффициент A.
	:param b: Коэффициент B.
	:param c: Коэффициент C.
	:return: Корни квадратного уравнения
	"""
	
	discriminant = Decimal(b ** 2 - 4 * a * c)

	if discriminant > Decimal(0):
		root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
		root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
		return [root_1, root_2]
	elif discriminant == Decimal(0):
		x = -b / (2 * a)
		return [x]
	else:
		return []


if __name__ == '__main__':
	print(solve(a=0.0001, b=0.001, c=0.23))
