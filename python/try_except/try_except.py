numerator = 10 ** 3
denominator = int(input("enter a  number for the denominator: "))

try:
    result = float(numerator/denominator)
    print(result)
except ZeroDivisionError:
    print("Division by zero is undefined.")


# try:
    # response.raise_for_status()
# except requests.exceptions.RequestException as e