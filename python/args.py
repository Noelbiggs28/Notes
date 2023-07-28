def sumOfNumbers(*args):
    output = 0
    for i in args:
        output +=i
    return output
def concatenate1(**kwargs):
    return kwargs
print(concatenate1(a="hello", b="iamathing", juiceColor="blue"))
def concatenate2(phrase1,phrase2,**kwargs):
    if kwargs["juiceColor"]=="blue":
        return "blue"
    return phrase1 + phrase2
print(concatenate2('hello','iamathing',juiceColor='purple'))
print(concatenate2('hello','iamathing',juiceColor='blue'))