import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()

    def valid_seat(self, r, c):
        return r >= 0 and r < len(self.input) and c >= 0 and c < len(self.input[0])

    def occupied_seats(self, seats):
        return sum([1 if seats[r][c] == '#' else 0 for r in range(len(seats)) for c in range(len(seats[0]))])

    def num_adjacent_seats(self, r, c):
        count = 0
        if self.valid_seat(r - 1, c):
            count += 1 if self.input[r - 1][c] == '#' else 0
        if self.valid_seat(r - 1, c + 1):
            count += 1 if self.input[r - 1][c + 1] == '#' else 0
        if self.valid_seat(r, c + 1):
            count += 1 if self.input[r][c + 1] == '#' else 0
        if self.valid_seat(r + 1, c + 1):
            count += 1 if self.input[r + 1][c + 1] == '#' else 0
        if self.valid_seat(r + 1, c):
            count += 1 if self.input[r + 1][c] == '#' else 0
        if self.valid_seat(r + 1, c - 1):
            count += 1 if self.input[r + 1][c - 1] == '#' else 0
        if self.valid_seat(r, c - 1):
            count += 1 if self.input[r][c - 1] == '#' else 0
        if self.valid_seat(r - 1, c - 1):
            count += 1 if self.input[r - 1][c - 1] == '#' else 0
        return count

    def num_visible_seats(self, row, col):
        count = 0
        for (r, c) in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            step_factor = 1
            while self.valid_seat(row + step_factor * r, col + step_factor * c):
                if self.input[row + step_factor * r][col + step_factor * c] == '#':
                    count += 1
                    break
                if self.input[row + step_factor * r][col + step_factor * c] == 'L':
                    break
                step_factor += 1
        return count  

    def solve_part_1(self):
        next_gen = []
        while True:
            for row in range(len(self.input)):
                new_row = ""
                for col in range(len(self.input[0])):
                    adj_seats = self.num_adjacent_seats(row, col)
                    if self.input[row][col] == 'L' and adj_seats == 0:
                        new_row += '#'
                    elif self.input[row][col] == '#' and adj_seats >= 4:
                        new_row += 'L'
                    else:
                        new_row += self.input[row][col]
                next_gen.append(new_row)
            if self.input == next_gen:
                return self.occupied_seats(self.input)
            self.input, next_gen = next_gen, []      
        return None
        
    
    def solve_part_2(self):
        next_gen = []
        while True:
            for row in range(len(self.input)):
                new_row = ""
                for col in range(len(self.input[0])):
                    vis_seats = self.num_visible_seats(row, col)
                    if self.input[row][col] == 'L' and vis_seats == 0:
                        new_row += '#'
                    elif self.input[row][col] == '#' and vis_seats >= 5:
                        new_row += 'L'
                    else:
                        new_row += self.input[row][col]
                next_gen.append(new_row)
            if self.input == next_gen:
                return self.occupied_seats(self.input)
            self.input, next_gen = next_gen, []     
        return None
        

if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)