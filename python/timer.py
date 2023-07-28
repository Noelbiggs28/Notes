import time

def next_bigger(n):
    if n < 10:
        return -1
    def dict_it(numb):
        dict={
            '9':0,
            '8':0,
            '7':0,
            '6':0,
            '5':0,
            '4':0,
            '3':0,
            '2':0,
            '1':0,
            '0':0,
        }
        strn = str(numb)
        arr=[number for number in strn]
        for number in arr:
            dict[number] +=1
        return dict
    book1 = dict_it(n)
    most = ''
    for key in book1:
        if book1[key] > 0:
            most += key * book1[key]
    most = int(most)
    while n < most:
        n +=1
        book2 = dict_it(n)
        if book1==book2:
            return n
    return -1

startTime = time.time()

print(next_bigger(60543))
print(time.time()-startTime)