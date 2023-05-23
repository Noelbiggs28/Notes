# create own error
class ImaginaryNumberError(Exception):
    """User defined exception"""
    pass

user_input = int(input("Enter a positive integar: "))

if user_input >=0:
    finalResult = user_input ** 0.5
else:
    raise ImaginaryNumberError