import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()

    def count_trees(self, row_steps, col_steps):
        cnt = 0
        rows, cols = len(self.input), len(self.input[0])
        r, c = 0, 0
        while r < rows:
            if self.input[r][c % cols] == '#':
                cnt += 1
            r += row_steps
            c += col_steps
        print(cnt)
        return cnt

    def count_trees_multiple(self, traversals):
        result = 1
        for (r, c) in traversals:
            result *= self.count_trees(r, c) 
        print(result)
        return result 

if __name__ == '__main__':
    s = Solution()
    s.count_trees(1, 3)
    s.count_trees_multiple([(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])