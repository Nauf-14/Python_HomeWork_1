# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))
a = int(n // 100) 
b = int(n / 10 % 10)
c = int(n % 10)
result = a + b + c
print(result)