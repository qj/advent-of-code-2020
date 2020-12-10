import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()
            self.input = sorted([int(n) for n in self.input])


    def solve_part_1(self):
        count = {1: 0, 2: 0, 3: 1}
        j = 0
        for i in range(len(self.input)):
            count[self.input[i] - j] += 1
            j = self.input[i]
        return count[1] * count[3]

    def solve_part_2(self):
        cache = {self.input[-1]: 1}
        def solve(n, count):
            if n in cache:
                return cache[n]
            for i in range(1, 4):
                if n + i in self.input:
                    ways = solve(n + i, count)
                    cache[n + i] = ways
                    count += ways
            return count 
        return solve(0, 0)
            
if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)