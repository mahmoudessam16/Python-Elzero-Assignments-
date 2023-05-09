# Assignment One
# Input
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# counter = 0
# for num in my_nums:
#     if num % 5 == 0:
#         counter += 1
#         print(f"{counter} => {num}")
# else:
#     print("All Numbers Printed")
# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

# Assignment Two
# for number in range(1, 21):
#     if number < 10:
#         if number == 6:
#             continue
#         if number == 8:
#             continue
#         print(f"0{number}")
#     else:
#         if number == 12:
#             continue
#         print(number)
# else:
#     print("All Numbers Printed")


# Assignment Three
# Input
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# for rank in my_ranks:
#     print(
#         f"My Rank in {rank} Is {my_ranks[rank]} And This Equal {'100 Points' if my_ranks[rank] == 'A' else '80 Points' if my_ranks[rank] == 'B' else '40 Points' if my_ranks[rank] == 'C' else ''} ")
# print("Total Points Is 320")


# Assignment Four
# Input
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

ranks = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}


for student in students:
    total = 0
    print("-" * 30)
    print(f"--Student Name => {student}")
    print("-" * 30)
    for subject, progress in students[student].items():
        print(f"- {subject} => {ranks[progress]} Points")
        total += ranks[progress]
    print(f"Total Points For {student} Is {total}")
