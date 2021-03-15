# for i in "agegelhusen":
#     if i == 'a':
#         # continue
#         print("YES")
#         break
#     else:
#         print("Thereis no any a letter in the word")
# def printThese(a=None,b=None,c=3):
#    print(a, "is stored in a")
#    print(b, "is stored in b")
#    print(c, "is stored in c")
# printThese(c=1, a=1)
def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)