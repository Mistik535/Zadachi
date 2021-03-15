# def bubble_Sort(array):
#     # определяем длину массива
#     length = len(array)
#     # Внешний цикл, количество проходов N-1
#     for i in range(length):
#         # Внутренний цикл, N-i-1 проходов
#         print("------")
#         for j in range(0, length - i - 1):
#             # Меняем элементы местами
#             print("")
#             print("array[j]", array[j])
#             print("array[j + 1]", array[j + 1])
#
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
# a = [9, 8, 7, 6, 7, 4, 6, 2, 1, 0]
# print(a)
# bubble_Sort(a)
# print(a)

# def selection_sort(array):
#     length = len(array)
#     for i in range(0, length - 1):
#         smallest = i
#         print("----")
#         for j in range(i + 1, length):
#             if array[j] < array(smallest):
#                 smallest = j
#         array[i], array[smallest] = array[smallest], array[i]
#
# a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(a)
# selection_sort(array)
# print(a)
def selection_sort(alist):
    for i in range(len(alist)):
        smallest = i
        for j in range(i, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]

alist = [9, 8, 7, 6, -5, 4, 3, 42, 1, 0]
#alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)