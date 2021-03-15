# n = int(input())
# a = n//100
# b = (n//10)%10
# c = n%10
# print(a+b+c, "Sum of three")

# a =int(input())
# a= a+1
# print(a)

#arr = [23, 4, 56, 5554, 232, 198, 4, 3242, 5534, 65]
# for i in range (mas):
#     digit = i
#     for j in range(i, mas):
def insertion_sort(mas):
    for i in range (1, len(mas)): # начинаем сортировку с первого элемента так как первый уже отсортирован
        temporary = mas[i] # ячейка которая будет сравнивать
        #print(temporary)
        j = i-1 # это нужно чтобы пробегаться по всем индексам массива
        #print(j)
        while j >=0 and temporary < mas[j]:
            print(temporary)
            mas[j+1] = mas[j]
            print(j+1,j,":", temporary)
            j -= 1
        mas[j+1] = temporary
    #return mas
mas = [23, 4, 56, 5554, 232, 198, 4, 3242, 5534, 65, -1123, -1345]
print("Результат:", mas)
insertion_sort(mas)
print("Результат:", mas)
# for i in range(len(mas)):
#      print(mas[i])

