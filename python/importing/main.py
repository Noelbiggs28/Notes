import mystats #import entire library us like line 4
from myave import average #import single function use like line 5(perfereed way)
some_li = [20, 38,3,43,10,74]
mean_val = mystats.find_mean(some_li)
pro_val = average(some_li)
print(mean_val)
print(pro_val)
