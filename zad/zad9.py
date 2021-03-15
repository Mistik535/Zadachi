# Реализовать калькулятор
# Должно быть 4 функции (сложение, вычитание, умножение и деление) + вывод на экран
# Данные должны вводиться с клавиатуры 2 значения

# import keyboard
#
# keyboard.press_and_release('+')
# print("Нажмите, чтобы выполнить операцию")
# def plus(a, b):
#     print(a + b)
#
# print("input \"a\" +")
# a = int(input())
# print("input \"b\" +")
# b = int(input())

#plus(a, b)

# def minus(c, d):
#     print(c - d)

# print("input" \"c\" -")
# c = int(input())
# print("input" \"d\" -")
# d = int(input())

a1 = int(input("Введите первое число:"))
a2 = int(input("Введите второе число:"))

b = int (input('Выберите операцию? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

if b == 1:
    r = a1 + a2
    p = 'сложения'
    t = p
if b == 2:
    r = a1 - a2
    l = 'вычитания'
    t = l
if b == 3:
    r = float(a1 / a2)
    m = 'деления'
    t = m
if b == 4:
    r = a1 * a2
    n = 'умножения'
    t = n
print ('Результат ',t,' = ',r)