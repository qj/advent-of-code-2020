import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()
            self.input = [int(n) for n in self.input]

    def possible_two_sum(self, start, end, target):
        m = {}
        for i in range(start, end):
            if target - self.input[i] in m:
                return True
            m[self.input[i]] = target - self.input[i]
        return False

    def solve_part_1(self, n):
        for i in range(0, len(self.input) - n):
            if not self.possible_two_sum(i, i + n, self.input[i + n]):
                return self.input[i + n]
        return None
    
    def solve_part_2(self, target):
        for i in range(2, len(self.input)):
            for j in range(0, len(self.input) - i):
                if sum(self.input[j: j + i]) == target:
                    return min(self.input[j: j + i]) + max(self.input[j: j + i])
        return None
        

if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1(25)
    print(part_1)
    part_2 = s.solve_part_2(part_1)
    print(part_2)