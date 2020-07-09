"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
 Считаем 3 + 33 + 333 = 369."""

n = input("Please provide the magic number: ")
n1 = int(n)
n2 = int(n+n)
n3 = int(n+n+n)
print(f'Magic = {n1+n2+n3}')


