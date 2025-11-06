def month_to_season(month_number):
    seasons = {
        1: 'Зима',
        2: 'Зима',
        3: 'Весна',
        4: 'Весна',
        5: 'Весна',
        6: 'Лето',
        7: 'Лето',
        8: 'Лето',
        9: 'Осень',
        10: 'Осень',
        11: 'Осень',
        12: 'Зима'
    }
    return seasons.get(month_number, "Неверный номер месяца")

# Интерфейс взаимодействия с пользователем
try:
    user_input = int(input("Введите номер месяца (от 1 до 12): "))
    result = month_to_season(user_input)
    print(result)
except ValueError:
    print("Некорректный ввод. Нужно ввести число.")