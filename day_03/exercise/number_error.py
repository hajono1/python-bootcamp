class NotANumber(ValueError):
    pass
class NotPositive(ValueError):
    pass
class NotInRange(ValueError):
    pass
userinput = input("Enter a positive number [1,100]: ")

if not userinput.isnumeric() and not userinput[1:].isnumeric():
    raise NotANumber("That is not a number")

number = int(userinput)
if number < 0:
    raise NotPositive("That is a negative number")

if not (1 <= number <= 100):
    raise NotInRange("Not in range")