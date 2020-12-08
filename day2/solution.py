import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()
            print(len(self.input))

    def count_valid_part_1(self):
        cnt = 0
        for i in range(len(self.input) // 3):
            occs, letter, password = self.input[i * 3], self.input[i * 3 + 1][0], self.input[i * 3 + 2]
            occs = [int(n) for n in occs.split("-")]
            min_occ, max_occ, occ = occs[0], occs[1], 0
            for c in password:
                if c == letter:
                    occ += 1
            if occ >= min_occ and occ <= max_occ:
                cnt += 1
        print(cnt)
        return cnt

    def count_valid_part_2(self):
        cnt = 0

        for i in range(len(self.input) // 3):
            occs, letter, password = self.input[i * 3], self.input[i * 3 + 1][0], self.input[i * 3 + 2]
            occs = [int(n) for n in occs.split("-")]
            fst_idx, snd_idx = occs[0] - 1, occs[1] - 1
            if password[fst_idx] == letter and password[snd_idx] != letter or password[snd_idx] == letter and password[fst_idx] != letter:
                cnt += 1
        print(cnt)
        return cnt  

if __name__ == '__main__':
    s = Solution()
    s.count_valid_part_1()
    s.count_valid_part_2()