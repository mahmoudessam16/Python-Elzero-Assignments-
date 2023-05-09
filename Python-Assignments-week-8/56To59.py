# Assignment One
def calculate(n1, n2, operation="add"):
    operation = operation.lower()
    if operation in ['a', 'add']:
        return n1 + n2
    elif operation in ['s', 'subtract']:
        return n1 - n2
    elif operation in ['m', 'multiply']:
        return n1 * n2
    else:
        return "operation is not valid"


# Tests
print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30

print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10

print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200

##############################################################
# Assignment Two


def addition(*nums):
    result = 0
    for num in nums:
        if num == 10:
            continue
        if num == 5:
            result -= num
        result += num
    return result


# Tests
print(addition(10, 20, 30, 10, 15))  # 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # 160

###############################################################
# Assignment Three


def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is: ")
        for skill in skills:
            print(f"- {skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")


###############################################################
# Assignment Four


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} You Live In Egypt {country}"


print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
