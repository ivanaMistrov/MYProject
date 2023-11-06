import random

# Создаем словарь с известными людьми и их годами рождения
celebrities = {
    "Альберт Эйнштейн": 1879,
    "Исаак Ньютон": 1643,
    "Мария Кюри": 1867,
    "Наполеон Бонапарт": 1769,
    "Уильям Шекспир": 1564
}

def play_quiz():
    correct_answers = 0
    wrong_answers = 0

    # Перемешиваем известных людей для каждой новой игры
    list_of_celebrities = list(celebrities.items())
    random.shuffle(list_of_celebrities)

    for name, birth_year in list_of_celebrities:
        guess = input(f"В каком году родился {name}? ")
        try:
            guess = int(guess)
            if guess == birth_year:
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно. Правильный ответ: {birth_year}")
                wrong_answers += 1
        except ValueError:
            print("Вы ввели некорректный год. Попробуйте снова.")
            wrong_answers += 1

    total_questions = correct_answers + wrong_answers
    correct_percentage = (correct_answers / total_questions) * 100
    wrong_percentage = (wrong_answers / total_questions) * 100

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    print(f"Процент правильных ответов: {correct_percentage}%")
    print(f"Процент неправильных ответов: {wrong_percentage}%")

# Запускаем игру
play_quiz()

# Проверяем, хочет ли пользователь начать игру заново
while True:
    play_again = input("Хотите начать игру заново? (да/нет): ")
    if play_again.lower() == "да":
        play_quiz()
    elif play_again.lower() == "нет":
        print("Спасибо за игру! До свидания!")
        break
    else:
        print("Пожалуйста, введите 'да' или 'нет'.")

