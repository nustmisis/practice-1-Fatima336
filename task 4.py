### Задание №4
a = input("Введите целое четырехзначное число: ")
summa = 0
for i in range(len(a)):
    ost = int(a)%10
    a = int(a)/10
    summa = summa + ost
print('Сумма составляющих его цифр равна:', summa)