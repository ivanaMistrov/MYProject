total = 0
again = 1

enshtein = 1879
nuton = 1643
kuri = 1867
bonapart = 1769
Schekspir = 1564

while again:
    total = 0
    a = input("Напиши год рождения Энштейна ")
    if (enshtein == int(a)):
        total += 1

    b = input("год рождения Ньютона напиши")
    if (nuton == int(b)):
        total += 1

    c = input("Год рождения Кюри напиши")
    if (kuri == int(c)):
        total += 1

    d = input("Год рождения Наполеона напиши")
    if (bonapart == int(d)):
        total += 1

    f = input("Год рождения Шекспира напиши")
    if (Schekspir == int(f)):
        total += 1

    print("ты " + str(total) + " ответов отгадал")
    print("это  целых % " + str(total * 100 / 5) + " ответов ")
    again = input("еще разок? 1 = да 2 = нет")
    if (int(again) == 1):
        continue
    else:
        break
