# Определение функции
def is_year_leap(year):
    return year % 4 == 0

# Выбор года для проверки
year_to_check = 2024

# Проверяем год функцией и сохраняем результат
result = is_year_leap(year_to_check)

# Выводим результат
print(f'год {year_to_check}: {result}')