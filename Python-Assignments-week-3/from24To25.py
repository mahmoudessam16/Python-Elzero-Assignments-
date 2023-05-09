# Assignment One
# Needed Output
name = "Osama",

print(name)
print(type(name))
# "Osama"
# <class 'tuple'>


# Assignment Two
friends = ("Osama", "Ahmed", "Sayed")

listOfFriends = list(friends)
listOfFriends[0] = "Elzero"
print(tuple(listOfFriends))
print(type(friends))
print(f"{len(friends)} Elements")
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements


# Assignment Three
nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output
numsAndLetters = nums + letters
print(f"nums_and_letters_one = {numsAndLetters}")
print(f"{len(numsAndLetters)} Elements")
# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements


# Assignment Four
my_tuple = (1, 2, 3, 4)

a, b, _, c = my_tuple

print(a)
print(b)
print(c)
# Needed Output
# 1
# 2
# 4
