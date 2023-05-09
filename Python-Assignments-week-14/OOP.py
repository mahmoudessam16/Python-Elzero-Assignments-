# Assignment One
class Game:
    # Write Class Content
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return f"{float(self.price * 15.6)} Egyptian Pounds"


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

#########################################################
# Assignment Two


class User:
    # Write Class Content
    def __init__(self, firstName, lastName, age, gender):
        self.fname = firstName
        self.lname = lastName
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname} {self.lname[0:1]}. [{str((40 - self.age)).zfill(2)}] Years To Reach 40"
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname} {self.lname[0:1]}. [{str((40 - self.age)).zfill(2)}] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")
user_three = User("Mahmoud", "Essam", 23, "Male")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40
print(user_three.full_details())  # Hello Mr Mahmoud E. [17] Years To Reach 40


################################################################
# Assignment Three
class Message:
    # Write Class Content
    def __init__(self):
        pass

    def print_message():
        return "Hello From Class Message"


print(Message.print_message())

# Output
# Hello From Class Message
#########################################################
# Assignment Four


class Games:
    # Write Class Content
    def __init__(self, game):
        self.game = game

    def show_games(self):
        if type(self.game) == str:
            print(f"I Have One Game Called {self.game}")
        elif type(self.game) == list:
            print("I Have Many Games: ")
            for game in self.game:
                print(f"-- {game}")
        elif type(self.game) == int:
            print(f"I Have {self.game} Game.")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.


#############################################################################
# Assignment Five
# Main Class
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here


class Admins(Members):
    def __init__(self, n, p):
        Members.__init__(self, n, p)

# Create Moderators Class Here


class Moderators(Members):
    def __init__(self, n, p):
        super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator
#########################################################################
# Assignemnt six


class A:
    def __init__(self, one):
        self.one = one


class B:
    def __init__(self, two):
        self.two = two


class C:
    def __init__(self, three):
        self.three = three

# Write The Class Called "Text" Here


class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero
