'''yearPushkin = 1744
year = int(input('год рождения Пушкина :'))
while year != yearPushkin:
    print("Неверно")
    year = int(input('год рождения Пушкина :'))
print('вы угадали ')'''

yearPushkin = 1744
year = int(input('год рождения Пушкина :'))
if yearPushkin == year:
    print('верно')
else:
    print('не верно')
