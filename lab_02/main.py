n = int(input("Сколько измерений вы хотите ввести? "))

summa = 0

# вводим числа и складываем их
for i in range(n):
    chislo = float(input("Введите измерение: "))
    summa = summa + chislo

# считаем среднее
srednee = summa / n

# выводим результат
print("Сумма всех измерений:", summa)
print("Среднее арифметическое:", srednee)