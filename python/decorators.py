# def printWhenComplete(someFunc):
#     def wrapper(*args, **kargs):
#         someFunc(*args, **kargs)
#         print("function is done!")
#     return wrapper


# @printWhenComplete
# def countdown(startNum):
#     for i in range(startNum,0,-1):
#         print(i)


# countdown(10)

# @printWhenComplete
# def addThreeNumbers(n1,n2,n3):
#     print(n1+n2+n3)

# addThreeNumbers(1,2,3)

import datetime

def only_even_seconds(someFunc):
    current_time = str(datetime.datetime.now().time())
    current_time= current_time.split(":")
    seconds = round(float(current_time[2]))
    def wrapper(*args, **kargs):
        if seconds % 2 == 0:
            someFunc(*args, **kargs)
    return wrapper

# def only_odd_seconds(someFunc):
#     current_time = str(datetime.datetime.now().time())
#     current_time= current_time.split(":")
#     seconds = round(float(current_time[2]))
#     def twoChainz(*args, **kargs):
#         if seconds % 2 == 1:
#             someFunc(*args, **kargs)
#     return twoChainz

# @only_even_seconds
# def printSeconds():
#     print("its even")

@only_even_seconds
def factorial(num):
	if num == 0:
		return 1
	product = 1
	for number in range(1, num + 1):
		product *= number
	print(product)

factorial(7)