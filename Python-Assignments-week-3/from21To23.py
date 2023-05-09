# Assignment One
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends.pop(0))

print(friends[-1])
print(friends.pop(-1))
# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two


# Assignment Two
friends1 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends1[::2])
print(friends1[1::2])
# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"


# Assingment Three
friends3 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends3[1:4])
print(friends3[-2:])
# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"


# Assignment Four
friends4 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends4[-1] = "Elzero"
friends4[-2] = "Elzero"
print(friends4)
# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]


# Assignment Five
friends5 = ["Osama", "Ahmed", "Sayed"]

friends5.insert(0, "Nasser")
print(friends5)
friends5.append("Salem")
print(friends5)
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


# Assignment six
friends6 = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends6.pop(0)
friends6.pop(0)
friends6.pop(-1)
print(friends6)
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]


# Assignment Seven
friends7 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends7.extend(employees)
friends7.extend(school)

print(friends7)
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]


# Assignment Eight
friends8 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends8.sort()
print(friends8)
friends8.reverse()
print(friends8)
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

# Asignment Nine
friends9 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends9))
# Needed Output
# 6


# Assignment Ten
technologies = ["Html", "CSS", "JS", "Python",
                ["Django", "Flask", "Web", "Numby"]]

print(technologies[4][0])
print(technologies[4][len(technologies[4]) - 1])
# Needed Output
# Django
# Web
