a = float(input("Сколько километро спортсмен пробежал в первый день >>>"))
b = float(input("Какого результата должен достичь спортсмен >>>"))

day = 1

if a >= b:
    print(day)
while a < b:
    a = a + a * 0.1
    day += 1
print(day)