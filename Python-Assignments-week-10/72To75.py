# Assignment One
from functools import reduce


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]


def remove_chars(text):
    array = list(text)
    array[len(array) - 1] = ""
    array[0] = ""
    return "".join(array)


cleaned_list = map(remove_chars, friends_map)
for name in list(cleaned_list):
    print(name)
##########################################################
# Assignment Two


def get_names(name):
    return str(name).endswith("m")


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)

for name in names:
    print(name)
# Same Example but with lambda function
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)
for name in filter(lambda name: str(name).endswith("m"), friends_filter):
    print(name)

#############################################################
# Assignment Three
# def miltiply(num1, num2):
#     return num1 * num2
nums = [2, 4, 6, 2]
multiplyAll = reduce(lambda num1, num2: num1 * num2, nums)
print(multiplyAll)
# # Output
# 96

#################################################
# Assignment Four
# Method One
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
enumerateSkills = enumerate(reversed(skills), 50)
for counter, skill in enumerateSkills:
    if type(skill) == int:
        continue
    print(f"{counter} - {skill}")
print("#" * 30)
####################################
# Method Two
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
index = 50
for skill in reversed(skills):
    if type(skill) == int:
        index += 1
        continue
    print(f"{index} - {skill}")
    index += 1
# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"
