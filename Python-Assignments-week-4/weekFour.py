# Assignments one
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
list1 = list(unique_list)
print(list1)
print(type(list1))
list1.pop()
print(list1)
# Needed Output
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4


# Assignments Two
nums = {1, 2, 3}
letters1 = {"A", "B", "C"}

print(nums | letters1)
print(nums.union(letters1))
# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}


# Assignments Three
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.symmetric_difference_update(letters)
my_set.remove("C")
print(my_set)
# Needed Output
# {1, 2, 3}
# set()
# {"A", "B"}


# Assignment Four
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# Needed Output
# True


# Assignment Five
# Create Dictionary Here
skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%",
}
skills.setdefault("AI", "20%")

print(f"HTML Progress Is {skills['HTML']}")
print(f"CSS Progress Is {skills['CSS']}")
print(f"Python Progress Is {skills['Python']}")
print(f"AI Progress Is {skills['AI']}")

# Needed Output
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"
