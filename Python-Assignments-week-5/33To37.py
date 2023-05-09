# Assignment One
print(bool("name"))
print(bool(True))
print(bool(2133))
print(bool(["Hi"]))

print(bool(""))
print(bool(False))
print(bool(0))
print(bool([]))


# Assignment Two
html = 80
css = 60
javascript = 70

# Needed Output
print(html > 50 and css > 50 and javascript > 50)
# True


# Assignment Three
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

# Needed Output
# True
# False


# Assignment Four
num_one = 10
num_two = 20

result = num_one + num_two
print(result)
result **= 3
print(result)
result %= 26000
print(result)
result /= 5
print(result)
print(type(str(result)))
# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str' >
