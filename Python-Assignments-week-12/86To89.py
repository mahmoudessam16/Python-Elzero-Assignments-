# Assignment One
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#     my_data.append("".join(data))
#     final_string = "".join(my_data)

# print(final_string.capitalize())  # Elzero


################################################
# Assignment Two
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data1 = []


for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    my_data1.append(item1)
    if len(my_data1) == len("Elzero"):
        final_string = ("".join(my_data1)).capitalize()

print(final_string)
