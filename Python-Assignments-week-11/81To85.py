# Assignment One
def reverse_string(my_string):
    # Your Code Here
    for x in my_string[-1::-1]:
        yield x


# Reverse The String
for c in reverse_string("Elzero"):
    print(c)

##########################################################
# Assignment Two
# Create Your Decorator Here


def decorator(func):
    def make_tea():
        func()
        print("Tea Created")
        print("#" * 20)

    def make_coffe():
        func()
        print("Coffe Created")
        print("#" * 20)

    make_tea()
    make_coffe()


@decorator
def say_suger():
    print("Sugar Added From Decorators")
# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
