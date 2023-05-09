# Assignment One
import datetime
specificDate = datetime.datetime(2021, 6, 25).date()
today = datetime.datetime(2021, 8, 10).date()

print(
    f"Days From {specificDate} To {today} Is => {(today - specificDate).days}")


################################################################################
# Assignment Two
dateNow = datetime.datetime.now().date()

print(dateNow)
print(dateNow.strftime("%b %d, %Y"))  # "Mar 15, 2023"
print(dateNow.strftime("%d - %b - %Y"))  # "15 - Mar - 2023"
print(dateNow.strftime("%d / %b / %y"))  # "15 / Mar / 23"
print(dateNow.strftime("%d / %B / %Y"))  # "15 / March / 2023"
print(dateNow.strftime("%a, %d %B %Y"))  # "wed, 15 March 2023"
