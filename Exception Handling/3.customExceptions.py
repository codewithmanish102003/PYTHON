# num=int(input("Enter a number between 5 and 9......."))

# if num <5 or num>9:
#     raise ValueError("value Should be between 5 and 9")
# else:
#     print("The value is =",num)


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_value(value):
    if value < 0:
        raise CustomError("Value must be positive")


value = int(input("Type a Number : "))

try:
    check_value(value)

except CustomError as e:
    print(f"Caught an exception : {e}")

else:
    print(f"Value is : {value}")
