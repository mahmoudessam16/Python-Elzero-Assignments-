# # Assignment One
# num = int(input("Write A Number: "))
# counter = 1
# if num > 0:
#     while num > 0:
#         num -= 1
#         if num == 0:
#             continue
#         if num == 6:
#             continue
#         print(num)
#         counter += 1
#     else:
#         print(f"{counter - 1} Numbers Printed Successfully.")

# else:
#     print(f"Number {num} Is Not Larger Than 0")

#########################################################################
# Assignment Two
# Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif", "Mahmoud", "sayed"]

# ignoredFriends = 0
# index = 0

# while index < len(friends):
#     if friends[index][0].isupper():
#         print(friends[index])
#     elif friends[index][0].islower():
#         ignoredFriends += 1
#     index += 1
# else:
#     print(f"Friends Printed And Ignored Names Count Is {ignoredFriends}")

# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"


# Assignment Three
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print(skills.pop(0))
# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"

# Assignment Four
my_friends = []
biggest = 4

while biggest > 0:
    name = input("Write Your Name: ")
    if name.isupper():
        print("Invalid Name")
    if name.islower():
        name.capitalize()
        my_friends.append(name.strip())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {biggest}")
    if name[0].isupper():
        my_friends.append(name.strip())
        print(f"Names Left in List Is {biggest}")
    biggest -= 1
