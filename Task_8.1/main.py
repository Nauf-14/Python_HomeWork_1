# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите кол-во долек в плитке по горизонтали: "))
m = int(input("Введите кол-во долек в плитке по вертикали: "))
k = int(input("Введите кол-во долек отломанные за один раз: "))
if k < m * n and ( k % n == 0 or k % m == 0):
    print('Yes')
else:
    print('No')