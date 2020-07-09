"""Task4. Пользователь вводит целое положительное число.
 Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""

n = int(input("Please provide any natural number: "))
k = 0
b = 0
while n != 0:
        k = n % 10
        if k > b:
            b = k
        n = n // 10

print (b)