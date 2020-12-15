import sys
import functools
import operator

with open(sys.argv[1]) as f:
    _ = int(f.readline())
    bus_schedule = f.readline().split(sep=',')
busses = [(bus_schedule[i], i) for i in range(len(bus_schedule))] 
busses = [(int(bus), (int(bus) - num) % int(bus)) 
    for bus, num in busses if not 'x' in bus] 
product = functools.reduce(operator.mul, [bus for bus, num in busses], 1)
B = [product // bus for bus, num in busses] 
x = [pow(B[i], -1, busses[i][0]) for i in range(len(B))] 
sum_list = [B[i] * x[i] * busses[i][1] for i in range(len(B))] 
print("Value: ", functools.reduce(operator.add, sum_list, 0) % product)