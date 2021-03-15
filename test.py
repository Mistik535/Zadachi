# l_list = {1.1, 1.5, 4.4, 9.0}
# print(type(l_list))
#
# for root in l_list:
#     print(type(root), "=", root)
#     for item in root:
#         print(item)
#     print("")

# a = int(input())
# while a < -1:
#    a += 1
#    if a >= 7:
#        continue
#    print("A")

# def fibb(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibb(n-1) + fibb(n-2)
# print(fibb(10))

# def simple_generator(val):
#    while val > 0:
#        val -= 1
#        yield 1
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
# print(next(gen_iter))

# Lev = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda x: x**3, Lev)))

# n1 = input("Введите первое двоичное число: ")
# # n2 = input("Введите второе двоичное число: ")
# #
# # n1 = int(n1, 2)
# # n2 = int(n2, 2)
# #
# # bit_or = n1 | n2
# # bit_and = n1 & n2
# # bit_xor = n1 ^ n2
# #
# # print("Результат побитового OR: %10s" % bin(bit_or))
# # print("Результат побитового AND: %10s" % bin(bit_and))
# # print("Результат побитового XOR: %10s" % bin(bit_xor))

# a = input()
# print(int(a[0])+int(a[1])+int(a[2]))

# n1 = input("Введите целое число: ")
# n_list = list(n1)
# n_list.reverse()12
# n2 = "".join(n_list)
# print('"Обратное" ему число:', n2)

# old_list = ["1", "2", "3", "4", "5"]
# new_list = list(map(int, old_list))
# print (new_list)

# elements = (1,2,3,4)
# elements_plus1 = tuple(map(lambda x:x+1,elements))
# print(elements_plus1)

# students = [('Amanda','161cm','51kg'), ('Patricia','165cm','61kg'), ('Marcos','191cm', '101kg')]
# students_height = list(map(lambda x:x[1], students))
#
# students_weight = list(map(lambda x:int(x[2][:-2]), students))
# print(students_weight)

# import sys
# #print("Привет {}. Добро пожаловать в руководство по  {} на {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
# print(sys.path)
# sys.exit()
# sys.exit(0)
from random import randint


def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 5
a = []
for i in range(N):
    a.append(randint(0, 9))

print(a)
bubble(a)
print(a)

# #from random import randint
# N = (0,1,2,3,4,5,6,7,8,9)
# a =()
#for i in range(0, 9):
    #a.append(randint(0, 9))
#print(a)

# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)

# N = [0,1,2,3,4,5,6,7,8,9]
# a = ()
# for i in range(N -1):
#     for i in range(N - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)