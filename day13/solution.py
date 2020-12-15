import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()
            self.earliest_departure = int(self.input[0])
            self.bus_ids = [int(id) for id in filter(lambda i: i != 'x', self.input[1].split(","))]

    def solve_part_1(self):  
        min_diff, min_id = float("inf"), None
        for id in self.bus_ids:
            num_prev_busses = (self.earliest_departure - 1) // id
            diff = (num_prev_busses + 1) * id - self.earliest_departure
            if diff < min_diff:
                min_diff, min_id = diff, id 
        return min_diff * min_id 
    
    def solve_chinese_remainder(self, n, a):
        from functools import reduce
        N = reduce(lambda x, y: x * y, n)
        sum = 0
        for n_i, a_i in zip(n, a):
            p = N // n_i
            sum += a_i * self.eed(p, n_i) * p
        return sum % N

    def eed(self, a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1 

    def solve_part_2(self):
        n, a = [], []
        times = self.input[1].split(",")
        for i in range(len(times)):
            if times[i] != 'x':
                n.append(int(times[i]))
                a.append(int(times[i]) - i)
        return self.solve_chinese_remainder(n, a)


if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)