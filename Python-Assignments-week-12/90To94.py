# Assignment one

# num = int(input("Add Your Number "))

# if len(str(num)) > 1:
#     raise IndexError("Only One Character Allowed")
# elif num == 0:
#     raise ValueError(f"Number Must Be Larger Than {num}")
# elif type(num) != int:
#     raise Exception("Only Numbers Allowed")
# else:
#     print(f"The Number Is {num}")

################################################
# Assignment Two
# LETTER = input("Add Letter From A to Z => ")

# try:
#     if len(LETTER) != 1:
#         raise NameError
#     if not LETTER.isupper():
#         raise IndexError
# except NameError:
#     print("You Must Write One Character Only")
# except IndexError:
#     print("The Letter Not In A - Z")
# else:
#     print(f"You Typed {LETTER}")


###########################################
# Assignment Three
def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))
