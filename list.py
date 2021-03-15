# LetterNum = 1
# for Letter in "Howdy!":
#     if Letter == "w":
#         pass
#         print("Encountered w, not processed.")
#     print("Letter ", LetterNum, " is ", Letter)
#     LetterNum+=1

Value = input("Type less than 6 characters: ")
LetterNum = 1
for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1
else:
    print("The string is blank.")