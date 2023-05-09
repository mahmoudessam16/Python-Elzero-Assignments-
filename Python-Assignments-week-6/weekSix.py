# # Assignment One
# # Inputs
# num1 = int(input("Num One: ").strip())
# num2 = int(input("Num Two: ").strip())
# operation = input("Calculation Operation: ").strip()

# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "%":
#     print(num1 % num2)

# # Needed Output
# # [num1 20] [operation +] [num2]
# # Example One 20 + 40 = 60
# # Example Two 20 * 40 = 800

################################################################################

# Assignment Two
# age = 16

# print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
# # Needed Output
# # "App Is Suitable For You"  # If Age Larger Than 6
# # "App Is Not Suitable For You"  # if Age Smaller Than 16

###########################################################################

# Assignment Three
# yourAge = int(input("Your Age: "))

# if yourAge > 10 and yourAge < 100:
#     print(f"Your Age In Months Is {yourAge * 12:,} Months")
#     print(f"Your Age In Weeks Is {yourAge * 52:,} Weeks")
#     print(f"Your Age In Days Is {yourAge * 365:,} Days")
#     print(f"Your Age In Hours Is {yourAge * 365 * 24:,} Hours")
#     print(f"Your Age In Minutes Is {yourAge * 365 * 24 * 60:,} Minutes")
#     print(f"Your Age In Seconds Is {yourAge * 365 * 24 * 60 * 60:,} Seconds")
# else:
#     print("Your Age Is Out Of Range")

#############################################################################
# Assignment Four
# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70"  # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100"  # Ghana Example
