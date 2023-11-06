# год рождения Пушкина
correct_year_pushkin = "1744"

while True:
    year_pushkin = input("Введите год рождения Александра Пушкина: ")
    if year_pushkin == correct_year_pushkin:
        day_pushkin = input("Введите день рождения Александра Пушкина: ")
        if day_pushkin == "6 июня":
            print("Верно")
            break  # Выходим из цикла
        else:
            print("Неверно")
            day_pushkin = input("Введите день рождения Александра Пушкина: ")
else:
    print("Не верный год")
