# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Написать программу, которая проверяет счастливость билета. 

n = int(input("Введите номер билета: "))
s1 = 0
s2 = 0
a = int(n // 100000)
b = int(n // 10000 % 10)
c = int(n /1000 % 10)
s1 = a + b + c
print(s1)

d = int(n / 100 % 10) 
e = int(n / 10 % 10)
f = int(n % 10)
s2 = d + e + f
print(s2)

if s1 == s2:
    print("Счастливый")
else:
    print("Нет")

