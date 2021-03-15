# ZAD 1
# Создать массив N и заполнить его числами с клавиатуры.
# Вывести на консоль первый и последний элемент массива.
# Поменять местами первый и последний элемент в массиве.

# ZAD 2
# Программа должна переводить число, введенное с клавиатуры в метрах, в километры.

print("Input N:")
N = int(input())
list = []

for i in range(0, N):
    print("Append item [", i, "]: ")
    list.append(int(input()))
print(list[0])
print(list[N - 1])
x = list[N - 1]
list[N - 1] = list[0]
list[0] = x
print(list)

# def meters(a):
#     return a * 0.001
#
# a = int(input())
# print("Kilometres =", meters(a))
