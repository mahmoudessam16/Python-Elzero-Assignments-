# Assignment One
# Input

# name = input("What is your name ? ").strip().capitalize()
# print(f"Hello {name}, Happy To See You Here.")

# # Needed Output
# "Hello Osama, Happy To See You Here."

################################################################################## @###

# Assignment Two
# Inputs

# age = int(input("What is your age?"))
# if age < 16:
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

# if age >= 16:
#     print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

# 16  # Input One
# 24  # Input Two

# Needed Output

# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You"  # If Age < 16
# # If Age Is 16+
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You"

#######################################################################################

# Assignment Three
# Inputs
# first_name = input("What's your first name? ").strip().capitalize()
# second_name = input("What's your second name? ").strip().capitalize()

# print(f"Hello {first_name} {second_name[:1]}.")

# "Osama"  # First Name
# "Mohamed"  # Second Name

# Needed Output

# "Hello {First_Name} {First_Letter_From_Second_Name}."  # Example "Osama M."

##################################################################################

# Assignment Four
# Inputs
email = input("Input Your Email: ").strip().lower()
atIndex = email.index("@")

print(f"Your Name is {email[0:atIndex]}")
dotIndex = email.index(".")
print(f"Email Services Provider is {email[atIndex+1:dotIndex]}")
print(f"Top Level Domain Is {email[dotIndex+1:]}")


# "Osama@Nn.Sa"  # Email
# Needed Output
# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"
