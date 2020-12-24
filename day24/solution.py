from collections import defaultdict
import copy
import os
import re
import sys 

class Solution:

    def __init__(self, tdata: bool):
        file_name = "test.txt" if tdata else "input.txt"
        with open(os.path.join(sys.path[0], file_name), "r") as f:
            self.input = f.read().splitlines()

    def solve_part_1(self):
        self.black_tiles = set()
        for line in self.input:
            x, y = 0, 0
            for d in re.findall(r'nw|w|sw|e|ne|se', line):
                if d == 'nw':
                    y -= 1
                elif d == 'w':
                    x -= 1
                elif d == 'sw':
                    x -= 1
                    y += 1
                elif d == 'e':
                    x += 1
                elif d == 'se':
                    y += 1
                else:
                    x += 1
                    y -= 1
            if (x, y) in self.black_tiles:
                self.black_tiles.remove((x, y))
            else:
                self.black_tiles.add((x, y))
        return len(self.black_tiles)

    def neighbours(self, x, y):
        return [(x, y - 1), (x - 1, y), (x - 1, y + 1), (x + 1, y), (x, y + 1), (x + 1, y - 1)]

    def solve_part_2(self, iterations):
        for _ in range(iterations):
            neighbours = defaultdict(int)
            for (x, y) in self.black_tiles:
                for (nx, ny) in self.neighbours(x, y):
                    neighbours[(nx, ny)] += 1
            next_black_tiles = set()
            for tile, count in neighbours.items():
                if tile in self.black_tiles and count > 0 and count <= 2:
                    next_black_tiles.add(tile)
                elif tile not in self.black_tiles and count == 2:
                    next_black_tiles.add(tile)
            self.black_tiles = next_black_tiles
        return len(self.black_tiles)
        
if __name__ == '__main__':
    s = Solution(False)
    print(s.solve_part_1())
    print(s.solve_part_2(100))