import os
import sys 

class Solution:

    def __init__(self, tdata: bool):
        file_name = "test.txt" if tdata else "input.txt"
        with open(os.path.join(sys.path[0], file_name), "r") as f:
            self.input = f.read().splitlines()
            self.card_pub = int(self.input[0])
            self.door_pub = int(self.input[1])

    def calculate_loop_size(self, subject_number, pub_key):
        loop_size = 0
        value = 1
        while value != pub_key:
            value *= subject_number
            value %= 20201227
            loop_size += 1
        return loop_size

    def solve_part_1(self):
        return pow(self.door_pub, self.calculate_loop_size(7, self.card_pub), 20201227)

if __name__ == '__main__':
    s = Solution(False)
    print(s.solve_part_1())