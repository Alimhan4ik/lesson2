import math


def square(side_length):
    # Возводим длину стороны в квадрат
    area = side_length ** 2

    # Округляем вверх, если длина была дробной
    if isinstance(side_length, float):
        area = math.ceil(area)

    return area
# Целое значение
print(square(5))   # Output: 25

# Дробное значение
print(square(8.5)) # Output: 73 (так как 8.5 * 8.5 = 72.25, которое округлится вверх до 73)
