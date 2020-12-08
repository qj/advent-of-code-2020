import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()


    def calculate_id(self, seat):
        l, r = 0, 127
        for c in seat[:7]:
            if c == 'F':
                r = l + (r - l) // 2
            else:
                l = l + (r - l) // 2 + 1
        result = l * 8
        cl, cr = 0, 7
        for c in seat[7:]:
            if c == 'L':
                cr = cl + (cr - cl) // 2
            else:
                cl = cl + (cr - cl) // 2 + 1
        return result + cl
    
    def set_seat_ids(self):
        self.ids = [self.calculate_id(seat) for seat in self.input]

    def max_id(self):
        return max(self.ids)
    
    def find_my_seat(self):
        min_id, max_id = min(self.ids), self.max_id()
        return sum(list(range(min_id, max_id + 1))) - sum(self.ids)

if __name__ == '__main__':
    s = Solution()
    s.set_seat_ids()
    print(s.max_id())
    print(s.find_my_seat())